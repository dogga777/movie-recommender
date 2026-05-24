# Import pandas
import pandas as pd

# Dataset path
file_path = "data/movies_5000.csv"

# Load CSV file
df = pd.read_csv(file_path)

# Success message
print("--- Movie Database Loaded Successfully ---")

# Print rows and columns
print(f"Total Rows: {df.shape[0]}")
print(f"Total Columns: {df.shape[1]}")

# Print column names
print("\nHere are the columns available:")
print(df.columns.tolist())

# Show first 3 rows safely
print("\nPeeking at the first 3 rows:")
print(df.head(3))

# Final message
print("\nDataset loaded successfully!")