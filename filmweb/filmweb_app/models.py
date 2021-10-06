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

    movie_name = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    year_of_production = models.IntegerField(null=True)
    rating = models.IntegerField(choices=CHOICES)
    genre = models.IntegerField(null=True)

class Actors(models.Model):
    GENDER_CHOISES = (
        (-1, "I DONT KNOW"),
        (0, "MAN"),
        (1, "WOMAN"),
    )
    actor_name = models.CharField(max_length=255)
    year_of_birth = models.DateField()
    gender = models.IntegerField(choices=GENDER_CHOISES)
    movies = models.ManyToManyField(Movies)

