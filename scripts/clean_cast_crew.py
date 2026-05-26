# Import the tool to convert strings into Python lists
import ast

# Function 1: Get Top 3 Actors
def get_top_3(text):

    # Empty list for actors
    actors = []

    # Convert string into real Python list
    data = ast.literal_eval(text)

    # Loop through first 3 actors
    for i in data[0:3]:

        # Add actor name
        actors.append(i['name'])

    # Return actor list
    return actors


# Function 2: Find Director
def get_director(text):

    # Convert string into real Python list
    data = ast.literal_eval(text)

    # Search every crew member
    for i in data:

        # Find Director
        if i['job'] == 'Director':

            # Return director name inside a list
            return [i['name']]

    # Return empty list if no director found
    return []


# --- TESTING THE VIP FILTER ---

# Cast data
messy_cast = '[{"name": "Robert Downey Jr."}, {"name": "Terrence Howard"}, {"name": "Jeff Bridges"}, {"name": "Gwyneth Paltrow"}]'

# Crew data with Director FIRST
messy_crew = '[{"job": "Director", "name": "Jon Favreau"}, {"job": "Producer", "name": "Kevin Feige"}]'

# Run the functions
print(f"Top 3 Actors: {get_top_3(messy_cast)}")
print(f"Director: {get_director(messy_crew)}")