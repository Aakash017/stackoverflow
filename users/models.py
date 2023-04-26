from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=250)
    profile_pic = models.FileField(upload_to='documents/', null=True)
    points = models.IntegerField(default=0,null=True)


    def __str__(self):
        return self.email

    # def save(self, *args, **kwargs):
    #     self.set_password(self.password)
    #     if not self.username:
    #         self.username = self.email
    #     return super().save()

