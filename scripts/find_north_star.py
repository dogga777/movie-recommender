import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load dataset
df = pd.read_csv('data/tmdb_5000_movies.csv')

# Clean missing values
df['overview'] = df['overview'].fillna('')

# Create TF-IDF matrix
tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
tfidf_matrix = tfidf.fit_transform(df['overview'])

# Choose North Star
target_movie = "The Avengers"

try:
    movie_index = df[df['title'] == target_movie].index[0]

    vector = tfidf_matrix[movie_index]

    print("--- North Star Found ---")
    print("Movie:", target_movie)
    print("Index:", movie_index)
    print("Vector shape:", vector.shape)

except IndexError:
    print("Movie not found. Try Avatar / Iron Man / The Avengers")