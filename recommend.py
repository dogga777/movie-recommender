import pickle
import pandas as pd

# LOAD THE ENGINE FILES
with open('models/movies_list.pkl', 'rb') as f:
    movies_list = pickle.load(f)

with open('models/similarity.pkl', 'rb') as f:
    similarity_matrix = pickle.load(f)

# RECOMMENDATION FUNCTION
def recommend(movie):
    try:
        # Find movie index
        index = movies_list[movies_list['title'] == movie].index[0]

        # Get similarity scores
        distances = sorted(
            list(enumerate(similarity_matrix[index])),
            reverse=True,
            key=lambda x: x[1]
        )

        # Top 5 recommendations
        top_5 = distances[1:6]

        # Display Results
        print(f"\n🌟 Because you liked '{movie}', you might also enjoy:")
        print("-" * 40)

        for i in top_5:
            recommended_movie_index = i[0]

            movie_title = movies_list.iloc[recommended_movie_index].title

            print(f"🎬 {movie_title}")

        print("-" * 40)

    except IndexError:
        print(f"❓ Movie '{movie}' not found.")

# TEST THE ENGINE
recommend("The Dark Knight Rises")