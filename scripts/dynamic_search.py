# Import pandas (optional for now)
import pandas as pd

# Define function with TWO parameters
def search_engine(user_choice, num_results):

    # Print search message using both parameters
    print(f"🔍 Finding {num_results} results for {user_choice}...")

    # Create simulated recommendation list
    results = [
        f"{user_choice} 2",
        f"{user_choice} 3",
        f"{user_choice}: Origins"
    ]

    # Return the results
    return results


# --- EXECUTION SECTION ---

# Call the function with arguments
movie_list = search_engine("Iron Man", 5)

# Print recommendations
print(f"Recommended for you: {movie_list}")