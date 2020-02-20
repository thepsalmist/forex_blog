from django.urls import path

from .views import PostListAPIView, PostDetailAPIView

app_name = "blog_api"

urlpatterns = [
    path("", PostListAPIView.as_view(), name="list"),
    path("<pk>/", PostDetailAPIView.as_view(), name="post_detail",),
]

