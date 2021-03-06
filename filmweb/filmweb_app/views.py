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


class AddActor(View):
    def get(self, request):
        return render(request, "add_actor.html")

    def post(self, request):
        name = request.POST.get("actor-name")
        year = request.POST.get("year_of_birth")
        gender = request.POST.get("gender")

        if not name:
            return render(request, "add_actor.html", context={"error": "Nie podano aktora!"})

        if not year:
            return render(request, "add_actor.html", context={"error": "Nie podano daty urodzin!"})

        if not gender:
            return render(request, "add_actor.html", context={"error": "Nie podano płci!"})

        if Actors.objects.filter(actor_name=name).first():
            return render(request, "add_actor.html", context={"error": "Podany aktor już istnieje w bazie danych"})

        Actors.objects.create(actor_name=name, year_of_birth=year, gender=gender)
        return redirect("actor-list")


class ActorListView(View):
    def get(self, request):
        actors = Actors.objects.all()
        return render(request, "actors.html", context={"actors": actors})


class DeleteMovieView(View):
    def get(self, request, id):
        movie = Movies.objects.get(id=id)
        movie.delete()
        return redirect("movie-list")


class DeleteActorView(View):
    def get(self, request, id):
        actor = Actors.objects.get(id=id)
        actor.delete()
        return redirect("actor-list")


class ModifyMovie(View):
    def get(self, request, id):
        movie = Movies.objects.get(id=id)
        return render(request, "modify_movie.html", context={"movie-name": movie})

    def post(self, request, id):
        movie = Movies.objects.get(id=id)
        name = request.POST.get("movie-name")
        director = request.POST.get("director")
        year = request.POST.get("year_of_production")
        rating = request.POST.get("rating")
        genre = request.POST.get("genre")

        if not name:
            return render(request, "modify_movie.html", context={"movie-name": movie,
                                                                 "error": "Nie podano nazwy filmu!"})

        if not director:
            return render(request, "modify_movie.html", context={"movie-name": movie,
                                                                 "error": "Nie podano reżysera!"})

        if not year:
            return render(request, "modify_movie.html", context={"movie-name": movie,
                                                                 "error": "Rok produkcji musi być dodatni!"})

        if name != movie.movie_name and Movies.objects.filter(movie_name=name).first():
            return render(request, "modify_movie.html", context={"movie-name": movie,
                                                                 "error": "Film o podanej nazwie juz istnieje!"})

        movie.movie_name = name
        movie.director = director
        movie.year_of_production = year
        movie.save()
        return redirect("movie-list")


class ModifyActor(View):
    def get(self, request, id):
        actor = Actors.objects.get(id=id)
        return render(request, "modify_actor.html", context={"actor-name": actor})

    def post(self, request, id):
        actor = Actors.objects.get(id=id)
        name = request.POST.get("actor-name")
        year = request.POST.get("year_of_birth")
        gender = request.POST.get("gender")

        if not name:
            return render(request, "modify_actor.html", context={"actor-name": name,
                                                                 "error": "Nie podano aktora!"})

        if not year:
            return render(request, "modify_actor.html", context={"actor-name": name,
                                                                 "error": "Nie podano daty urodzin!"})

        if not gender:
            return render(request, "modify_actor.html", context={"actor-name": name,
                                                                 "error": "Nie podano płci!"})

        if name != actor.actor_name and Actors.objects.filter(actor_name=name).first():
            return render(request, "modify_actor.html", context={"actor-name": name,
                                                                 "error": "Taki Aktor juz istnieje!"})

        actor.actor_name = name
        actor.year_of_birth = year
        actor.gender = gender
        actor.save()
        return redirect("actor-list")


class MovieDetails(View):
    def get(self, request, id):
        movie = Movies.objects.get(id=id)
        return render(request, "movie_details.html", context={"movie": movie})


class ActorDetails(View):
    def get(self, request, id):
        actor = Actors.objects.get(id=id)
        return render(request, "actor_details.html", context={"actor": actor})


class SearchViewMovie(View):
    def get(self, request):
        name = request.POST.get("movie-name")
        director = request.POST.get("director")
        year = request.POST.get("year_of_production")
        rating = request.POST.get("rating")
        genre = request.POST.get("genre")
        movies = Movies.objects.all()

        if director:
            movies = movies.filter(director=director)
        if year:
            movies = movies.filter(year_of_production=year)
        if name:
            movies.filter(movie_name__contains=name)
        if rating:
            movies = movies.filter(rating=rating)
        if genre:
            movies = movies.filter(genre=genre)

        return render(request, "movies.html", context={"movie": movies})


class SearchViewActor(View):
    def get(self, request):
        name = request.POST.get("actor-name")
        year = request.POST.get("year_of_birth")
        gender = request.POST.get("gender")
        actor = Actors.objects.all()

        if name:
            actor.filter(actor_name__contains=name)
        if year:
            actor = actor.filter(year_of_birth=year)
        if gender:
            actor = actor.filter(gender=gender)

        return render(request, "actors.html", context={"actor": actor})
