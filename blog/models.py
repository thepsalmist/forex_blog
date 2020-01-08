from django.db import models
from tinymce import models as tinymce_models
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status="published")


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default="default.jpeg", upload_to="Authors")

    def __str__(self):
        return self.user.username


class Category(models.Model):
    CATEGORY_CHOICES = (
        ("currency", "CURRENCY"),
        ("banks", "BANKS"),
        ("crypto", "CRYPTO"),
        ("commodities", "COMMODITIES"),
    )
    title = models.CharField(
        choices=CATEGORY_CHOICES, max_length=100, default="currency"
    )
    slug = models.SlugField(max_length=200, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_list_by_category", args=[self.slug])


class Post(models.Model):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, unique_for_date="publish")
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="blog_posts"
    )
    body = tinymce_models.HTMLField()
    thumbnail = models.ImageField(
        default="images/resource/blackroq_5.jpg", upload_to="Posts %Y%M%d"
    )
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    view_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()

    class Meta:
        ordering = ("publish",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "blog:post_detail",
            args=[self.publish.year, self.publish.month, self.publish.day, self.slug],
        )


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ("created",)

    def __str__(self):
        return f"Comment by {self.user.username}on {self.post}"

