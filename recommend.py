# Import the pickle library to load our binary brain files
import pickle
# Import pandas to handle the movie data table
import pandas as pd

# Define a function to load our assets
def load_engine():

    print("⏳ Loading the Recommendation Engine...")

    # Load movies list
    with open('models/movies_list.pkl', 'rb') as f:
        movies = pickle.load(f)

    # Load similarity matrix
    with open('models/similarity.pkl', 'rb') as f:
        similarity = pickle.load(f)

    return movies, similarity


# Function to find movie index
def find_movie_index(movie_title, movies_df):

    try:
        index = movies_df[movies_df['title'] == movie_title].index[0]
        return index

    except IndexError:
        return None


# --- MAIN PROGRAM ---
if __name__ == "__main__":

    # Load engine files
    movies_list, similarity_matrix = load_engine()

    # Change the movie here
    target = "Spectre"

    # Find the index
    idx = find_movie_index(target, movies_list)

    # Show result
    if idx is not None:
        print(f"✅ Found it! '{target}' is located at Index: {idx}")
    else:
        print(f"❌ Error: '{target}' was not found in our database.")