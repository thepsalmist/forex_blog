from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from .models import Post, Category, Comment
from .forms import CommentForm


def get_category_count():
    queryset = Post.published.values("categories__title").annotate(
        Count("categories__title")
    )
    return queryset


def post_list(request, category_slug=None):
    posts = Post.published.all()
    latest_posts = Post.published.order_by("-publish")[:4]
    categories = Category.objects.all()
    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=category)
    paginator = Paginator(posts, 6)
    page_variable = request.GET.get("page")
    try:
        posts = paginator.page(page_variable)
    except EmptyPage:
        posts = paginator.page(1)
    except PageNotAnInteger:
        posts = paginator.page(paginator.num_pages)

    context = {
        "posts": posts,
        "categories": categories,
        "category": category,
        "page_variable": page_variable,
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
    comments = post.comments.filter(active=True)
    post_tags_ids = post.tags.values_list("id", flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count("tags")).order_by(
        "-same_tags", "-publish"
    )
    # Increment view_count +1
    post.view_count += 1
    post.save(update_fields=["view_count"])

    context = {"post": post, "comments": comments, "similar_posts": similar_posts}

    return render(request, "blog/post_detail.html", context)


@login_required
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()

    else:
        comment_form = CommentForm()

    context = {"new_comment": new_comment, "comment_form": comment_form}

    return render(request, "blog/post_detail.html", context)

