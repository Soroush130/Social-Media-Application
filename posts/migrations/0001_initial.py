# Generated by Django 4.1.4 on 2022-12-16 00:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='posts/', verbose_name='File')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('count_like', models.PositiveIntegerField(default=0, verbose_name='Count Like')),
                ('like', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='User Like')),
                ('tag', models.ManyToManyField(blank=True, related_name='posts', to='tags.tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
