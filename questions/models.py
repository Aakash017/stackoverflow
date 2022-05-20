from django.db import models
from users.models import User
from markupfield.fields import MarkupField


# Create your models here.


class Content(models.Model):
    title = models.CharField(max_length=500, blank=True)
    body = MarkupField(default_markup_type="plain", null=True)
    is_question = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tagging = models.JSONField(default=list)

    def __str__(self):
        return self.title

