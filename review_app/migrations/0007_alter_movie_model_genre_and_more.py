# Generated by Django 5.1.4 on 2025-03-13 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review_app', '0006_alter_movie_model_movie_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_model',
            name='genre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='movie_model',
            name='movie_language',
            field=models.CharField(max_length=100),
        ),
    ]
