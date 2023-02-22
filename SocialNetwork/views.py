from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from posts.models import Post
from django.db.models import Q


def header(request):
    return render(request, 'shared/Header.html', {})


def footer(request):
    return render(request, 'shared/Footer.html', {})


def page_not_found(request):
    return render(request, '404.html')


@login_required(login_url='accounts/login/')
def home_page(request):
    current_user = request.user

    posts = Post.objects.filter(user__in=current_user.following.all()).order_by('-created')

    context = {
        'posts': posts,
    }
    return render(request, 'home.html', context)
