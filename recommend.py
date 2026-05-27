import pickle
import pandas as pd

# Load assets
def load_assets():
    with open('models/movies_list.pkl', 'rb') as f:
        movies = pickle.load(f)

    with open('models/similarity.pkl', 'rb') as f:
        sim = pickle.load(f)

    return movies, sim


# Recommendation function
def get_recommendations(movie_name, movies_list, sim_matrix):

    # Find movie index
    idx = movies_list.index(movie_name)

    # Similarity scores
    distances = sorted(
        list(enumerate(sim_matrix[idx])),
        reverse=True,
        key=lambda x: x[1]
    )

    top_matches = distances[1:11]

    print(f"\nSearching for high-match relatives of {movie_name}...\n")

    # LOOP TO DEBUG
    for match in top_matches:

        score = match[1]

        # 🔴 SET CONDITIONAL BREAKPOINT HERE
        movie_title = movies_list[match[0]]

        print(f"Checking: {movie_title} (Score: {score})")


# Main execution
if __name__ == "__main__":

    m_list, s_matrix = load_assets()

    get_recommendations("Iron Man", m_list, s_matrix)