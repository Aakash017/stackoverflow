from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy

from questions import forms, models
from questions.models import Content, Comment
from users.models import User


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
    comments = Comment.objects.filter(question_id=article.id)
    con_obj = Content.objects.get(id=article.id)
    return render(request, template_name='article_detail.html', context={"article": article,
                                                                         'comments': comments,
                                                                         'upvote': con_obj.upvote})


def questions(request):
    return render(request, template_name='questions.html')


def add_question(request):
    return render(request, template_name='add_question.html')


def add_article(request):
    return render(request, template_name='add_article.html')


def add_question_backend(request):
    content_title = request.POST['title']
    content_description = request.POST['description']
    content_tags = [request.POST['tags']]
    content = Content.objects.create(title=content_title, body=content_description, tagging=content_tags,
                                     is_question=True)
    content.author_id = request.session.get("user_id")
    content.save()
    return redirect(f'/articles/question_detail/{content.id}/', content={"question": content})


def add_article_backend(request):
    content_title = request.POST['title']
    content_description = request.POST['description']
    content_tags = [request.POST['tags']]
    content = Content.objects.create(title=content_title, body=content_description, tagging=content_tags, )
    content.author_id = request.session.get("user_id")
    content.save()
    return redirect(f'/articles/articles_detail/{content.id}', content={"article": content})


def articles_list(request):
    _articles = Content.objects.filter(is_question=False)
    print("logged in user email", request.session.get("user_email"))
    return render(request, template_name='articles.html', context={'articles': _articles})


def questions_list(request):
    _articles = Content.objects.filter(is_question=True)
    print("logged in user email", request.session.get("user_email"))
    return render(request, template_name='question_list.html', context={'questions': _articles})


def question_detail(request, pk):
    question = get_object_or_404(Content, pk=pk)
    comments = Comment.objects.filter(question_id=question.id)
    con_obj = Content.objects.get(id=question.id)
    print("Comment values are", comments)
    print("content obj is", con_obj.id)
    print("content obj upvote is", con_obj.upvote)
    return render(request, 'question_detail.html',
                  context={'question': question, 'comments': comments, 'upvote': con_obj.upvote})


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
    search_k = request.POST["search"]
    results = Content.objects.filter(title__icontains=search_k)
    return render(request, template_name='search.html', context={'questions': results})


def post_comment(request, pk):
    print("Hello there")
    question = get_object_or_404(Content, pk=pk)
    comment_content = request.POST['comment']
    user = request.session["user_id"]
    # user_mail = User.object.filter(id = user)
    print(comment_content)
    print(question.id)
    print(user)
    fields = Comment._meta.get_fields()
    print(fields)
    a = Comment(question_id=question.id, comment=comment_content, author_id=user)
    a.save()
    if question.is_question:
        return redirect(f'/articles/question_detail/{pk}/', content={"question": question})
    else:
        return redirect(f'/articles/articles_detail/{pk}', content={"article": question})



def upvote_question(request, pk):
    print('inside upvote_question api')
    user_id = request.session["user_id"]
    print("user id is", user_id)
    user = get_object_or_404(User, pk=user_id)
    print("user is", user, type(user))
    question = get_object_or_404(Content, pk=pk)
    print("question is", question, type(question))
    user_upvote_increase = User.objects.get(id = question.author.id)
    print("User to upvote is", user_upvote_increase.id)
    if user_id != question.author:
        question.upvote = question.upvote + 1
        question.save()
        # question.update(upvote=question.upvote+1)
        # user.update(points=user.points+1)
        user_upvote_increase.points = user_upvote_increase.points + 1
        user_upvote_increase.save()
    comments = Comment.objects.filter(question_id=question.id)
    con_obj = Content.objects.get(id=question.id)

    # print("Comment values are", comments)
    if question.is_question:
        return render(request, 'question_detail.html',
                  context={'question': question, 'comments': comments, 'upvote': con_obj.upvote})
    else:
        return render(request, 'articles_detail.html',
                  context={'article': question, 'comments': comments, 'upvote': con_obj.upvote})
    # question_detail(pk = pk)
    # return render(request, template_name='question_detail.html', context={"question": question})


def upvote_comment(request, pk, ck):
    user_id = request.session["user_id"]
    user = get_object_or_404(User, pk=user_id)
    comment = get_object_or_404(Comment, pk=ck)
    question = get_object_or_404(Content, pk=pk)
    user_upvote_increase = User.objects.get(id = comment.author.id)
    if user_id != comment.author.id:
        # print('User comment upvote inside else if', comment.upvote)
        comment.upvote = comment.upvote + 1
        comment.save()
        # User.update(points=User.points + 1)
        
        user_upvote_increase.points += 1

        user_upvote_increase.save()
    comments = Comment.objects.filter(question_id=question.id)
    # print('User comment upvote is', comment.upvote)
    if question.is_question:
        return redirect(f'/articles/question_detail/{question.id}', context={'question': question, 'comments': comments,
                                                                             'upvote': question.upvote})
    else:
        return redirect(f'/articles/articles_detail/{question.id}', context={'article': question, 'comments': comments,
                                                                            'upvote': question.upvote})

    # return render(request, template_name='article_detail.html', context={"article": question})
