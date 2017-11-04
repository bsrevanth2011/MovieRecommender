from recommender import models
from datetime import datetime
import pandas as pd


# adding users to the database
def add_users(csv_file='ml-100k/u.user'):
    with open(csv_file, mode='r') as f:
        for line in f.readlines():
            row = line.split('|')
            user = models.User(
                id=int(row[0]),
                age=int(row[1]),
                gender=row[2],
            )
            user.save()


def str_to_bool(bool_str):
    if bool_str == 'True':
        return True
    else:
        return False


# add movies to the database
def add_movies(csv_file='ml-100k/u.details'):
    with open(csv_file, mode='r') as f:
        for i, line in enumerate(f.readlines()):
            row = line.split('|')
            is_adult = False
            release_date = None
            popularity = None
            if not not row[0]:
                is_adult = str_to_bool(row[0])
            if not not row[6].replace('\n', ''):
                release_date = datetime.strptime(row[6].replace('\n', ''), '%Y-%m-%d').date()
            if not not row[3]:
                popularity = float(row[3])
            title = row[1]
            overview = row[2]
            poster_path = row[4]
            genre_ids = row[5]

            movie = models.Movie(
                id=i+1,
                adult=is_adult,
                title=title,
                overview=overview,
                popularity=popularity,
                poster_path=poster_path,
                genre_ids=genre_ids,
                release_date=release_date
            )
            movie.save()


# add ratings to the database
def add_ratings(csv_file='ml-100k/u.data'):
    names = ['user_id', 'movie_id', 'rating', 'timestamp']
    df = pd.read_csv(csv_file, sep='\t', names=names)
    for index, row in df.iterrows():
        print(index)
        user = models.User.objects.get(id=row['user_id'])
        movie = models.Movie.objects.get(id=row['movie_id'])
        rating = row['rating']
        models.Rating(user=user, movie=movie, rating=rating).save()

