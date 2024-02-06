from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("movies", views.movie_view, name='movies'),
    path("addmovie/", views.add_movie, name="add movie"),
]