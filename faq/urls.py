from django.urls import path

from . import views
from .views import faq

app_name = "faq"

urlpatterns = [
    path("", views.faq, name="faq"),
]
