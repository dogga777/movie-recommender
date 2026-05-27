# Import the libraries we need
import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Load the processed dataset
print("📂 Loading clean data...")

df = pd.read_csv('data/processed_movies.csv')

# 2. Vectorization
tfidf = TfidfVectorizer(stop_words='english')

tfidf_matrix = tfidf.fit_transform(df['tags'])

# 3. Similarity Calculation
print("🧠 Calculating similarity scores...")

similarity = cosine_similarity(tfidf_matrix)

# 4. Save the movie list
print("💾 Saving movie list...")

with open('models/movies_list.pkl', 'wb') as f:
    pickle.dump(df, f)

# 5. Save the similarity matrix
print("💾 Saving similarity matrix... this may take a moment.")

with open('models/similarity.pkl', 'wb') as f:
    pickle.dump(similarity, f)

# Final success message
print("✨ Done! Your engine is now saved in the models folder.")