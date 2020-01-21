from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from .models import Post, Category, Comment, Video
from .forms import CommentForm, ContactForm
from marketting.models import SignUp


def get_category_count():
    queryset = Post.published.values("category__title").annotate(
        Count("category__title")
    )
    return queryset


def post_list(request, category_slug=None):
    posts = Post.published.all()
    videos = Video.objects.all()
    latest_posts = Post.published.order_by("-publish")[:4]
    popular = Post.published.order_by("-view_count")[:5]
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=category)

    # get email from request for signup
    if request.method == "POST":
        email = request.POST["email"]
        new_signup = SignUp()
        new_signup.email = email
        new_signup.save()
        messages.info(request, "Thank you for subscribing")
        return redirect("blog:home")

    category_count = get_category_count()
    paginator = Paginator(posts, 6)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        "posts": posts,
        "videos": videos,
        "popular": popular,
        "category": category,
        "categories": categories,
        "category_count": category_count,
        "page": page,
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
    categories = Category.objects.all()
    latest_posts = Post.published.order_by("-publish")[:4]
    popular = Post.published.order_by("-view_count")[:5]
    comments = post.comments.filter(active=True)
    post_tags_ids = post.tags.values_list("id", flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count("tags")).order_by(
        "-same_tags", "-publish"
    )
    # Increment view_count +1
    post.view_count += 1
    post.save(update_fields=["view_count"])

    context = {
        "post": post,
        "comments": comments,
        "similar_posts": similar_posts,
        "categories": categories,
        "latest_posts": latest_posts,
        "popular": popular,
    }

    return render(request, "blog/post_detail.html", context)


def search(request):
    categories = Category.objects.all()
    queryset = Post.published.all()
    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        ).distinct()
    context = {
        "queryset": queryset,
        "categories": categories,
    }
    return render(request, "blog/search.html", context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            name = form.cleaned_data.get("name")
            messages.success(request, f"{name}Thank you for contacting us")
            return redirect("blog:home")
    else:
        form = ContactForm()

    context = {"form": form}
    return render(request, "blog/contact.html", context)


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


def faq(request):
    posts = Post.published.filter(category__title="faq")
    context = {"posts": posts}
    return render(request, "blog/faq.html", context)


def analysis(request):
    return render(request, "blog/analysis.html", context={})


def news(request):
    return render(request, "blog/news.html", context={})


def education(request):
    return render(request, "blog/education.html", context={})


def privacy(request):
    return render(request, "blog/privacy.html", context={})


def terms_of_use(request):
    return render(request, "blog/terms_of_use.html", context={})
