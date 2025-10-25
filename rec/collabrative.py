import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def build_user_movie_matrix(ratings):
    return ratings.pivot(index='user_id', columns='movie_id', values='rating').fillna(0)


def get_collaborative_recommendations(user_id, ratings, top_n=5):
    user_movie_matrix = build_user_movie_matrix(ratings)
    user_similarities = cosine_similarity(user_movie_matrix)

    if user_id not in user_movie_matrix.index:
        raise ValueError(f"User ID {user_id} not found in ratings data.")

    user_idx = user_movie_matrix.index.get_loc(user_id)
    sim_scores = list(enumerate(user_similarities[user_idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]

    similar_users = [user_movie_matrix.index[i[0]] for i in sim_scores]
    recommendations = ratings[ratings['user_id'].isin(similar_users)]

    return recommendations.groupby('movie_id').rating.mean().sort_values(ascending=False).head(top_n)
