from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Movie vectors [Action, Comedy, Sci-Fi]

movie_pure_action = np.array([[10, 0, 0]])
movie_pure_comedy = np.array([[0, 10, 0]])
movie_mix = np.array([[10, 2, 0]])

# Similarity calculations
score_opposite = cosine_similarity(movie_pure_action, movie_pure_comedy)[0][0]
score_partial = cosine_similarity(movie_pure_action, movie_mix)[0][0]
score_identical = cosine_similarity(movie_pure_action, movie_pure_action)[0][0]

print("--- Similarity Scores ---")
print("Opposite:", score_opposite)
print("Partial:", score_partial)
print("Identical:", score_identical)