from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Product, ProductCategory


def shop_products(request):
    books = Product.objects.filter(category__title="book")[:8]
    courses = Product.objects.filter(category__title="course")[:8]
    context = {
        "books": books,
        "courses": courses,
    }
    return render(request, "shop/products.html", context)
