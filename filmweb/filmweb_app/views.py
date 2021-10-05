from django.shortcuts import render, redirect
from django.views import View
from .models import Movies, Actors


# Create your views here.

class AddMovie(View):
    def get(self, request):
        return render(request, "add_movie.html")

    def post(self, request):
        name = request.POST.get("movie-name")
        director = request.POST.get("director")
        year = request.POST.get("year_of_production")
        rating = request.POST.get("rating")
        genre = request.POST.get("genre")

        if not name:
            return render(request, "add_movie.html", context={"error": "Nie podano nazwy filmu!"})

        if not director:
            return render(request, "add_movie.html", context={"error": "Nie podano reżysera!"})

        if not year:
            return render(request, "add_movie.html", context={"error": "Rok produkcji musi być dodatni!"})

        if Movies.objects.filter(movie_name=name).first():
            return render(request, "add_movie.html", context={"error": "Film o podanej nazwie istnieje"})

        Movies.objects.create(movie_name=name, director=director, year_of_production=year, rating=rating, genre=genre)
        return redirect("movie-list")


class MovieListView(View):
    def get(self, request):
        movies = Movies.objects.all()
        return render(request, "movies.html", context={"movies": movies})
