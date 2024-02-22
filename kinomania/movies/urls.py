from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("catalogue/", views.catalogue, name="catalogue"),
    path("<int:id>/", views.movies, name='movies'), # http://127.0.0.1:8000/movies/5
    path("addmovie/", views.add_movie, name="add movie"),
    path("editmovie/<int:pk>", views.edit_movie, name="edit movie"),
]