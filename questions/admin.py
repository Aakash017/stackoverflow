from django.contrib import admin

# Register your models here.
from .models import Content, Comment


class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_question', ]


admin.site.register(Content, ContentAdmin)
admin.site.register(Comment)