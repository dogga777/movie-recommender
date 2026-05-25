import numpy as np

movie_a = np.array([1, 1])
movie_b = np.array([5, 5])
movie_c = np.array([5, 0])

def euclidean(v1, v2):
    return np.linalg.norm(v1 - v2)

def cosine(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

print("A vs B Euclidean:", euclidean(movie_a, movie_b))
print("A vs B Cosine:", cosine(movie_a, movie_b))

print("A vs C Euclidean:", euclidean(movie_a, movie_c))
print("A vs C Cosine:", cosine(movie_a, movie_c))