"""
URL configuration for movie_review_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from review_app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("add_movie/",views.Movie_view.as_view(),name="add_movie"),
    path("review/<int:pk>",views.Review_view.as_view(),name="add_review"),
    path("login/",views.Signin.as_view(),name="login"),
    
    path('filter/<str:cata>',views.Filter_movie.as_view(),name='filter'),
    path("",views.Review_user.as_view(),name="reviewer"),
    path("movie/",views.Movie_list.as_view(),name="list_movies"),
    path("profile/",views.Profiledetail.as_view(),name="profile"),
    path("delete_review/<int:pk>",views.Delete_comment.as_view(),name="commentdel"),
    path("signout/",views.Signout.as_view(),name="signout"),
    
    
    
    
    path("",include("review_app.urls"))
    
    
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
