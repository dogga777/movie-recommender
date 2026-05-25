# Function 1: Prepares the search word
def format_search(raw_input):

    # Convert text to lowercase
    clean_text = raw_input.lower()

    # Debug message
    print(f"DEBUG: Formatted input to {clean_text}")

    # Return cleaned text
    return clean_text


# Function 2: Simulates recommendation
def get_recommendation(movie_name):

    # Call first function
    target = format_search(movie_name)

    # Return recommendation
    return f"Since you liked {target}, you will like Avengers."


# --- MAIN EXECUTION ---

# Messy user input
user_query = "iRoN mAn"

# Main function call
final_result = get_recommendation(user_query)

# Print output
print(final_result)