import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. LOAD DATASET
df = pd.read_csv(r"C:\Users\chand\OneDrive\Desktop\movie-recommender\data\tmdb_5000_movies.csv")

# 2. CLEAN DATA
df['overview'] = df['overview'].fillna('')

# 3. VECTORIZE
tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
tfidf_matrix = tfidf.fit_transform(df['overview'])

# 4. SIMILARITY MATRIX
sim_matrix = cosine_similarity(tfidf_matrix)

# 5. AUDIT FUNCTION
def run_audit(movie_a_title, movie_b_title):
    try:
        idx_a = df[df['title'] == movie_a_title].index[0]
        idx_b = df[df['title'] == movie_b_title].index[0]

        score = sim_matrix[idx_a][idx_b]

        print(f"\nAUDIT: {movie_a_title} vs {movie_b_title}")
        print(f"Score: {round(score, 4)}")

        if score > 0.1:
            print("PASS: Related movies detected")
        else:
            print("FAIL: No strong relationship")

    except IndexError:
        print("ERROR: Movie not found (check exact title)")

# 6. TEST CASES
print("\n--- FINAL SIMILARITY AUDIT ---")

run_audit("Iron Man", "The Avengers")
run_audit("Iron Man", "Finding Nemo")