from django import forms
from .models import Comment, Contact


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

