# Generated by Django 5.1.4 on 2025-03-18 07:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review_app', '0012_remove_review_model_movie_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='review_model',
            name='movie_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='review_app.movie_model'),
            preserve_default=False,
        ),
    ]
