from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator 

class Movie_model(models.Model):
    
    LANGUAGE_CHOICES = (
        ('Malayalam','Malayalam'),
        ("Tamil","Tamil"),
        ("Kannada","Kannada"),
        ("Hindi","Hindi"),
        ('English',"English")
    )
    GENRE_CHOICES = (
        ('horror','horror'),
        ('action','action'),
        ('war','war'),
        ('apocalypse','apocalypse'),
        ('science fiction','science fiction'),
        ('mystery','mystery'),
        ('comedy','comedy')
    )
    
    movie_name=models.CharField(max_length=50)
    movie_language=models.CharField(max_length=100,choices=LANGUAGE_CHOICES)
    director=models.CharField(max_length=60)
    genre=models.CharField(max_length=100,choices=GENRE_CHOICES)
    release_date=models.DateField(null=True)
    
    def __str__(self):
        return self.movie_name
    
    
class Review_model(models.Model):
    reviewer=models.ForeignKey(User,on_delete=models.CASCADE)
    movie_name=models.ForeignKey(Movie_model,on_delete=models.CASCADE)
    comment=models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
