import numpy as np

# Movie vectors (features: [Action, Sci-Fi])

movie_a = np.array([1, 1])
movie_b = np.array([5, 5])
movie_c = np.array([1, 1.1])

# Euclidean Distance
def get_euclidean(v1, v2):
    return np.linalg.norm(v1 - v2)

# Cosine Similarity
def get_cosine(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

print("--- Distance vs Similarity ---")

print(f"A vs B - Euclidean Distance: {get_euclidean(movie_a, movie_b):.2f}")
print(f"A vs B - Cosine Similarity: {get_cosine(movie_a, movie_b):.2f}")

print(f"\nA vs C - Euclidean Distance: {get_euclidean(movie_a, movie_c):.2f}")
print(f"A vs C - Cosine Similarity: {get_cosine(movie_a, movie_c):.2f}")

print("\nConclusion: Cosine Similarity focuses on direction, not size.")