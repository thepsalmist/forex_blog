from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(models.ModelAdmin):
    list_display = ("title", "slug", "author", "publish", "status")
    list_filter = ("status", "status", "author", "publish")
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ("author",)
    date_hierachy = "publish"
    ordering = ("status", "publish")

