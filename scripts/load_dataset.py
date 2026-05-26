# Import pandas library
import pandas as pd

# Dataset path
file_path = 'data/movies_5000.csv'

# Safety net for loading the dataset
try:
    # Load CSV file
    movies_df = pd.read_csv(file_path)

    # Success message
    print("✅ Dataset loaded successfully!")

    # Show dataset shape
    print(f"📊 Dataset Dimensions: {movies_df.shape}")

    # Show all columns
    print(f"📋 Columns found: {list(movies_df.columns)}")

    # Preview first 3 rows
    print("\n--- Quick Peek at Data ---")

    print(movies_df[['title', 'genres', 'vote_average']].head(3))

# Handle missing file error
except FileNotFoundError:
    print("❌ ERROR: Could not find 'movies_5000.csv' in the 'data' folder.")
    