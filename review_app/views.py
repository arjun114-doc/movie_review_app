from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import  View
# Create your views here.
from . forms import Review_user_form,Movie_form,Review_form
from . models import User,Movie_model,Review_model

class Review_user(View):
    def get(self,request):
        form=Review_user_form
        return render(request,"reviewer.html",{"form":form})
    
    def post(self,request):
        form=Review_user_form(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return HttpResponse("created user")
        else:
            return HttpResponse("input details carefully")

class Movie_view(View):
    def get(self,request):
        genres=Movie_model.GENRE_CHOICES
        languages=Movie_model.LANGUAGE_CHOICES
        form=Movie_form
        return render(request,"movie_form.html",{"form":form,"genres":genres,"languages":languages})

    def post(self,request):
        form=Movie_form(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            Movie_model.objects.create(**form.cleaned_data)
            # return HttpResponse("movie added successfullyy")
            return redirect('list_movies')
        else:
            print(form.cleaned_data)
            return HttpResponse("not valid")

class Review_view(View):
    def get(self,request):
        form=Review_form
        return render(request,"review_form.html",{"form":form})
    def post(self,request):
        form=Review_form(request.POST)
        if form.is_valid():
            Review_model.objects.create(**form.cleaned_data)
            return HttpResponse("data added successfully")


class Movie_list(View):
    def get(self,request):
        movies=Movie_model.objects.all()
        return render(request,"movie_list.html",{"movies":movies})
    