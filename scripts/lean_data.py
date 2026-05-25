import pandas as pd

file_path = "data/movies_5000.csv"
df = pd.read_csv(file_path)

print("--- DIAGNOSTIC CHECK ---")
print("Columns:", df.columns)

df_lean = df[['City', 'State', 'Shape Reported']]

print("\n--- Data Slimming Operation ---")
print(f"Columns before: {len(df.columns)}")
print(f"Columns after: {len(df_lean.columns)}")

print(df_lean.head())

original_memory = df.memory_usage().sum() / 1024
lean_memory = df_lean.memory_usage().sum() / 1024

print("\nMemory Before:", original_memory)
print("Memory After:", lean_memory)