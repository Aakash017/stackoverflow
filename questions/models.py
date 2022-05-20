from django.db import models
from users.models import User
from markupfield.fields import MarkupField


# Create your models here.


class Content(models.Model):
    title = models.CharField(max_length=500, blank=True)
    body = MarkupField(default_markup_type="html", null=True)
    is_question = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tagging = models.JSONField(default=list)
    upvote = models.IntegerField(default=0, null=True)


class Comment(models.Model):
    question = models.ForeignKey(Content, blank=True, null=True, on_delete=models.SET_NULL)
    comment = MarkupField(default_markup_type="html", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    upvote = models.IntegerField(default=0, null=True)
