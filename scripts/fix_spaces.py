# Function to remove spaces from names
def collapse_names(name_list):

    # Empty list for cleaned names
    squished_list = []

    # Loop through every name
    for name in name_list:

        # Remove spaces
        clean_name = name.replace(" ", "")

        # Add cleaned name to list
        squished_list.append(clean_name)

    # Return cleaned list
    return squished_list


# --- TESTING THE SQUISH ---

# Actors list
actors = ["Tom Cruise", "Tom Hanks", "Scarlett Johansson"]

# Director list
directors = ["Christopher Nolan"]

# Run function on actors
cleaned_actors = collapse_names(actors)

# Run function on directors
cleaned_directors = collapse_names(directors)

# Print results
print(f"Original Actors: {actors}")
print(f"Squished Actors: {cleaned_actors}")

print("\nOriginal Director:", directors)
print(f"Squished Director: {cleaned_directors}")

# Success check
if "TomCruise" in cleaned_actors and "Tom" not in cleaned_actors:
    print("\n✅ Success: The 'Tom' confusion has been prevented!")

if "ChristopherNolan" in cleaned_directors:
    print("✅ Director name cleaned successfully!")