# Import the library that turns strings into real Python lists
import ast

# Define the 'Unpacker' function
def convert_to_list(text):
    
    # Create an empty list
    clean_list = []

    # Convert string into real Python list
    data = ast.literal_eval(text)

    # Loop through each dictionary
    for i in data:

        # Extract only the 'name'
        clean_list.append(i['name'])

    # Return final clean list
    return clean_list


# --- TESTING THE TOOL ---

# Add 3 genres
messy_data = '[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"}]'

# Call the function
result = convert_to_list(messy_data)

# Print output
print(f"Original: {messy_data}")
print(f"Unpacked: {result}")