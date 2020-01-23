from django.contrib import admin
from .models import ForexFaq, Faq


@admin.register(ForexFaq)
class ForexFaqAdmin(admin.ModelAdmin):
    list_display = ("title", "publish")


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "message")
    list_filter = ("subject", "name")
    search_fields = ("subject",)
