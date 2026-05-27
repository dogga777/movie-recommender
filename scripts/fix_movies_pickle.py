import pandas as pd
import pickle

print("📂 Loading movie dataset...")

# Load your movie CSV
movies = pd.read_csv('data/tmdb_5000_movies.csv')

# Convert titles into normal Python strings
movies_list = movies['title'].astype(str).tolist()

# Save fixed pickle
with open('models/movies_list.pkl', 'wb') as f:
    pickle.dump(movies_list, f)

print("✅ Fixed movies_list.pkl created successfully!")