from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.shortcuts import get_object_or_404

from blog.models import Post
from .serializers import PostListSerializer


class PostListAPIView(ListAPIView):
    queryset = Post.published.all()
    serializer_class = PostListSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.published.all()
    serializer_class = PostListSerializer

