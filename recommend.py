# Import the necessary libraries
import pickle
import pandas as pd

# Function to load our pre-calculated brain
def load_assets():

    # Load the movie list dataframe
    with open('models/movies_list.pkl', 'rb') as f:
        movies = pickle.load(f)

    # Load the similarity scores matrix
    with open('models/similarity.pkl', 'rb') as f:
        sim = pickle.load(f)

    return movies, sim


# The core recommendation engine function
def get_recommendations(movie_name, movies_df, sim_matrix):

    try:
        # Step 1: Find movie index
        idx = movies_df[movies_df['title'] == movie_name].index[0]

        # Step 2: Enumerate similarity scores
        score_series = list(enumerate(sim_matrix[idx]))

        # Step 3: Sort scores
        sorted_scores = sorted(
            score_series,
            reverse=True,
            key=lambda x: x[1]
        )

        # Step 4: Get top 5 matches
        top_matches = sorted_scores[1:6]

        # Step 5: Display recommendations
        print(f"\n🎬 Recommendations for '{movie_name}':")
        print("-" * 40)

        for match in top_matches:
            print(f"✨ {movies_df.iloc[match[0]].title}")

        print("-" * 40)

    except IndexError:
        print(f"\n❌ Error: '{movie_name}' not found.")


# MAIN PROGRAM
if __name__ == "__main__":

    # Load assets
    m_list, s_matrix = load_assets()

    # Test recommendation
    get_recommendations("The Dark Knight", m_list, s_matrix)