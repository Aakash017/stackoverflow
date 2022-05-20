from django import forms
from . import models


class QuestionForm(forms.ModelForm):
    class Meta:
        model = models.Content
        fields = [
            'title', 'body', 'tagging'
        ]
