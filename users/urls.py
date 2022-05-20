from django.urls import path, include

from users import views

urlpatterns = [
    path('', views.list_users),
    path('login/', views.login)
]
