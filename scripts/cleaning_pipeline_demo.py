# Import pandas
import pandas as pd

# Mock raw movie data
raw_movie_row = {
    'title': 'Iron Man',

    'genres': '[{"name": "Action"}, {"name": "Sci-Fi"}]',

    'keywords': 'marvel superhero billionaire',

    'overview': 'After being held captive, Tony Stark builds a suit.',

    'cast': 'Robert Downey Jr.'
}

# Step 1: Clean genres
clean_genres = ['Action', 'Sci-Fi']

# Step 2: Convert overview to lowercase
overview_lower = raw_movie_row['overview'].lower()

# Step 3: Blend tags together
tags = f"{overview_lower} {' '.join(clean_genres)} {raw_movie_row['keywords']} {raw_movie_row['cast']}"

# Display results
print("--- Data Cleaning Pipeline Visualization ---")

print(f"RAW GENRES: {raw_movie_row['genres']}")

print(f"CLEANED GENRES: {clean_genres}")

print("-" * 30)

print("FINAL BLENDED TAGS FOR THE ENGINE:")

print(tags)