# Create a mock row of already cleaned data
movie_data = {
    'overview': 'A billionaire builds a high-tech suit to fight crime.',
    'genres': ['Action', 'Sci-Fi', 'Adventure'],
    'keywords': ['superhero', 'marvel', 'billionaire'],
    'cast': ['RobertDowneyJr', 'TerrenceHoward', 'JeffBridges'],
    'director': ['JonFavreau'],

    # Added new mood list
    'mood': ['Exciting', 'Intense']
}

# Step 1: Convert overview string into a list
overview_list = movie_data['overview'].split()

# Step 2: Combine all lists into one master list
combined_list = (
    overview_list
    + movie_data['genres']
    + movie_data['keywords']
    + movie_data['cast']
    + movie_data['director']
    + movie_data['mood']
)

# Step 3: Convert the master list into one string
tags_string = " ".join(combined_list)

# Step 4: Convert everything to lowercase
final_tags = tags_string.lower()

# Print final result
print("--- The Final Blend ---")
print(f"Final Tags Column Content:\n{final_tags}")