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
        widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter movie name'}),
        #     'language': forms.Select(attrs={'class': 'form-control'}),
        #     'director': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Director Name'}),
        #     'genre': forms.Select(attrs={'class': 'form-control'}),
        #     'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Year'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Movie description'}),
            # 'image': forms.ImageField()
        }

class Review_form(forms.ModelForm):
    class Meta:
        model=Review_model
        # fields=["comment","rating"]
        fields="__all__"
    
    
   