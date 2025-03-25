from django.contrib import admin

# Register your models here.
from . models import Movie_model,Review_model

admin.site.register(Movie_model)
admin.site.register(Review_model)