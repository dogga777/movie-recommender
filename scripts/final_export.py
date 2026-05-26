# Import the pandas library to save our data
import pandas as pd

# Mock data representing our final cleaned dataset
data = {
    'movie_id': [19995, 285],
    'title': ['Avatar', 'Pirates of the Caribbean'],
    'tags': [
        'action adventure fantasy marine soldier alien',
        'adventure fantasy ocean captain pirate'
    ]
}

# Create a DataFrame
df_clean = pd.DataFrame(data)

# Define where to save the clean dataset
export_path = 'data/processed_movies.csv'

# Export the clean file
df_clean.to_csv(export_path, index=False)

# Success message
print(f"✅ Success! Your clean data has been saved to: {export_path}")

# Reload the file to verify export
test_load = pd.read_csv(export_path)

print("\n--- Verifying Exported File ---")
print(test_load.head())