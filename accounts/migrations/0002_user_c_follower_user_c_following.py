# Generated by Django 4.1.4 on 2022-12-14 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='c_follower',
            field=models.PositiveIntegerField(default=0, verbose_name='Count Follower'),
        ),
        migrations.AddField(
            model_name='user',
            name='c_following',
            field=models.PositiveIntegerField(default=0, verbose_name='Count Following'),
        ),
    ]
