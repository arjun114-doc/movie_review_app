# Generated by Django 5.1.4 on 2025-03-13 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review_app', '0004_movie_model_release_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie_model',
            name='release_date',
        ),
        migrations.AddField(
            model_name='movie_model',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='movie_model',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='movie_model',
            name='year',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
