# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    adult = models.BooleanField(default=False)
    title = models.TextField(max_length=100)
    overview = models.TextField(max_length=500)
    popularity = models.FloatField(default=0.0)
    poster = models.TextField(max_length=50)
    release_date = models.DateField()


class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)


class Rating(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

