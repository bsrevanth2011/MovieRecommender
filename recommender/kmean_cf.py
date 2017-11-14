
# coding: utf-8

# In[52]:


import numpy as np
from . import models

MAX_ITERATIONS = 500


# In[53]:


def load_csv():
    no_of_users = models.User.objects.all().count()
    no_of_items = models.Movie.objects.all().count()
    ratings = np.zeros((no_of_users, no_of_items))
    for rating in models.Rating.objects.all():
        ratings[rating.user.id - 1, rating.movie.id - 1] = rating.rating
    return ratings


# In[54]:


def randomize_centroids(ratings, k=10):
    return ratings[np.random.choice(range(ratings.shape[0]), size = k, replace = False)]


# In[55]:


def assign_clusters(ratings, clusters, centroids, k = 10):
    cluster_indices = [[] for _ in range(k)]
    for i, user in enumerate(ratings):
        index = min([(j, np.linalg.norm(user - centroids[j])) for j, _ in enumerate(centroids)], key = (lambda t: t[1]))[0]
        clusters[index].append(user)
        cluster_indices[index].append(i)
    for cluster in clusters:
        if not cluster:
            rand_index = np.random.randint(0, ratings.shape[0])
            cluster.append(ratings[rand_index])
            cluster_indices.append(rand_index)
    return cluster_indices, clusters   


# In[56]:


def has_converged(centroids, old_centroids, iterations):
    if iterations >= MAX_ITERATIONS:
        return False
    return np.array_equal(centroids, old_centroids)


# In[57]:


def kmeans(ratings, k = 10):
    centroids = randomize_centroids(ratings, k)
    old_centroids = [[] for _ in range(k)]
    iterations = 0
    clusters = []
    cluster_indices = []
    while not has_converged(centroids, old_centroids, iterations):
        iterations += 1
        old_centroids = centroids.copy()
        clusters = [[] for _ in range(k)]
        cluster_indices, clusters = assign_clusters(ratings, clusters, centroids, k)
        for i in range(k):
            centroids[i] = np.mean(clusters[i], axis = 0)
    return clusters, cluster_indices


# In[58]:


def similarity(ratings):
    ratings += 1e-9
    user_sim = ratings.dot(ratings.T)
    norm = np.array(np.sqrt(np.diagonal(user_sim)))
    user_sim = user_sim / norm / norm.T
    return user_sim


def item_similarity(ratings):
    ratings += 1e-9
    item_sim = ratings.T.dot(ratings)
    norm = np.array([np.sqrt(np.diagonal(item_sim))])
    item_sim = item_sim / norm / norm.T
    return item_sim

# In[59]:


def predict_rating_user(ratings, similarity):
    return similarity.dot(ratings) / np.array([np.abs(similarity).sum(axis=1)]).T


def predict_rating_item(ratings, similarity):
    item_bias = ratings.mean(axis=0)
    ratings = (ratings - item_bias[np.newaxis, :]).copy()
    pred = ratings.dot(similarity) / np.array([np.abs(similarity).sum(axis=1)])
    pred += item_bias[np.newaxis, :]
    return pred


# In[60]:


def total_similarity(ratings, clusters, cluster_indices):
    sim = np.zeros((ratings.shape[0], ratings.shape[0]))
    for i in range(len(clusters)):
        cluster_similarity = similarity(np.asarray(clusters[i]))
        for j in range(np.asarray(clusters[i]).shape[0]):
            for k in range(np.asarray(clusters[i]).shape[0]):
                sim[cluster_indices[i][j], cluster_indices[i][k]] = cluster_similarity[j][k]
    return sim


# In[61]:


def kmeans_cf():
    ratings = load_csv()
    clusters, cluster_indices = kmeans(ratings, k=10)
    sim = total_similarity(ratings, clusters, cluster_indices)
    pred = predict_rating_user(ratings, sim)
    item_sim = item_similarity(ratings)
    pred_item = predict_rating_item(ratings, item_sim)
    return ratings, pred, pred_item

