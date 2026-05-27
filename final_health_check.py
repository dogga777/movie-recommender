import os

core_files = ["recommend.py", "README.md", ".gitignore"]

def final_health_check():

    print("📋 Running Final File Health Check...")
    print("-" * 30)

    for file in core_files:

        if os.path.exists(file):

            file_size = os.path.getsize(file)

            if file_size > 0:
                print(f"✅ {file} is present and has data ({file_size} bytes).")
            else:
                print(f"⚠️ {file} is EMPTY!")

        else:
            print(f"❌ {file} is MISSING!")

    print("-" * 30)
    print("Check complete.")

if __name__ == "__main__":
    final_health_check()