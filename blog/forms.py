from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    pass

    class Meta:
        model = Comment
        fields = ["body"]

