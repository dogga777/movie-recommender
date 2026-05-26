# Import the ast library
import ast

# Example JSON-style string from dataset
messy_cell = '[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}]'

# Check original type
print(f"Before Unwrapping: {type(messy_cell)}")

# Convert string into real Python list
clean_list = ast.literal_eval(messy_cell)

# Check new type
print(f"After Unwrapping: {type(clean_list)}")

# Print first genre
print(f"First Genre Found: {clean_list[0]['name']}")

# Loop through all genres
for item in clean_list:
    print(f"Found Genre: {item['name']}")

# --- ACTION ITEM ---

# Create messy keyword string
messy_keywords = '["superhero", "marvel", "billionaire"]'

# Convert string into Python list
clean_keywords = ast.literal_eval(messy_keywords)

# Print second item
print(f"\nSecond Keyword: {clean_keywords[1]}")