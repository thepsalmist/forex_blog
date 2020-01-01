from django.shortcuts import render


def shop_products(request):
    return render(request, "shop/products.html", context={})
