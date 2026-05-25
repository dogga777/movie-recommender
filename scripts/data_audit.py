import pandas as pd
import os

file_path = "data/tmdb_5000_movies.csv"

def run_audit():
    print("DATA AUDIT START\n")

    if not os.path.exists(file_path):
        print("FILE NOT FOUND")
        return

    df = pd.read_csv(file_path)

    print("Columns:", df.columns)

    required = ['id', 'title', 'overview', 'genres', 'keywords']
    missing = [col for col in required if col not in df.columns]

    if not missing:
        print("ALL REQUIRED COLUMNS PRESENT")
    else:
        print("Missing:", missing)

    nulls = df['overview'].isnull().sum()
    print("Missing overviews:", nulls)

    print("\nAUDIT COMPLETE")

run_audit()