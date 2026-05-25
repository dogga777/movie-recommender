import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# STEP 1: Load dataset
df = pd.read_csv(r"C:\Users\chand\OneDrive\Desktop\movie-recommender\data\tmdb_5000_movies.csv")

print("\n--- Dataset Loaded ---")
print("Shape:", df.shape)

# STEP 2: Safe cleaning
df['overview'] = df['overview'].fillna('')

# STEP 3: Create high-dimensional vectors (5000 features)
tfidf = TfidfVectorizer(
    stop_words='english',
    max_features=8000,
    ngram_range=(1,2)   # IMPORTANT UPGRADE
)
tfidf_matrix = tfidf.fit_transform(df['overview'])

print("\n--- TF-IDF MATRIX CREATED ---")
print("Shape:", tfidf_matrix.shape)

# STEP 4: Cosine similarity matrix
print("\nCalculating similarity matrix... (wait a few seconds)")
sim_matrix = cosine_similarity(tfidf_matrix)

print("\n--- SIMILARITY MATRIX READY ---")
print("Shape:", sim_matrix.shape)

# STEP 5: Show sample values (important for your task)
print("\nSample values:")
print("Row 0, Col 1:", sim_matrix[0][1])
print("Row 0, Col 2:", sim_matrix[0][2])
print("Row 1, Col 2:", sim_matrix[1][2])
print("\n--- STATISTICS ---")
print("Max similarity:", sim_matrix.max())
print("Min similarity:", sim_matrix.min())
print("Average similarity:", sim_matrix.mean())