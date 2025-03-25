from django.db import models

# Create your models here.

from django.contrib.auth.models import User

from django.core.validators import MinValueValidator, MaxValueValidator 

class Movie_model(models.Model):
    
    LANGUAGE_CHOICES = (
        ('Malayalam','Malayalam'),
        ("Tamil","Tamil"),
        ("Telugu","Telugu"),
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
    
    movie_name=models.CharField(max_length=50,name="movie_name")
    movie_language=models.CharField(max_length=100,name="movie_language")
    director=models.CharField(max_length=60,name="director")
    genre=models.CharField(max_length=100,name="genre")
    # release_date=models.DateField(null=True)
    year=models.CharField(max_length=4,null=True,name="year")
    image=models.ImageField(null=True,name='image',blank=False)
    description=models.TextField(null=True,name="description")
    
    
    def __str__(self):
        return self.movie_name
    
    
class Review_model(models.Model):
    reviewer=models.ForeignKey(User,on_delete=models.CASCADE)
    
    movie_id=models.ForeignKey(Movie_model, on_delete=models.CASCADE)
    commented_on=models.DateTimeField(auto_now_add=True)
    comment=models.TextField(name="comment")
    rating = models.DecimalField(max_digits=4,decimal_places=2,validators=[MinValueValidator(0), MaxValueValidator(10)],name='rating')
    
