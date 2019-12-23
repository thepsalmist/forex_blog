from django.contrib import admin
from .models import Post, Category, Author, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "publish", "status")
    list_filter = ("status", "status", "author", "publish")
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ("author",)
    date_hierachy = "publish"
    ordering = ("status", "publish")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "comment", "created", "active")
    list_filter = ("active", "created", "updated")
    search_fields = ("user", "comment")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("user",)

