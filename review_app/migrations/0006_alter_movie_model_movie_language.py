# Generated by Django 5.1.4 on 2025-03-13 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review_app', '0005_remove_movie_model_release_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_model',
            name='movie_language',
            field=models.CharField(choices=[('Malayalam', 'Malayalam'), ('Tamil', 'Tamil'), ('Telugu', 'Telugu'), ('Kannada', 'Kannada'), ('Hindi', 'Hindi'), ('English', 'English')], max_length=100),
        ),
    ]
