from django import forms
from .models import Comment, Contact, Faq


class CommentForm(forms.ModelForm):
    pass

    class Meta:
        model = Comment
        fields = ["body"]


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "email", "message")
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Name"}),
            "email": forms.TextInput(attrs={"placeholder": "Email"}),
            "message": forms.Textarea(attrs={"placeholder": "Message...", "rows": 20}),
        }


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
