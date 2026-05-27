import pandas as pd
import ast

# Load datasets
movies = pd.read_csv(
    'data/tmdb_5000_movies.csv',
    engine='python'
)
credits = pd.read_csv(
    'data/tmdb_5000_credits.csv',
    engine='python'
)

print("✅ Datasets loaded")

# Merge datasets
movies = movies.merge(credits, on='title')

print("✅ Datasets merged")

# Keep important columns
movies = movies[['movie_id',
                 'title',
                 'overview',
                 'genres',
                 'keywords',
                 'cast',
                 'crew']]

print("✅ Important columns selected")

# Remove missing data
movies.dropna(inplace=True)

print("✅ Missing values removed")


# -----------------------------
# FUNCTION 1
# Extract names from dictionaries
# -----------------------------
def convert(text):
    result = []

    for i in ast.literal_eval(text):
        result.append(i['name'])

    return result


# Clean genres and keywords
movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)

print("✅ Genres & keywords cleaned")


# -----------------------------
# FUNCTION 2
# Extract top 3 actors
# -----------------------------
def convert_cast(text):
    result = []
    counter = 0

    for i in ast.literal_eval(text):
        if counter != 3:
            result.append(i['name'])
            counter += 1
        else:
            break

    return result


movies['cast'] = movies['cast'].apply(convert_cast)

print("✅ Cast cleaned")


# -----------------------------
# FUNCTION 3
# Extract director
# -----------------------------
def fetch_director(text):
    result = []

    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            result.append(i['name'])
            break

    return result


movies['crew'] = movies['crew'].apply(fetch_director)

print("✅ Director extracted")


# Split overview into words
movies['overview'] = movies['overview'].apply(lambda x: x.split())

print("✅ Overview cleaned")


# -----------------------------
# FUNCTION 4
# Remove spaces
# -----------------------------
def collapse(text):
    result = []

    for i in text:
        result.append(i.replace(" ", ""))

    return result


movies['genres'] = movies['genres'].apply(collapse)
movies['keywords'] = movies['keywords'].apply(collapse)
movies['cast'] = movies['cast'].apply(collapse)
movies['crew'] = movies['crew'].apply(collapse)

print("✅ Spaces removed")


# Create tags column
movies['tags'] = movies['overview'] + \
                 movies['genres'] + \
                 movies['keywords'] + \
                 movies['cast'] + \
                 movies['crew']

print("✅ Tags column created")


# Final dataframe
new_df = movies[['movie_id', 'title', 'tags']]


# Convert list into string
new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))


# Convert lowercase
new_df['tags'] = new_df['tags'].apply(lambda x: x.lower())

print("✅ Lowercase conversion complete")


# Save processed dataset
new_df.to_csv('data/processed_movies.csv', index=False)

print("🎉 FULL DATASET READY")
print(f"✅ Total Movies Processed: {len(new_df)}")