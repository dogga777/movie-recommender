# Import pandas to manage our movie table
import pandas as pd

# Define the file path
file_path = "data/movies_5000.csv"

# Load the dataset
df = pd.read_csv(file_path)

# --- TASK 1: THE NULL HUNT ---
# .isnull() finds missing values
# .sum() counts them column by column
null_report = df.isnull().sum()

print("--- Missing Data Report (Before Cleaning) ---")
print(null_report)

# --- TASK 2: VISUAL INSPECTION ---
# Dummy variable for debugging
check_point = "Open Variables View"

# --- TASK 3: CLEANING ---
# Remove rows where 'overview' is missing
# (Only works if your dataset has an 'overview' column)

if 'overview' in df.columns:
    df_cleaned = df.dropna(subset=['overview'])

    print("\n--- Missing Data Report (After Cleaning) ---")
    print(df_cleaned.isnull().sum())

    print(f"\nMovies removed due to missing descriptions: {len(df) - len(df_cleaned)}")

else:
    print("\n⚠️ Your dataset does NOT contain an 'overview' column.")
    print("You are currently using the UFO dataset instead of the TMDB movies dataset.")

    # Example cleaning for your current dataset
    df_cleaned = df.dropna()

    print("\n--- Missing Data Report (After Cleaning) ---")
    print(df_cleaned.isnull().sum())

    print(f"\nRows removed due to missing data: {len(df) - len(df_cleaned)}")