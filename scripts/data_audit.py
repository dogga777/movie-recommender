import pandas as pd
import os

file_path = "data/movies_5000.csv"

def run_data_audit():
    print("📋 STARTING DATA AUDIT CHECKPOINT...")
    print("-" * 40)

    # CHECK 1: File existence
    if not os.path.exists(file_path):
        print("❌ FAILED: 'movies_5000.csv' not found in data folder.")
        return
    else:
        print("✅ PASS: Dataset file detected.")

    # Load dataset
    df = pd.read_csv(file_path)

    # CHECK 2: Missing values in overview
    if "overview" in df.columns:
        null_count = df["overview"].isnull().sum()
        if null_count == 0:
            print("✅ PASS: No missing values in 'overview'.")
        else:
            print(f"⚠️ WARNING: {null_count} missing overviews.")
    else:
        print("❌ FAILED: 'overview' column not found.")

    # CHECK 3: Required columns
    required_cols = ['id', 'title', 'genres', 'overview', 'keywords']
    found_cols = [col for col in required_cols if col in df.columns]

    if len(found_cols) == len(required_cols):
        print("✅ PASS: All critical feature columns are present.")
    else:
        missing = set(required_cols) - set(found_cols)
        print(f"❌ FAILED: Missing columns: {missing}")

    print("-" * 40)
    print("AUDIT COMPLETE: Your data is ready for Module 3!")

if __name__ == "__main__":
    run_data_audit()