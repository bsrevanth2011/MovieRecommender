# -*- coding:
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegisterForm, UserLoginForm
from django.views.generic import View
from .models import Movie, UserInfo, Rating, Genre
import numpy as np
from recommender.kmean_cf import item_similarity, predict_rating_item, similarity, predict_rating_user
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    movies = Movie.objects.all()

    return render(request, 'recommender/index.html', {'movies': movies})


@login_required
def user(request):
    user = request.user.userinfo_set.all()[0]
    movies = Movie.objects.all()
    users = UserInfo.objects.all()
    ratings = np.zeros((len(users), len(movies)))

    for rating in Rating.objects.all():
        ratings[rating.user.id - 1, rating.movie.id - 1] = rating.rating

    sim = similarity(ratings)

    pred = predict_rating_user(ratings, sim)
    indices = np.argsort(pred[user.id - 1, :])[:-11:-1] + 1

    recommended_movies = [Movie.objects.get(id=i) for i in indices]
    popular_movies = Movie.objects.order_by('-popularity')[:10]
    latest_movies = Movie.objects.order_by('-release_date')[:10]
    context = {
        'recommended_movies': recommended_movies,
        'popular_movies': popular_movies,
        'latest_movies': latest_movies
    }
    return render(request, 'recommender/user.html', context)


def rating(request):
    movie = Movie.objects.get(id=request.GET['movie_id'])
    user = request.user.userinfo_set.all()[0]
    try:
        Rating.objects.get(movie=movie, user=user).delete()
    except Rating.DoesNotExist:
        pass
    rating = Rating(user=user, movie=movie, rating=request.GET['rating'])
    rating.save()
    return HttpResponse("rating modified")


@login_required
def user_movie_details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    genres = Genre.objects.filter(movie=movie)
    movies = Movie.objects.all()
    users = UserInfo.objects.all()
    user = request.user
    user = user.userinfo_set.all()[0]
    try:
        user_rating = Rating.objects.get(movie=movie, user=user)
    except:
        user_rating = 0
    ratings = np.zeros((len(users), len(movies)))

    for rating in Rating.objects.all():
        ratings[rating.user.id - 1, rating.movie.id - 1] = rating.rating

    item_sim = item_similarity(ratings)
    count = np.sum(item_sim == 1)
    np.place(item_sim, item_sim == 1, np.zeros(count))

    indices = np.argsort(item_sim[int(movie_id) - 1, :])[:-12:-1] + 1
    recommended_movies = [Movie.objects.get(id=i) for i in indices if i != movie.id][:10]

    context = {
        'movie': movie,
        'recommended_movies': recommended_movies,
        'genres': genres,
        'rating': user_rating
    }

    return render(request, 'recommender/user_movie_details.html', context=context)


def movie_details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    genres = Genre.objects.filter(movie=movie)
    movies = Movie.objects.all()
    users = UserInfo.objects.all()
    ratings = np.zeros((len(users), len(movies)))

    for rating in Rating.objects.all():
        ratings[rating.user.id - 1, rating.movie.id - 1] = rating.rating

    item_sim = item_similarity(ratings)
    count = np.sum(item_sim == 1)
    np.place(item_sim, item_sim == 1, np.zeros(count))
    indices = np.argsort(item_sim[int(movie_id) - 1, :])[:-7:-1] + 1
    recommended_movies = [Movie.objects.get(id=i) for i in indices if i != movie.id][:5]

    context = {
        'movie': movie,
        'recommended_movies': recommended_movies,
        'genres': genres
    }

    return render(request, 'recommender/movie_details.html', context=context)


def user_details(request, user_id):
    user = UserInfo.objects.get(user_id)
    movies = Movie.objects.all()
    users = UserInfo.objects.all()
    ratings = np.zeros((len(users), len(movies)))
    for i in range(len(users)):
        for j in range(len(movies)):
            ratings[i, j] = Rating.objects.get(user=users[i], movie=movies[j]).rating


def user_logout(request):
    logout(request)
    return redirect('recommender:index')


class UserFormView(View):
    form_class = UserRegisterForm
    template_name = 'recommender/user_registration.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            userinfo = UserInfo.objects.create(user=user)
            userinfo.id = UserInfo.objects.count() + 1

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('recommender:user')

        return render(request, self.template_name, {'form': form})


class UserLogin(View):
    form_class = UserLoginForm
    template_name = 'recommender/user_login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('recommender:user')

        return render(request, self.template_name, {'form': form})


def search(request):
    query_string = request.POST['search']
    try:
        movies = Movie.objects.filter(title__icontains=query_string)
    except Movie.DoesNotExist:
        movies = []
    return render(request, 'recommender/search.html', {'movies': movies})


def user_search(request):
    query_string = request.POST['search']
    try:
        movies = Movie.objects.filter(title__icontains=query_string)
    except Movie.DoesNotExist:
        movies = []
    return render(request, 'recommender/user_search.html', {'movies': movies})