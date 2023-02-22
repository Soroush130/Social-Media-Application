from django.db import models
from tags.models import Tag
from SocialNetwork import settings


class Post(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='User'
    )
    img = models.ImageField(
        upload_to='posts/',
        verbose_name='File'
    )
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(
        auto_now_add=True
    )
    tag = models.ManyToManyField(
        Tag,
        related_name='posts',
        blank=True
    )
    like = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        verbose_name='User Like',
        blank=True
    )
    count_like = models.PositiveIntegerField(
        default=0,
        verbose_name='Count Like'
    )

    def __str__(self) -> str:
        return f'{self.user.email} ==> {self.id}'


