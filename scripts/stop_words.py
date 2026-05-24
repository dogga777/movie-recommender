# Import the CountVectorizer tool from Scikit-Learn
from sklearn.feature_extraction.text import CountVectorizer

# Import pandas to help us compare the results
import pandas as pd

# Our sample movie descriptions
movie_plots = [
    "The movie is a space battle in a galaxy far away",
    "This is a fast car chase in the city",
    "A space explorer finds a new galaxy"
]

# STEP 1: Without removing stop-words
vec_noisy = CountVectorizer()
matrix_noisy = vec_noisy.fit_transform(movie_plots)

# STEP 2: Remove English stop-words
vec_clean = CountVectorizer(stop_words='english')
matrix_clean = vec_clean.fit_transform(movie_plots)

# STEP 3: Compare the results
print(f"Total words found WITH noise: {len(vec_noisy.get_feature_names_out())}")
print(f"Total words found WITHOUT noise: {len(vec_clean.get_feature_names_out())}")

print("\nWords ignored by the machine (Noise):")

# Find removed words
noise = set(vec_noisy.get_feature_names_out()) - set(vec_clean.get_feature_names_out())

# Print sorted noise words
print(sorted(list(noise)))

print("\nMeaningful 'Tags' remaining:")
print(vec_clean.get_feature_names_out())