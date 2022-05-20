from django.contrib import admin
from django.urls import path
from questions import views
app_name = 'articles'

urlpatterns = [
    path('', views.articles_list, name='articles_list'),
    path('articles_detail/<pk>', views.articles_detail, name='articles_detail'),
    path('questions_list', views.questions_list),
    path('create_question/', views.create_question, name="create_question"),
    path('question_detail/<pk>/', views.question_detail, name='question_detail'),
    path('edit_question/<pk>', views.edit_question, name="edit_question"),
    path('search/', views.search, name="search"),
]