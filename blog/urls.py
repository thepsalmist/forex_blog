from django.urls import path

from . import views
from .views import post_list, post_detail

app_name = "blog"

urlpatterns = [
    path("", views.post_list, name="home"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/",
        views.post_detail,
        name="post_detail",
    ),
]
