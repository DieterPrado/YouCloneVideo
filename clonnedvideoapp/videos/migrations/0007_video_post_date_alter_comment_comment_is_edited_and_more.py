# Generated by Django 4.1 on 2022-09-16 00:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0006_alter_comment_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 16, 0, 0, 39, 412607, tzinfo=datetime.timezone.utc), verbose_name=datetime.datetime(2022, 9, 16, 0, 0, 39, 412607, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_is_edited',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_post_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 16, 0, 0, 39, 412607, tzinfo=datetime.timezone.utc), verbose_name=datetime.datetime(2022, 9, 16, 0, 0, 39, 412607, tzinfo=datetime.timezone.utc)),
        ),
    ]
