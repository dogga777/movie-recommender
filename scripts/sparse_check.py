# Import pandas for data loading
import pandas as pd

# Import the Vectorizer tool
from sklearn.feature_extraction.text import TfidfVectorizer

# Load our cleaned dataset
df = pd.read_csv('data/processed_movies.csv')

# Initialize the vectorizer
tfidf = TfidfVectorizer(stop_words='english')

# Transform the tags into a sparse matrix
tfidf_matrix = tfidf.fit_transform(df['tags'])

# --- SYSTEM INSPECTION ---

# 1. Check matrix type
print(f"Matrix Type: {type(tfidf_matrix)}")

# 2. Count non-zero entries
print(f"Number of non-zero entries: {tfidf_matrix.nnz}")

# 3. Calculate total possible cells
total_cells = tfidf_matrix.shape[0] * tfidf_matrix.shape[1]
print(f"Total possible cells: {total_cells}")

# 4. Calculate sparsity percentage
sparsity = (1 - tfidf_matrix.nnz / total_cells) * 100
print(f"Sparsity: {sparsity:.2f}% (This much of the matrix is empty zeros!)")