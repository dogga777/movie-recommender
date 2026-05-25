import pandas as pd
import ast
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def convert(obj):
    try:
        data = ast.literal_eval(obj)
        return " ".join([i['name'] for i in data])
    except:
        return ""

# LOAD DATASET
df = pd.read_csv(r"C:\Users\chand\OneDrive\Desktop\movie-recommender\data\tmdb_5000_movies.csv")

print("\nColumns loaded:")
print(df.columns)

# CLEAN
df['overview'] = df['overview'].fillna('')
df['genres'] = df['genres'].apply(convert)
df['keywords'] = df['keywords'].apply(convert)

# CREATE TAGS
df['tags'] = df['overview'] + " " + df['genres'] + " " + df['keywords']
df['tags'] = df['tags'].fillna('')

# VECTORIZE
tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
tfidf_matrix = tfidf.fit_transform(df['tags'])

# SIMILARITY
print("\nCalculating similarity matrix...")
similarity_matrix = cosine_similarity(tfidf_matrix)

print("\nDONE")
print("Shape:", similarity_matrix.shape)