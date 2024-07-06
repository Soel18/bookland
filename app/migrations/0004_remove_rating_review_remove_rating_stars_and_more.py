# Generated by Django 4.0 on 2024-07-06 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_book_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='review',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='stars',
        ),
        migrations.AddField(
            model_name='rating',
            name='dislike',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='rating',
            name='like',
            field=models.BooleanField(default=False),
        ),
    ]
