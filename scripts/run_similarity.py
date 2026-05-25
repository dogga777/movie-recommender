from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Movie vectors [Action, Sci-Fi, Adventure]

movie_a = np.array([[10, 10, 5]])
movie_b = np.array([[10, 8, 10]])
movie_c = np.array([[0, 0, 10]])
movie_d = np.array([[10, 10, 5]])

# Cosine similarity calculations
score_ab = cosine_similarity(movie_a, movie_b)[0][0]
score_ac = cosine_similarity(movie_a, movie_c)[0][0]
score_ad = cosine_similarity(movie_a, movie_d)[0][0]
print("\nIron Man vs Clone:", round(score_ad, 2))

print("--- Cosine Similarity Results ---")
print("Iron Man vs Avengers:", round(score_ab, 2))
print("Iron Man vs Finding Nemo:", round(score_ac, 2))

if score_ab > 0.8:
    print("\nGood recommendation match!")