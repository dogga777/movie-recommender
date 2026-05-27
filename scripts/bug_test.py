import pandas as pd

# Dummy similarity scores
mock_scores = [(0, 99.9), (1, 0.98), (2, 0.5), (3, 0.05)]

print("--- Start Bug Test ---")

# LOGIC ERROR
broken_sort = sorted(mock_scores, key=lambda x: x[1])

print(f"Engine Suggestion: Movie Index {broken_sort[0][0]}")
print(f"Similarity Score: {broken_sort[0][1]}")

print("--- End Bug Test ---")