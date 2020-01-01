from django.urls import path

from . import views
from .views import shop_products

app_name = "shop"

urlpatterns = [path("", views.shop_products, name="shop_products")]

