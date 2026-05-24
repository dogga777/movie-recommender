# Import pandas
import pandas as pd

# Define dataset path
file_path = "data/movies_5000.csv"

# Load dataset
df = pd.read_csv(file_path)

# Select useful columns from YOUR UFO dataset
potential_features = [
    'City',
    'Shape Reported',
    'State',
    'Time',
    'Colors Reported'
]

# Create smaller dataframe
ufo_data = df[potential_features]

# Print selected features
print("--- Selected Features for Analysis ---")
print(ufo_data.head())

# Efficiency comparison
print("\n--- Efficiency Check ---")
print(f"Original Column Count: {df.shape[1]}")
print(f"Feature Column Count: {ufo_data.shape[1]}")