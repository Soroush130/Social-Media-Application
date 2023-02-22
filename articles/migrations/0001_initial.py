# Generated by Django 4.1.4 on 2022-12-16 00:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('count_like', models.PositiveIntegerField(default=0, verbose_name='Count Like')),
                ('like', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Like User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
        ),
    ]