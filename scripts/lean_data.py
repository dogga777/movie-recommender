import pandas as pd

df = pd.read_csv("data/tmdb_5000_movies.csv")

print("Before:", len(df.columns))

df_lean = df[['id', 'title', 'overview', 'genres', 'keywords']]

print("After:", len(df_lean.columns))

print(df_lean.head())

print("Memory:", df.memory_usage().sum() / 1024, "KB")