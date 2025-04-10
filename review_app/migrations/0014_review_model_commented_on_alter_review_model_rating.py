# Generated by Django 5.1.4 on 2025-03-19 03:15

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review_app', '0013_review_model_movie_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='review_model',
            name='commented_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review_model',
            name='rating',
            field=models.DecimalField(decimal_places=2, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
