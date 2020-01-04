from django.contrib.sitemaps import Sitemap
from .models import Post

# create custom sitemap by inheriting from sitemap class
class PostSitemap(Sitemap):
    # changefreq and priority indicate change frequency and relevance to website (max=1)
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        # the items method returns objects queryset to include in sitemap
        return Post.published.all()

    def lastmod(self, obj):
        # receives each object returned by items and returns last time ovject was modified
        return obj.updated

