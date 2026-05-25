# Import pandas for our data table
import pandas as pd

# --- THE DRY STATION (Reusable Function) ---
def clean_column(dataframe, column_name):

    # Fill empty cells with "Unknown"
    dataframe[column_name] = dataframe[column_name].fillna("Unknown")

    # Print success message
    print(f"✨ Cleaned the {column_name} column!")

    # Return updated dataframe
    return dataframe


# --- THE PROCESS ---

# Load the movie dataset
df = pd.read_csv('data/tmdb_5000_movies.csv')

# Clean multiple columns using ONE reusable function
df = clean_column(df, 'overview')
df = clean_column(df, 'tagline')
df = clean_column(df, 'homepage')

# Action Item: Clean a fourth column
df = clean_column(df, 'original_language')

# Show results
print("\n--- Cleaning Complete ---")

print(df[['title', 'overview', 'tagline', 'original_language']].head())