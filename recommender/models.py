# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    adult = models.BooleanField(default=False)
    title = models.TextField(max_length=100, null=True, blank=True)
    overview = models.TextField(max_length=500, null=True, blank=True)
    popularity = models.FloatField(default=0.0, null=True, blank=True)
    poster_path = models.TextField(max_length=50, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    genre_ids = models.TextField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=1, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return str(self.rating)

