from django.shortcuts import render
from kinomania.movies.forms import MovieCreateForm
from kinomania.movies.models import Movie
# Create your views here.


def index(request):
    movies = Movie.objects.all()
    return render(request, "common/index.html", {"movies": movies})


def movies(request, id):
    movies = Movie.objects.get(movie=id)
    context = {"movies": movies}
    return render(request, "movies/movies.html", context)


def movie_view(request, id):
    movies = Movie.objects.filter(movie=id)
    context = {
        'movies': movies,
    }

    if movies:
        return render(request, 'common/index.html', context)
    else:
        messages.warning(request, 'No such Movie found')
        return redirect('movies/movies.html')

def add_movie(request):
    if request.POST == "GET":
        form = MovieCreateForm()
    else:
        form = MovieCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("movie list")
    context = {"form": form}
    return render(request, 'movies/add-movie.html', context)