from django.urls import path

from . import views
from .views import index

app_name = "blog"

urlpatterns = [path("", views.index, name="home")]
