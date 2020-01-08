from django.urls import path

from . import views
from .views import post_list, post_detail, analysis, education

app_name = "blog"

urlpatterns = [
    path("", views.post_list, name="home"),
    # path("<slug:category_slug>/", views.post_list, name="post_list_by_category"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/",
        views.post_detail,
        name="post_detail",
    ),
    path("education/", views.education, name="education"),
    path("analysis/", views.analysis, name="analysis"),
]
