import pickle
import pandas as pd

# LOAD THE ENGINE FILES
with open('models/movies_list.pkl', 'rb') as f:
    movies_list = pickle.load(f)

with open('models/similarity.pkl', 'rb') as f:
    similarity_matrix = pickle.load(f)

# USER INPUT
user_input = "Avatar"

# FIND THE MOVIE INDEX
movie_idx = movies_list[movies_list['title'] == user_input].index[0]

# ACCESS THE SIMILARITY ROW
similarity_row = similarity_matrix[movie_idx]

# ENUMERATION HACK
stapled_scores = list(enumerate(similarity_row))

# SORT THE SCORES (Highest First)
sorted_matches = sorted(
    stapled_scores,
    reverse=True,
    key=lambda x: x[1]
)

# PRINT FIRST 3 RESULTS
print("🎬 Top 3 Sorted Matches:")
print(sorted_matches[:3])