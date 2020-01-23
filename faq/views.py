from django.shortcuts import render
from django.contrib import messages
from .models import ForexFaq
from .forms import FaqForm


def faq(request):
    faqs = ForexFaq.objects.all()
    if request.method == "POST":
        form = FaqForm(request.POST)
        if form.is_valid:
            form.save()
            name = form.cleaned_data.get("name")
            messages.success(request, f" Thank you {name} for your question")
    else:
        form = FaqForm()
    context = {"faqs": faqs, "form": form}
    return render(request, "faq/faq.html", context)
