from django.urls import path

from . import views
from .views import (
    post_list,
    post_detail,
    analysis,
    education,
    news,
    contact,
    privacy,
    terms_of_use,
    about_us,
)

app_name = "blog"

urlpatterns = [
    path("", views.post_list, name="home"),
    path("search/", views.search, name="search"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about_us, name="about_us"),
    path(
        "category/<slug:category_slug>/", views.post_list, name="post_list_by_category"
    ),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/",
        views.post_detail,
        name="post_detail",
    ),
    path("category/analysis/", views.analysis, name="analysis"),
    path("category/news/", views.news, name="news"),
    path("category/education/", views.education, name="education"),
    path("privacy/", views.privacy, name="privacy"),
    path("terms_of_use/", views.terms_of_use, name="terms_of_use"),
]
