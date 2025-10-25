from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def create_genre_matrix(movies):
    # Clean the genres column
    movies['genres'] = movies['genres'].fillna('').astype(str)
    movies['genres'] = movies['genres'].replace('', 'unknown')

    # TF-IDF vectorization
    vectorizer = TfidfVectorizer(token_pattern=r'[^|]+')
    genre_mat = vectorizer.fit_transform(movies['genres'])
    return genre_mat, vectorizer


def get_content_recommendations(movie_title, movies, genre_mat, top_n=5):
    # Find the movie index
    match = movies[movies['title'].str.lower() == movie_title.lower()]
    if match.empty:
        raise ValueError(f"Movie '{movie_title}' not found in dataset.")
    
    idx = match.index[0]
    sim_scores = cosine_similarity(genre_mat[idx], genre_mat).flatten()
    indices = sim_scores.argsort()[::-1][1:top_n+1]

    return movies.iloc[indices][['title', 'genres']]
