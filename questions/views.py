from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy

from questions import forms, models
from questions.models import Content


def home(request):
    return render(request, template_name='base.html')


def login(request):
    return render(request, template_name='login.html')


def logout(request):
    try:
        del request.session['user_email']
        del request.session['user_id']
    except:
        return render(request, template_name='login.html')
    return render(request, template_name='login.html')


def articles_detail(request, pk):
    article = Content.objects.get(id=pk)
    print("rs ", request.session)
    print("rs ", request.session.get("user_email"))
    print("rs ", request.session.get("user_id"))
    return render(request, template_name='article_detail.html', context={"article": article})


def questions(request):
    return render(request, template_name='questions.html')


def articles_list(request):
    _articles = Content.objects.all()
    print("logged in user email", request.session.get("user_email"))
    return render(request, template_name='articles.html', context={'articles': _articles})


def questions_list(request):
    _articles = Content.objects.filter(is_question=True)
    print("logged in user email", request.session.get("user_email"))
    return render(request, template_name='question_list.html', context={'questions': _articles})


def question_detail(request, pk):
    question = get_object_or_404(Content, pk=pk)
    return render(request, 'question_detail.html', {
        'question': question,
    })


@login_required
def create_question(request):
    form = forms.QuestionForm()
    if request.method == "POST":
        form = forms.QuestionForm(request.POST)
        if form.is_valid:
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            messages.success(request, "Question created successfully")
            return HttpResponseRedirect(reverse_lazy('questions:question_detail', kwargs={'pk': question.pk}))
    return render(request, 'question_form.html', {'form': form})


@login_required
def edit_question(request, pk):
    question = get_object_or_404(Content, pk=pk)
    form_class = forms.QuestionForm
    form = form_class(instance=question)
    if request.method == "POST":
        form = form_class(request.POST, instance=question)
        if form.is_valid:
            form.save()
            messages.success(request, "Question updated successfully")
            return HttpResponseRedirect(reverse_lazy('questions:question_detail', kwargs={'pk': question.pk}))
    return render(request, 'question_form.html', {
        'form': form,
        'question': question
    })


def search(request):
    print("request :", request)
    search_k = request.POST["search"]
    print(search_k)
    results = Content.objects.filter(title__icontains=search_k)
    return render(request, template_name='search.html', context={'questions': results})

