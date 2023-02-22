from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from articles.models import Article
from posts.models import Post
from .models import User
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from posts.utils import group_list


class Register(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }
        return render(request, 'accounts/register.html', context)

    def post(self, request, *args, **kwargs):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            cd = register_form.cleaned_data
            email, username, password = cd['email'], cd['username'], cd['password']
            User.objects.create_user(email=email, username=username, password=password)
            return redirect('accounts:login')
        else:
            pass


class Login(View):
    template_name = 'accounts/login.html'
    form_classes = LoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        login_form = self.form_classes()
        context = {
            'login_form': login_form,
        }
        return render(request, 'accounts/login.html', context)

    def post(self, request, *args, **kwargs):
        url = request.META.get("HTTP_REFERER")
        if request.method == "POST":
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                email = login_form.cleaned_data['email']
                password = login_form.cleaned_data['password']
                user = authenticate(request, email=email, password=password)
                if user:
                    login(request, user)
                    return redirect('home')
                else:
                    return redirect(url)


class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('accounts:login')


def follow_user(request):
    from_user = request.user
    to_user_id: int = request.GET.get('id', None)
    to_user = User.objects.get(id=to_user_id)
    from_user = User.objects.get(id=from_user.id)
    print('from : ', from_user, 'to : ', to_user)
    if from_user not in to_user.follower.all():
        from_user.c_following += 1
        to_user.c_follower += 1
        from_user.save()
        to_user.save()

        from_user.following.add(to_user)
        to_user.follower.add(from_user)

        response = {
            'type_operation': 'follow'
        }
    else:
        from_user.c_following -= 1
        to_user.c_follower -= 1
        from_user.save()
        to_user.save()

        from_user.following.remove(to_user)
        to_user.follower.remove(from_user)

        response = {
            'type_operation': 'unfollow'
        }
    return JsonResponse(response)


class Profile(View):
    def get(self, request, *args, **kwargs):
        current_user = request.user
        posts = Post.objects.filter(user=current_user)
        articles = Article.objects.filter(user=current_user)
        save_post = current_user.save_post.all()
        posts: list = group_list(list(posts), 3)
        articles: list = group_list(list(articles), 3)
        save_post: list = group_list(list(save_post), 3)
        return render(request, 'accounts/profile.html', {
            'posts': posts,
            'save_post': save_post,
            'articles': articles,
            'current_user':current_user
        })
