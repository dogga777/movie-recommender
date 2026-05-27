import subprocess

def verify_local_git():

    print("🔍 Checking if local Git is initialized...")

    result = subprocess.run(
        ["git", "status"],
        capture_output=True,
        text=True
    )

    if "fatal" in result.stderr:
        print("❌ Local Git NOT found.")
    else:
        print("✅ Local Git is active and connected.")

if __name__ == "__main__":
    verify_local_git()