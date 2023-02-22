from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('header', views.header, name="header"),
    path('footer', views.footer, name="footer"),
    #
    path('404/', views.page_not_found, name="page_not_found"),
    path('', views.home_page, name="home"),
    # apps
    path('accounts/', include("accounts.urls")),
    path('posts/', include("posts.urls")),
    path('articles/', include("articles.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
