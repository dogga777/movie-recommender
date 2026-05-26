# Import pandas to read our cleaned data
import pandas as pd

# Import the Vectorizer from scikit-learn
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the processed dataset
df = pd.read_csv('data/processed_movies.csv')

# Step 1: Initialize the Vectorizer
tfidf = TfidfVectorizer(stop_words='english')

# Step 2: Convert text into TF-IDF weights
tfidf_matrix = tfidf.fit_transform(df['tags'])

# Step 3: Get the vocabulary
vocab = tfidf.get_feature_names_out()

# Print total vocabulary size
print(f"✅ Total unique words in vocabulary: {len(vocab)}")

# Print sample words
print("\n--- Sample of the Engine's Vocabulary ---")
print(vocab[1000:1010])

# Step 4: Print matrix dimensions
print(f"\n📊 Matrix Shape: {tfidf_matrix.shape}")