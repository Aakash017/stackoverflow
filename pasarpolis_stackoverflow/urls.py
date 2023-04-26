"""pasarpolis_stackoverflow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from questions import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('login/', views.login),
    path('logout/', views.logout),
    path('articles/', include('questions.urls'), name='articles'),
    path('users/', include('users.urls')),
    path('add_question/', views.add_question),
    path('add_article/', views.add_article),
    path('add_article_backend/', views.add_article_backend),
    path('add_question_backend/', views.add_question_backend),
    path('question_detail/<pk>/upvote_question/', views.upvote_question, name="upvote_question"),
    path('question_detail/<pk>/upvote_comment/<ck>/', views.upvote_comment, name="upvote_comment")
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
