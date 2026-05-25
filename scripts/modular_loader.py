# Import pandas library
import pandas as pd

# Function 1: Load and clean the data
def load_and_clean_data():

    # Define dataset path
    file_path = 'data/tmdb_5000_movies.csv'

    # Read CSV file
    df = pd.read_csv(file_path)

    # Replace missing values in overview column
    df['overview'] = df['overview'].fillna('')

    # Success message
    print("✅ Success: Data loaded and Nulls handled!")

    # Return cleaned dataframe
    return df


# Function 2: Show total number of movies
def show_movie_count(data):

    # Print total rows
    print("🎬 Total Movies:", len(data))


# --- EXECUTION SECTION ---

print("Starting the program...")

# Call the loading function
movie_data = load_and_clean_data()

# Call the movie count function
show_movie_count(movie_data)

# Show first 5 rows
print(movie_data.head())