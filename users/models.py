import os
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

def get_user_avatar_path(instance, filename):
    user_id = instance.user.id if instance.user else 'unknown'
    return os.path.join('users_images', str(user_id), filename)


def get_user_image_path(instance, filename):
    user_id = instance.gallery.user.id if instance.gallery and instance.gallery.user else 'unknown'
    return os.path.join('users_images', str(user_id), 'images', filename)


def get_user_video_path(instance, filename):
    user_id = instance.gallery.user.id if instance.gallery and instance.gallery.user else 'unknown'
    return os.path.join('users_images', str(user_id), 'videos', filename)


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='profile', 
        verbose_name='Користувач'
    )
    birth = models.DateField(blank=True, null=True, verbose_name='Дата народження')
    photo = models.ImageField(upload_to=get_user_avatar_path, blank=True, verbose_name='Основна світлина')
    hobby = models.CharField(max_length=400, blank=True, verbose_name='Хобі')
    city = models.CharField(max_length=40, blank=True, verbose_name='Місто')
    phone = models.CharField(max_length=15, blank=True, verbose_name='Телефон')
    info = models.TextField(blank=True, verbose_name='Інформація')

    class Meta:
        verbose_name = 'Профіль користувача'
        verbose_name_plural = 'Профілі користувачів'

    def __str__(self):
        return f"Профіль: {self.user.username}"


class UserGallery(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='gallery', 
        verbose_name='Власник галереї'
    )

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереї'

    def __str__(self):
        return f"Галерея: {self.user.username}"


class UserImage(models.Model):
    gallery = models.ForeignKey(
        UserGallery, 
        on_delete=models.CASCADE, 
        related_name='images', 
        verbose_name='Галерея'
    )
    image = models.ImageField(upload_to=get_user_image_path, verbose_name='Зображення')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата завантаження')

    class Meta:
        verbose_name = 'Зображення'
        verbose_name_plural = 'Зображення'
        ordering = ['-created_at']


class UserVideo(models.Model):
    gallery = models.ForeignKey(
        UserGallery, 
        on_delete=models.CASCADE, 
        related_name='videos', 
        verbose_name='Галерея'
    )
    video = models.FileField(upload_to=get_user_video_path, verbose_name='Відео')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата завантаження')

    class Meta:
        verbose_name = 'Відео'
        verbose_name_plural = 'Відео'
        ordering = ['-created_at']


class UserMessage(models.Model):
    sender = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='sent_messages', 
        verbose_name='Відправник'
    )
    receiver = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='received_messages', 
        verbose_name='Отримувач'
    )
    content = models.TextField(verbose_name='Текст повідомлення')
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Час відправки')

    class Meta:
        verbose_name = 'Повідомлення'
        verbose_name_plural = 'Повідомлення'
        ordering = ['timestamp']
        indexes = [
            models.Index(fields=['sender', 'receiver']),
        ]

    def __str__(self):
        return f"{self.sender} -> {self.receiver}: {self.content[:20]}"