# Generated by Django 4.1 on 2022-09-13 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='channel_author',
        ),
        migrations.AlterField(
            model_name='video',
            name='is_private',
            field=models.BooleanField(default=False, verbose_name='Is the video private?'),
        ),
    ]
