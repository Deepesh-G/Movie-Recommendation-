import pandas as pd

def load_data(movies_path, ratings_path):
    ratings = pd.read_csv(ratings_path, encoding='latin1', sep='\t',
    names=['user_id', 'movie_id', 'rating', 'timestamp'])
    
    movies = pd.read_csv(movies_path, encoding='latin1', sep='|',
    names=['movie_id', 'title', 'release_date', 'video_release_date', 'IMDb_URL',
           'unknown', 'Action', 'Adventure', 'Animation', "Children's", 'Comedy', 'Crime',
           'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery',
           'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western'])
    return movies, ratings



def preprocess_movies(movies):
    # Genre columns start from column index 5
    genre_columns = ['unknown', 'Action', 'Adventure', 'Animation', "Children's", 'Comedy', 'Crime',
                     'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery',
                     'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

    # Create a new column 'genres' by joining genre names where the value is 1
    movies['genres'] = movies[genre_columns].apply(
        lambda row: '|'.join([genre for genre, val in row.items() if val == 1]),
        axis=1
    )
    
    return movies

