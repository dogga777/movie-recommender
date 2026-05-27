"""
Movie Recommendation Engine - Final Polished Version
Goal: Content-based filtering using Cosine Similarity.
"""

import pickle


def load_engine_assets():
    
    
    
    
    
    
    
    
    
    
    """Load serialized movie data and similarity matrix."""

    try:
        # Open both files safely
        with open('models/movies_list.pkl', 'rb') as f_list, \
             open('models/similarity.pkl', 'rb') as f_sim:

            return pickle.load(f_list), pickle.load(f_sim)

    except FileNotFoundError:

        print("Error: Model files not found.")
        return None, None


def get_recommendations(movie_title, movies_list, similarity_matrix):
    """
    Find and display top 5 similar movies.
    """

    try:
        # Find movie index
        movie_idx=movies_list.index(movie_title)

        # Sort similarity scores
        similarity_scores = sorted(
            list(enumerate(similarity_matrix[movie_idx])),
            reverse=True,
            key=lambda x: x[1]
        )[1:6]

        print(f"\n--- Top Recommendations for {movie_title} ---")

        # Print recommendations
        for match in similarity_scores:
            print(f"🎬 {movies_list[match[0]]}")

    except ValueError:

        print(f"❌ '{movie_title}' not found in database.")

    except Exception as error:

        print(f"⚠️ Unexpected error: {error}")


if __name__ == "__main__":

    # Load engine assets
    movies, similarity = load_engine_assets()

    # Run recommendation
    if movies is not None:
        get_recommendations(
            "The Dark Knight Rises",
            movies,
            similarity
        )
        # Final update