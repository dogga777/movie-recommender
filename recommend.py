import pickle

# Optimized loader
def load_assets():

    with open('models/movies_list.pkl', 'rb') as f_list, \
         open('models/similarity.pkl', 'rb') as f_sim:

        return pickle.load(f_list), pickle.load(f_sim)


# Refactored recommendation function
def get_recommendations(movie_name, movies_list, sim_matrix):

    try:
        # Find movie index
        idx = movies_list.index(movie_name)

        # Optimized similarity sorting
        distances = sorted(
            list(enumerate(sim_matrix[idx])),
            reverse=True,
            key=lambda x: x[1]
        )[1:6]

        # Clean output
        print(f"\n--- Recommendations for {movie_name} ---")

        # Print only titles
        for i in distances:

            # TEMPORARY slowdown test
            

            print(movies_list[i[0]])

    except Exception:
        print("Movie not found. Please try again.")


# Main execution
if __name__ == "__main__":

    # Load once
    m_list, s_mat = load_assets()

    # Test recommendation
    get_recommendations("Batman Begins", m_list, s_mat)