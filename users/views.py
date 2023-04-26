from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from .forms import LoginForm

# Create your views here.
from .models import User
from questions.models import Content

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    print(email, password)
    _user = User.objects.get(email=email)
    username = _user.username

    user = authenticate(username=username, password=password)
    print("user :", user)
    if user is not None:
        # login(request, user)
        request.session["user_email"] = user.email
        request.session["user_id"] = user.id
        if user.profile_pic:
            request.session["user_profile_pic"] = user.profile_pic.url
        return redirect('/articles/')
    else:
        return redirect('/login/')


def list_users(request):
    users_list =[]
    users = User.objects.all()
    for user in users:
        content = {}
        articles = Content.objects.filter(author__email=user.email)
        content["articles"] = articles
        content["email"] = user.email
        content["name"] = user.get_full_name()
        content["pic"] = user.profile_pic
        content["date_joined"] = user.date_joined
        content["score"] = user.points
        users_list.append(content)
    newlist = sorted(users_list, key=lambda d: d['score'], reverse=True) 


    return render(request, template_name='users_list.html', context={'users': newlist})
