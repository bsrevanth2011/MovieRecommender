from django.conf.urls import url
from . import views

app_name = 'recommender'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/', views.UserFormView.as_view(), name='register'),
    url(r'^login/', views.UserLogin.as_view(), name='login'),
    url(r'^logout/', views.user_logout, name='logout'),
    url(r'^user/search/', views.user_search, name='user_search'),
    url(r'^search/', views.search, name='search'),
    url(r'^user/(?P<movie_id>[0-9]+)/', views.user_movie_details, name='user_movie_detail'),
    url(r'^(?P<movie_id>[0-9]+)/', views.movie_details, name='movie_detail'),
    url(r'^user/', views.user, name='user'),
    url(r'^rating', views.rating, name='rating')
]
