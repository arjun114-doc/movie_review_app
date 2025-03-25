from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import  View
# Create your views here.
from . forms import Review_user_form,Movie_form,Review_form,Login_form
from . models import User,Movie_model,Review_model
from django.contrib.auth import authenticate,login,logout

class Review_user(View):
    def get(self,request):
        form=Review_user_form
        return render(request,"reviewer.html",{"form":form})
    
    def post(self,request):
        form=Review_user_form(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            # return HttpResponse("created user")
            return redirect('login')
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
    def get(self,request,*args, **kwargs):
        id=kwargs.get('pk')
        spec_movie=Movie_model.objects.get(id=id)
        related_cata=spec_movie.genre
        print(related_cata)
        related_movies=Movie_model.objects.filter(genre=related_cata)
        print(related_movies)
        
        reviews=Review_model.objects.filter( movie_id=id)
        print(spec_movie.movie_name)
        form=Review_form
        return render(request,"review_form.html",{"form":form,"spec_movie":spec_movie,"reviews":reviews,"related_movies":related_movies})
    def post(self,request,*args, **kwargs):
        id=kwargs.get('pk')
        spec_movie=Movie_model.objects.get(id=id)
        form=Review_form(request.POST)
        
        if form.is_valid():
            print(form.cleaned_data)
            reviewer=request.user
            print(reviewer)
            
            Review_model.objects.create(**form.cleaned_data,reviewer=request.user,movie_id=spec_movie)
            # return HttpResponse("data added successfully")
            return redirect("add_review",id)
        else:
            return HttpResponse("nooo")


class Movie_list(View):
    def get(self,request):
        movies=Movie_model.objects.all()
        genres=Movie_model.GENRE_CHOICES
        return render(request,"movie_list.html",{"movies":movies,"genres":genres})

class Signin(View):
    def get(self,request):
        form=Login_form
        return render(request,"login.html",{"form":form})
    def post(self,request):
        form=Login_form(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,password=password,username=username)
            if user:
                login(request,user)
                # return HttpResponse("login success")
                return redirect("list_movies")
            else:
                return HttpResponse("not")
class Filter_movie(View):
    def get(self,request,*args, **kwargs):
        catag=kwargs.get("cata")
        filtered_movies= Movie_model.objects.filter(genre=catag)
        genres=Movie_model.GENRE_CHOICES
        return render(request,'filter_movie.html',{'filtered_movies':filtered_movies,'genres':genres})

class Profiledetail(View):
    def get(self,request):
        data=request.user
        print(data.username)
        return render(request,"profile.html")
    
class Delete_comment(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        
        
        review_movie_id=Review_model.objects.get(id=id).movie_id.id
        review=Review_model.objects.get(id=id)
        if review.reviewer==request.user:
            review.delete()
            return redirect('add_review',review_movie_id)
            # return HttpResponse("deleted successfully")
        else:
            return HttpResponse("unable to delete")

class Signout(View):
    def get(self,request):
        logout(request)
        return redirect("login")

    
    