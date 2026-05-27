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

# Choose a movie
user_input = "Iron Man"

# -------------------------------
# FIND THE MOVIE INDEX
# -------------------------------

# Locate the movie row number
movie_idx = movies_list[movies_list['title'] == user_input].index[0]

# -------------------------------
# ACCESS THE SIMILARITY ROW
# -------------------------------

# Get the row of scores
similarity_row = similarity_matrix[movie_idx]

# -------------------------------
# DISPLAY RESULTS
# -------------------------------

print(f"✅ Successfully accessed row for: {user_input}")

print(f"📊 Total scores in this row: {len(similarity_row)}")

print(f"🔢 Sample scores: {similarity_row[:10]}")