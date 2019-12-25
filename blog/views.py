from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Category
from .forms import CommentForm


def get_category_count():
    queryset = Post.published.values("categories__title").annotate(
        Count("categories__title")
    )
    return queryset


def post_list(request):
    posts = Post.published.all()
    featured_posts = Post.published.order_by("-publish")[:6]
    latest_posts = Post.published.order_by("-publish")[:4]
    categories = Category.objects.all()
    context = {
        "posts": posts,
        "categories": categories,
        "featured_posts": featured_posts,
        "latest_posts": latest_posts,
    }
    return render(request, "blog/index.html", context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        status="published",
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    context = {"post": post}
    return render(request, "blog/post_detail.html", context)


@login_required
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()

    else:
        comment_form = CommentForm()

    return redirect(request, "blog/index.html", context)

