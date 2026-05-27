# Import pandas to help us look up the index of a movie
import pandas as pd

# Import pickle to load saved files
import pickle

# --- STEP 1: LOAD THE ASSETS ---

# Load movie list
with open('models/movies_list.pkl', 'rb') as f:
    movies = pickle.load(f)

# Load similarity matrix
with open('models/similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

# --- STEP 2: THE INDEX LOOKUP ---

# Change this movie name for testing
user_choice = "John Carter"

# Find the movie index
movie_index = movies[movies['title'] == user_choice].index[0]

print(f"✅ User selected: {user_choice}")
print(f"📍 Location in Warehouse (Index): {movie_index}")

# --- STEP 3: ACCESS THE SCORES ---

# Retrieve similarity scores
distances = similarity[movie_index]

print(f"📊 Number of scores retrieved: {len(distances)}")
print(f"🔢 First similarity score: {distances[0]}")

# --- STEP 4: SORTING PREVIEW ---

print("\nNext Step: We will sort these numbers to find the highest matches!")