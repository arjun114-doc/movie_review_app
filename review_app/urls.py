
from django.urls import path
from review_app import views




urlpatterns = [
    path("",views.Movie_list.as_view(),name="list_movies"),
    
]
