# Generated by Django 3.2.13 on 2022-10-27 10:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0003_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user_like',
            field=models.ManyToManyField(related_name='comment_like', to=settings.AUTH_USER_MODEL),
        ),
    ]