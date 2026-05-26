# Import pandas library
import pandas as pd

# Load the movie dataset
df = pd.read_csv('data/movies_5000.csv')

# Show original number of columns
print(f"Initial columns: {len(df.columns)}")

# List of unnecessary columns
dead_weight = [
    'budget', 'homepage', 'original_language', 'original_title',
    'popularity', 'production_companies', 'production_countries',
    'release_date', 'revenue', 'runtime', 'spoken_languages',
    'status', 'tagline', 'vote_average', 'vote_count'
]

# Drop unnecessary columns
df_slim = df.drop(columns=dead_weight)

# Show new number of columns
print(f"Columns after dropping dead weight: {len(df_slim.columns)}")

# Display remaining important columns
print("\n--- Essential Columns Remaining ---")
print(df_slim.columns.tolist())