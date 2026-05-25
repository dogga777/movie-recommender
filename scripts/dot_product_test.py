import numpy as np

# Movie vectors: [Action, Sci-Fi, Comedy]

avengers = np.array([10, 9, 5])
iron_man = np.array([9, 10, 8])
the_notebook = np.array([0, 0, 20])

# Dot products (overlap score)
overlap_score_marvel = np.dot(avengers, iron_man)
overlap_score_romance = np.dot(avengers, the_notebook)

print("--- Dot Product Test ---")

print("Avengers vs Iron Man:", overlap_score_marvel)
print("Avengers vs The Notebook:", overlap_score_romance)

if overlap_score_marvel > overlap_score_romance:
    print("\nMarvel movies have stronger similarity!")