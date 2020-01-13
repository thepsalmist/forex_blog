from django.db import models


class ProductCategory(models.Model):
    CATEGORY_CHOICES = (
        ("book", "Book"),
        ("course", "Course"),
    )
    title = models.CharField(choices=CATEGORY_CHOICES, max_length=200, default="book")

    class Meta:
        ordering = ("title",)
        verbose_name = "productcategory"
        verbose_name_plural = "productcategories"

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField()
    url = models.URLField()
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        related_name="product_categories",
        default="book",
    )

    def __str__(self):
        return self.title
