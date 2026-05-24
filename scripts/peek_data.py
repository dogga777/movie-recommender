# Import the pandas library as 'pd'
import pandas as pd

# Define the path to our dataset
file_path = "data/movies_5000.csv"

# Load the CSV file into a DataFrame
df = pd.read_csv(file_path)

# --- THE PEEK ---
print("--- TASK 1: PEEKING AT THE TOP 5 ROWS ---")

# Show first 5 rows
print(df.head())

# --- THE DIAGNOSIS ---
print("\n--- TASK 2: TECHNICAL DATA SUMMARY ---")

# Show technical information
df.info()

# --- THE TAIL ---
print("\n--- TASK 3: PEEKING AT THE BOTTOM 2 ROWS ---")

# Show last 2 rows
print(df.tail(2))