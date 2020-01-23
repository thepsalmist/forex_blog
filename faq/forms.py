from django import forms
from .models import Faq


class FaqForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ("name", "email", "subject", "message")
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your Name*"}),
            "email": forms.TextInput(attrs={"placeholder": "Your Email"}),
            "subject": forms.TextInput(attrs={"placeholder": "Subject"}),
            "message": forms.Textarea(
                attrs={"placeholder": "Your Question", "rows": 20}
            ),
        }
