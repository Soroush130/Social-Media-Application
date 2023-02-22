from django.shortcuts import render, redirect
from accounts.models import User
from tags.models import Tag
from .models import Article
from .forms import NewArticleForm


def list_article(request):
    current_user = request.user
    articles = Article.objects.filter(user__in=current_user.following.all())
    context = {
        'articles': articles
    }
    return render(request, 'articles/list_article.html', context)


def detail_article(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except:
        return redirect('page_not_found')

    context = {
        'article': article,
    }
    return render(request, 'articles/detail_article.html', context)


def new_post(request):
    tags = Tag.objects.all()
    if request.method == "POST":
        form = NewArticleForm(request.POST, request.FILES)
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.user = request.user
            new_article.save()
            return redirect('articles:articles')
        else:
            print(form.errors.as_data())
    context = {
        'tags': tags,
    }
    return render(request, 'articles/new_article.html', context)
