from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.exceptions import PermissionDenied

from users.forms import UserRegistrationForm, UserLoginForm, UserEditForm, ProfileEditForm, GalleryForm, MessageForm
from users.models import UserGallery, UserImage, UserVideo, UserProfile, UserMessage

def create_user(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileEditForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile_form.save()

            return redirect('user_dashboard', user_id=user.id)
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileEditForm()

    return render(request, 'users/create_user.html', {'user_form': user_form, 'profile_form': profile_form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None and user.is_active:
                auth_login(request, user)

                return redirect('user_dashboard', user_id=user.id)
    else:
        form = UserLoginForm()

    return render(request, 'users/login.html', {'form': form})


@login_required
def user_dashboard(request, user_id):
    if request.user.id != user_id:
        return redirect('user_dashboard', user_id=request.user.id)

    user = request.user
    profile, _ = UserProfile.objects.get_or_create(user=user)
    gallery, _ = UserGallery.objects.get_or_create(user=user)

    images = UserImage.objects.filter(gallery=gallery)[:10]
    vids = UserVideo.objects.filter(gallery=gallery)

    paginator = Paginator(vids, 5)
    page = request.GET.get('page')
    videos = paginator.get_page(page)

    context = {
        'user': user,
        'profile': profile,
        'gallery': gallery,
        'images': images,
        'videos': videos,
    }
    return render(request, 'users/user_dashboard.html', context)


@login_required
def delete_image(request, user_id):
    image = get_object_or_404(UserImage, id=user_id)
    if image.gallery.user != request.user:
        raise PermissionDenied
    image.delete()
    return redirect('account', id=request.user.id)


@login_required
def delete_video(request, user_id):
    video = get_object_or_404(UserVideo, id=user_id)
    if video.gallery.user != request.user:
        raise PermissionDenied
    video.delete()
    return redirect('account', id=request.user.id)


def user_logout(request):
    auth_logout(request)
    return redirect('user_login')


@login_required
def edit_data(request):
    user = request.user
    profile, _ = UserProfile.objects.get_or_create(user=user)
    gallery, _ = UserGallery.objects.get_or_create(user=user)

    if request.method == 'POST':
        user_form = UserEditForm(instance=user, data=request.POST)
        profile_form = ProfileEditForm(instance=profile, data=request.POST, files=request.FILES)
        gallery_form = GalleryForm(data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid() and gallery_form.is_valid():
            user_form.save()
            profile_form.save()

            images = request.FILES.getlist('images')
            if images:
                UserImage.objects.bulk_create([
                    UserImage(gallery=gallery, image=img) for img in images
                ])

            videos = request.FILES.getlist('videos')
            if videos:
                UserVideo.objects.bulk_create([
                    UserVideo(gallery=gallery, video=vid) for vid in videos
                ])

            return redirect('account', id=user.id)
    else:
        user_form = UserEditForm(instance=user)
        profile_form = ProfileEditForm(instance=profile)
        gallery_form = GalleryForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'gallery_form': gallery_form
    }
    return render(request, 'users/edit_data.html', context)


def users_list(request):
    users = User.objects.select_related('profile').exclude(id=request.user.id)
    return render(request, 'users/users_list.html', {'users': users})

def user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile, _ = UserProfile.objects.get_or_create(user=user)
    gallery, _ = UserGallery.objects.get_or_create(user=user)

    images = UserImage.objects.filter(gallery=gallery)[:10]
    vids = UserVideo.objects.filter(gallery=gallery)

    paginator = Paginator(vids, 5)
    page = request.GET.get('page')
    videos = paginator.get_page(page)

    context = {
        'profile_user': user,
        'profile': profile,
        'images': images,
        'videos': videos,
    }
    return render(request, 'users/user_profile.html', context)


@login_required
def send_message(request, user_id):
    recipient = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = recipient
            message.save()
            return redirect('user_profile', id=recipient.id)
    else:
        form = MessageForm()

    return render(request, 'users/send_message.html', {'user': recipient, 'form': form})


@login_required
def message_in(request):
    req_user = request.user
    participants_ids = UserMessage.objects.filter(
        Q(sender=req_user) | Q(receiver=req_user)
    ).values_list('sender_id', 'receiver_id')

    unique_ids = {uid for pair in participants_ids for uid in pair if uid != req_user.id}
    sender_users = User.objects.filter(id__in=unique_ids)

    context = {
        'sender_users': sender_users,
        'req_user': req_user
    }
    return render(request, 'users/message_in.html', context)


@login_required
def dialogue(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    req_user = request.user

    messages_qs = UserMessage.objects.filter(
        Q(sender=req_user, receiver=other_user) |
        Q(sender=other_user, receiver=req_user)
    ).order_by('timestamp')

    paginator = Paginator(messages_qs, 8)
    page = request.GET.get('page')
    messages = paginator.get_page(page)

    context = {
        'user': other_user,
        'messages': messages,
        'req_user': req_user,
    }
    return render(request, 'users/dialogue.html', context)