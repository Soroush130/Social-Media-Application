from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('detail_post/<int:post_id>/', views.DetailPostView.as_view(), name='detail_post'),
    path('comment/<int:id>/', views.CommentViwe.as_view(), name='comment'),
    path('new_post/', views.NewPostView.as_view(), name='new_post'),
    path('explor/', views.ExplorView.as_view(), name="explor"),
    path('like_post/', views.LikePostView.as_view(), name="like_post"),
    path('save_post/', views.SavePostView.as_view(), name="save_post"),
]