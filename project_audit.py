# Import the os library
import os

# Professional project checklist
professional_checklist = [
    "recommend.py",
    "models",
    "data",
    "README.md",
    ".gitignore"
]


def run_audit():

    print("🕵️ Starting Project Audit for GitHub Readiness...")
    print("-" * 50)

    # Get all current files/folders
    current_files = os.listdir(".")

    # Check required items
    for item in professional_checklist:

        if item in current_files:
            print(f"✅ FOUND: {item}")

        else:
            print(f"❌ MISSING: {item} - Recruiter might be confused!")

    print("-" * 50)
    print("💡 Tip: A clean folder structure makes you look professional.")


# Run audit
if __name__ == "__main__":
    run_audit()