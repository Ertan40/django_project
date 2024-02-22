from django.shortcuts import render, redirect
from kinomania.movies.forms import MovieCreateForm, MovieEditForm
from kinomania.movies.models import Movie
# Create your views here.


def catalogue(request):
    movies = Movie.objects.all()
    # return render(request, "common/index.html", {"movies": movies})
    return render(request, "movies/catalogue.html", {"movies": movies})


def movies(request, id):
    movie = Movie.objects.get(pk=id)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/movies.html', context)
    # if movie:
    #     return render(request, 'common/index.html', context)
    # else:
    #     messages.warning(request, 'No such Movie found')
    #     return redirect('movies/movies.html')

def add_movie(request):
    if request.POST == "GET":
        form = MovieCreateForm()
    else:
        form = MovieCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("catalogue")

    context = {"form": form}
    return render(request, 'movies/add-movie.html', context)


def edit_movie(request, pk):
    movie = Movie.objects.filter(pk=pk).get()

    if request.method == "GET":
        form = MovieEditForm(instance=movie)
    else:
        form = MovieEditForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            # return redirect("catalogue")
            return redirect("movies", id=pk)

    context = {"form": form, "movie": movie}
    return render(request, "movies/edit-movie.html", context)

