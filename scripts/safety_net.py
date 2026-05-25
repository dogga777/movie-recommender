# Create a small sample list of movies
available_movies = []

# Define a function to find a movie index
def get_movie_index(target):

    # TRY block
    try:

        # Find movie position
        index = available_movies.index(target)

        # Return success message
        return f"✅ Found! {target} is at position {index}."

    # EXCEPT block
    except ValueError:

        # Return error message instead of crashing
        return f"❌ Sorry, '{target}' is not in our database. Please check your spelling."


# --- TESTING THE SAFETY NET ---

# Existing movie
print(get_movie_index("Iron Man"))

# Missing movie
print(get_movie_index("Batman"))

# Program continues safely
print("\n🚀 Program finished successfully without crashing.")