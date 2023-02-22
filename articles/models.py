from django.db import models
from tags.models import Tag
from accounts.models import User
from SocialNetwork import settings


class Article(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Title'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Author',
        related_name='articles'
    )
    description = models.TextField(
        verbose_name='Description'
    )
    cover = models.ImageField(
        upload_to='article/',
        verbose_name='Cover Post'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created'
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated'
    )
    like = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        verbose_name='Like User',
        blank=True
    )
    count_like = models.PositiveIntegerField(
        default=0,
        verbose_name='Count Like'
    )

    def __str__(self) -> str:
        return self.title
