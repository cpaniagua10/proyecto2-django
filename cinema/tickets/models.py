from django.db import models

# Create your models here.

MOVIES = [
    ('1', 'movie-one'),
    ('2', 'movie-two'),
    ('3', 'movie-tree')]

class ticket(models.Model): 
    name = models.CharField(max_length=30)
    movie = models.CharField(max_length=9, choices=MOVIES)
