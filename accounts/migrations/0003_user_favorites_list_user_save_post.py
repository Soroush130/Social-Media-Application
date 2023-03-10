# Generated by Django 4.1.4 on 2022-12-16 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_count_save'),
        ('tags', '0001_initial'),
        ('accounts', '0002_user_c_follower_user_c_following'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorites_list',
            field=models.ManyToManyField(blank=True, related_name='users', to='tags.tag', verbose_name='Favorites List'),
        ),
        migrations.AddField(
            model_name='user',
            name='save_post',
            field=models.ManyToManyField(blank=True, related_name='users', to='posts.post', verbose_name='Save Post'),
        ),
    ]
