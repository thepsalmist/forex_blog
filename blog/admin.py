from django.contrib import admin
from .models import Post, Category, Author, Comment, Contact


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
    list_display = ("user", "post", "body", "created", "active")
    list_filter = ("active", "created", "updated")
    search_fields = ("user", "body")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("user",)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "message")
