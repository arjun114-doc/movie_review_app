from django import forms
from . models import Movie_model,Review_model

class Review_user_form(forms.Form):
    username=forms.CharField(max_length=50)
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=20)
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())
    
class Movie_form(forms.ModelForm):
    class Meta:
        model=Movie_model
        fields="__all__"

class Review_form(forms.ModelForm):
    class Meta:
        model=Review_model
        # fields=["comment","rating"]
        fields="__all__"
    
    
   