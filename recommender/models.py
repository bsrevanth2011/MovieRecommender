from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

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
    average_rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Rating(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return str(self.rating)


class Genre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.genre

