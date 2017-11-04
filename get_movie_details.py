
# coding: utf-8

# In[1]:


import pandas as pd
import json, requests
import urllib
import time


# In[2]:


def read_data(filepath='ml-100k/u.item'):
    movie_titles = []
    with open(filepath, mode='r') as f:
        for line in f.readlines():
            movie_titles.append(line.split('|')[1])
    return movie_titles


# In[3]:


def get_movie_details(movie_titles):
    movie_details = []
    headers = {'Accept': 'application/json'}
    payload = {'api_key': '85f9170ef8852f18ef6500d621c5c7fc'}  
    for i, movie_title in enumerate(movie_titles):
        payload['query'] = movie_title.split('(')[0]
        try:
            response = requests.get('http://api.themoviedb.org/3/search/movie/', params = payload, headers = headers)    
            movie_details.append(json.loads(response.text)['results'][0])
        except:
            movie_details.append({key: None for key in movie_details[0]})
    pd.DataFrame(movie_details)[['adult', 'title', 'overview', 'popularity', 'poster_path', 'genre_ids']].to_csv('ml-100k/u.details', sep='|', index=False, header=False, encoding='utf-8')


# In[22]:


def download_posters(filepath='ml-100k/u.details'):
    names = ['adult', 'title', 'overview', 'popularity', 'poster_path', 'genre_ids', 'date']
    df = pd.read_csv(filepath, sep='|', names=names)
    poster_paths = df['poster_path']
    headers = {'Accept': 'application/json'}
    payload = {'api_key': '85f9170ef8852f18ef6500d621c5c7fc'} 
    response = requests.get("http://api.themoviedb.org/3/configuration", params=payload, headers=headers)
    response = json.loads(response.text)
    base_url = response['images']['base_url'] + 'w185'
    poster_paths = poster_paths[1260:]
    for index, poster_path in enumerate(poster_paths):
        if index % 100 == 99:
            time.sleep(100)
            print(index)
        if poster_path == poster_path:
            image_url = base_url + poster_path
            # print(image_url)
            with open('images/{}'.format(poster_path), 'wb') as f:
                resource = urllib.urlopen(image_url)
                f.write(resource.read())
                f.close()

