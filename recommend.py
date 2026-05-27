# Import the pickle library to load saved files
import pickle

# Import pandas
import pandas as pd

# Function to load the recommendation engine
def load_engine():

    print("⏳ Loading the Recommendation Engine...")

    # Load movie list
    with open('models/movies_list.pkl', 'rb') as f:
        movies = pickle.load(f)

    # Load similarity matrix
    with open('models/similarity.pkl', 'rb') as f:
        similarity = pickle.load(f)

    return movies, similarity


# Main program
if __name__ == "__main__":

    movies_list, similarity_matrix = load_engine()

    print(f"✅ Engine Ready! Loaded {len(movies_list)} movies.")

    print("\n--- Preview of Movie Library ---")

    print(movies_list['title'].head())