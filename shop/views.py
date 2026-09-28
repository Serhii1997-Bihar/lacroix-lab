from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q

from shop.models import Product, Category, Brand, Employee
from shop.forms import SearchForm
from cart.forms import CartAddProductForm


def dashboard(request):
    search_form = SearchForm(request.GET)
    query = request.GET.get('query')

    all_products = Product.objects.all().select_related('category', 'country', 'brand')

    if search_form.is_valid() and query:
        all_products = all_products.filter(
            Q(name__icontains=query) | Q(about__icontains=query)
        )

    all_products = all_products.order_by('-created_at')

    paginator = Paginator(all_products, 8)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    context = {
        'products': products,
        'form': search_form,
        'query': query,
    }
    return render(request, 'shop/dashboard.html', context)


def categories(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    query = request.GET.get('query')

    category_products = Product.objects.filter(category=category).select_related(
        'category', 'country', 'brand'
    ).order_by('-created_at')

    if query:
        category_products = category_products.filter(name__icontains=query)

    paginator = Paginator(category_products, 8)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    context = {
        'category': category,
        'products': products,
        'query': query,
    }
    return render(request, 'shop/categories.html', context)


def brands(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    query = request.GET.get('query')

    brand_products = Product.objects.filter(brand=brand).select_related(
        'category', 'country', 'brand'
    ).order_by('-created_at')

    if query:
        brand_products = brand_products.filter(name__icontains=query)

    paginator = Paginator(brand_products, 8)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    context = {
        'brand': brand,
        'products': products,
        'query': query,
    }
    return render(request, 'shop/brands.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(
        Product.objects.select_related('category', 'country', 'brand').prefetch_related('sizes'),
        id=product_id
    )
    sizes = product.sizes.all()
    cart_product_form = CartAddProductForm(sizes=sizes)

    context = {
        'product': product,
        'sizes': sizes,
        'form': cart_product_form,
    }
    return render(request, 'shop/product_details.html', context)


def team(request):
    admins = Employee.objects.all().order_by('?')
    context = {'admins': admins}
    return render(request, 'shop/team.html', context)