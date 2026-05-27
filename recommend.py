import pickle
import pandas as pd

# LOAD THE ENGINE FILES
with open('models/movies_list.pkl', 'rb') as f:
    movies_list = pickle.load(f)

with open('models/similarity.pkl', 'rb') as f:
    similarity_matrix = pickle.load(f)

# RECOMMEND FUNCTION
def recommend(movie):

    try:
        # FIND MOVIE INDEX
        index = movies_list[movies_list['title'] == movie].index[0]

        # SORT SIMILARITY SCORES
        distances = sorted(
            list(enumerate(similarity_matrix[index])),
            reverse=True,
            key=lambda x: x[1]
        )

        # SUCCESS MESSAGE
        print(f"✅ Success! Showing recommendations for: {movie}")

    except IndexError:
        # FRIENDLY ERROR MESSAGE
        print(f"❓ Sorry! '{movie}' isn't in our 5,000-movie database. Check your spelling!")

    except Exception as e:
        # OTHER ERRORS
        print(f"⚠️ An unexpected error occurred: {e}")

# TESTING

recommend("Avatar")

# CHANGE THIS TO YOUR OWN NAME
recommend("Chandramouli")