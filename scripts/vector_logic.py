# Import the specialized tool for turning text into numbers
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Create a small 'Mini-Dataset' to visualize the logic
mini_data = {
    'title': ['Iron Man', 'The Avengers', 'The Lion King'],
    'tags': [
        'superhero billionaire marvel tech',
        'superhero marvel aliens team',
        'lion king jungle animation prince'
    ]
}

# Load this into a DataFrame
df = pd.DataFrame(mini_data)

# Step 1: Initialize the Vectorizer
vectorizer = TfidfVectorizer()

# Step 2: Transform text into vectors
tfidf_matrix = vectorizer.fit_transform(df['tags'])

# Step 3: Show the vocabulary
print("--- Vocabulary (Word Directions) ---")
print(vectorizer.get_feature_names_out())

# Step 4: Show the matrix
print("\n--- The Vector Matrix ---")
print(tfidf_matrix.toarray())