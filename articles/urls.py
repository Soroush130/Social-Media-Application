from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('articles/', views.list_article, name='articles'),
    path('detail_article/<int:article_id>/', views.detail_article, name='detail_article'),
    path('new_post/', views.new_post, name='new_post'),
]
