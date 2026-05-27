import subprocess

def check_git_config():
    print("🔍 Checking your local Git identity...")

    user = subprocess.getoutput("git config user.name")
    email = subprocess.getoutput("git config user.email")

    print(f"👤 Current Name: {user}")
    print(f"📧 Current Email: {email}")

    if user == "" or email == "":
        print("⚠️ Warning: Your local Git identity is not set yet!")
    else:
        print("✅ Local identity found. Ready to link to GitHub!")

if __name__ == "__main__":
    check_git_config()