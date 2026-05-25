# Create a list of movie genres
genres = ["Action", "Sci-Fi", "Comedy", "Drama"]

# Function to validate genres
def validate_genre(user_input):

    # Convert input to title case
    formatted_input = user_input.title()

    # Check if genre exists
    if formatted_input in genres:

        # Success message
        return f"✅ {formatted_input} is a valid genre for our engine."

    else:

        # Failure message
        return f"❌ {formatted_input} is not in our database."


# Test the function
test_result = validate_genre("sci-fi")

# Print result
print(test_result)