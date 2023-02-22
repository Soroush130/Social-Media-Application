from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from SocialNetwork import settings
from tags.models import Tag
from posts.models import Post

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("The email must be set")

        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email=email,
            username=username,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="Email",
        unique=True
    )
    username = models.CharField(
        verbose_name="UserName",
        unique=True,
        max_length=255
    )
    first_name = models.CharField(
        verbose_name="First Name",
        max_length=255,
        blank=True,
        null=True
    )
    last_name = models.CharField(
        verbose_name="Last Name",
        max_length=255,
        blank=True,
        null=True
    )
    birth_date = models.DateField(
        verbose_name="Birth Date",
        blank=True,
        null=True
    )
    bio = models.TextField(
        verbose_name="Bio",
        blank=True,
        null=True
    )
    image_profile = models.ImageField(
        verbose_name="Image Profile",
        upload_to='images-profile',
        blank=True,
        null=True
    )
    favorites_list = models.ManyToManyField(
        Tag,
        verbose_name="Favorites List",
        blank=True,
        related_name='users'
    )
    save_post = models.ManyToManyField(
        Post,
        verbose_name='Save Post',
        blank=True,
        related_name='users'
    )
    follower = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        verbose_name="Follower",
        related_name='followers'
    )
    following = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        verbose_name="Following",
        related_name='followings'
    )
    c_follower = models.PositiveIntegerField(
        default=0,
        verbose_name="Count Follower"
    )
    c_following = models.PositiveIntegerField(
        default=0,
        verbose_name="Count Following"
    )
    count_save = models.PositiveIntegerField(
        default=0,
        verbose_name='Count Save'
    )
    is_active = models.BooleanField(
        verbose_name="Active",
        default=True
    )
    is_staff = models.BooleanField(
        verbose_name="Staff",
        default=False
    )
    is_superuser = models.BooleanField(
        verbose_name="Superuser",
        default=False
    )
    date_join = models.DateTimeField(
        verbose_name="Date Join",
        default=timezone.now
    )
    last_login = models.DateTimeField(
        verbose_name="Last Login",
        blank=True,
        null=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_admin(self) -> bool:
        return self.is_staff

    @property
    def count_follower(self) -> str:
        if self.c_follower < 1000:
            return f'{self.c_follower}'
        elif 999 < self.c_follower < 1000000:
            return f'{self.c_follower / 1000}K'
        else:
            return f'{self.c_follower / 1000000}M'
