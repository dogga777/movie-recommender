# Import required libraries
import pickle
import pandas as pd

# -------------------------------
# LOAD THE ENGINE FILES
# -------------------------------

# Load movie list
with open('models/movies_list.pkl', 'rb') as f:
    movies_list = pickle.load(f)

# Load similarity matrix
with open('models/similarity.pkl', 'rb') as f:
    similarity_matrix = pickle.load(f)

# -------------------------------
# USER INPUT
# -------------------------------

user_input = "Iron Man"

# -------------------------------
# FIND MOVIE INDEX
# -------------------------------

movie_idx = movies_list[movies_list['title'] == user_input].index[0]

# -------------------------------
# ACCESS THE SIMILARITY ROW
# -------------------------------

similarity_row = similarity_matrix[movie_idx]

# -------------------------------
# ENUMERATION HACK
# -------------------------------

# Attach index numbers to scores
stapled_scores = list(enumerate(similarity_row))

# -------------------------------
# DISPLAY RESULTS
# -------------------------------

print("✅ Enumeration Complete!")

print("\n--- First 3 Stapled Pairs ---")

print(stapled_scores[:3])