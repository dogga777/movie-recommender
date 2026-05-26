# Import the 'pickle' library
import pickle

# Import os to create folders
import os

# Step 1: Create a mock recommendation brain
engine_brain = {
    "Iron Man": 0.99,
    "Avengers": 0.85,
    "The Lion King": 0.12
}

# Step 2: Ensure the models folder exists
if not os.path.exists('models'):
    os.makedirs('models')

# Step 3: Serialize (Pickle) the data
print("📦 Packing the brain into a pickle file...")

with open('models/test_model.pkl', 'wb') as file:
    pickle.dump(engine_brain, file)

# Step 4: Remove variable from memory
engine_brain = None

print(f"Memory Check: Variable is now {engine_brain}")

# Step 5: Deserialize (Unpickle) the data
print("🔓 Unpacking the brain to use it again...")

with open('models/test_model.pkl', 'rb') as file:
    restored_brain = pickle.load(file)

# Verify it worked
print(f"Restored Data: {restored_brain}")