from django.shortcuts import render, redirect
from tags.models import Tag
from .models import Post
from accounts.models import User
from .utils import group_list
from django.views import View
from django.http import JsonResponse
from .forms import NewPostForm
from comments.models import Comment
from comments.forms import CommentForm


class DetailPostView(View):
    def get(self, request, post_id, *args, **kwargs):

        try:
            post = Post.objects.get(id=post_id)
        except:
            return redirect('page_not_found')

        context = {
            'post': post,
        }
        return render(request, 'posts/detail_post.html', context)


class ExplorView(View):
    def get(self, request, *args, **kwargs):
        currrent_user = request.user
        posts = Post.objects.all()
        # posts = Post.objects.filter(tag__in=currrent_user.favorites_list.all()).exclude(user=currrent_user)
        posts: list = group_list(list(posts), 3)
        print(posts)
        context = {
            'posts': posts,
        }
        return render(request, 'posts/explor.html', context)


class LikePostView(View):
    def get(self, request, *args, **kwargs):
        current_user = request.user
        post_id = request.GET.get('post_id', None)
        post = Post.objects.get(id=post_id)
        if current_user not in post.like.all():
            post.count_like += 1
            post.save()
            post.like.add(current_user)
            response = {
                'is_like': 'like'
            }
            return JsonResponse(response)
        else:
            post.count_like -= 1
            post.save()
            post.like.remove(current_user)
            response = {
                'is_like': 'unlike'
            }
            return JsonResponse(response)


class SavePostView(View):
    def get(self, request, *args, **kwargs):
        current_user = request.user
        post_id = request.GET.get('post_id', None)
        post = Post.objects.get(id=post_id)

        if post not in current_user.save_post.all():
            current_user.count_save += 1
            current_user.save()
            current_user.save_post.add(post)
            response = {
                'is_save': 'save'
            }
            return JsonResponse(response)
        else:
            current_user.count_save -= 1
            current_user.save()
            current_user.save_post.remove(post)
            response = {
                'is_save': 'unsave'
            }
            return JsonResponse(response)


class NewPostView(View):
    def get(self, request, *args, **kwargs):
        form = NewPostForm()
        tags = Tag.objects.all()
        return render(request, 'posts/new_post.html', {'form': form, 'tags': tags})

    def post(self, request, *args, **kwargs):
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
        else:
            print(form.errors.as_data())
        return render(request, 'posts/new_post.html', {'form': form})


class CommentViwe(View):
    def post(self, request, id, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)