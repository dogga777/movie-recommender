# Import pandas for data loading
import pandas as pd

# Import the text vectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Import cosine similarity calculator
from sklearn.metrics.pairwise import cosine_similarity

# Import time module
import time

# Load the cleaned dataset
df = pd.read_csv('data/processed_movies.csv')

# Initialize the vectorizer
tfidf = TfidfVectorizer(stop_words='english')

# Convert text into a sparse matrix
tfidf_matrix = tfidf.fit_transform(df['tags'])

# --- THE BIG CALCULATION ---

print("🚀 Starting the Big Calculation (Comparing 4,803 movies)...")

# Start timer
start = time.time()

# Calculate cosine similarity
similarity = cosine_similarity(tfidf_matrix)

# End timer
end = time.time()

# Print calculation time
print(f"✅ Finished! Calculation took {end - start:.2f} seconds.")

# Print matrix shape
print(f"📊 Similarity Matrix Shape: {similarity.shape}")