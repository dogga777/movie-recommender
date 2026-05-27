# Import the pickle library to load binary files
import pickle

# Import os to check if files exist
import os

# Define the paths to our saved model files
model_files = [
    'models/movies_list.pkl',
    'models/similarity.pkl'
]

# Define the audit function
def run_final_audit():
    print("🕵️ Starting Final Engine Audit...")

    # Check if models folder exists
    if not os.path.exists('models'):
        print("❌ Error: 'models' folder is missing!")
        return

    # Check each model file
    for file_path in model_files:
        if os.path.exists(file_path):

            # Get file size in MB
            file_size = os.path.getsize(file_path) / (1024 * 1024)

            print(f"✅ Found {file_path} ({file_size:.2f} MB)")
        else:
            print(f"❌ Error: {file_path} is missing!")
            return

    # Final brain wake-up test
    try:
        with open('models/movies_list.pkl', 'rb') as f:
            movies = pickle.load(f)

        print(f"🧠 Brain Wake-up Success: {len(movies)} movies ready in memory.")

        print("🚀 STATUS: READY FOR PRODUCTION")

    except Exception as e:
        print(f"❌ Brain Wake-up Failed: {e}")

# Run the audit
run_final_audit()