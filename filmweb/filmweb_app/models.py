from django.db import models

# Create your models here.

class Movies(models.Model):
    CHOICES = (
        (0, ""),
        (1, "*"),
        (2, "**"),
        (3, "***"),
        (4, "****"),
        (5, "*****"),
    )

    GENRE_CHOICES = (
        (0, "Nie wiem"),
        (1, "Komedia"),
        (2, "Musical"),
        (3, "Familijny"),
        (4, "Film akcji"),
        (5, "Przygodowy"),
        (6, "Horror"),
    )
    movie_name = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    year_of_production = models.IntegerField(null=True)
    rating = models.IntegerField(choices=CHOICES)
    genre = models.IntegerField(choices=GENRE_CHOICES)

class Actors(models.Model):
    GENDER_CHOISES = (
        (-1, "Nie chcę podawać"),
        (0, "Mężczyzna"),
        (1, "Kobieta"),
    )
    actor_name = models.CharField(max_length=255)
    year_of_birth = models.DateField()
    gender = models.IntegerField(choices=GENDER_CHOISES)
    movies = models.ManyToManyField(Movies)

