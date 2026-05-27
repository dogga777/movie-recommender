import webbrowser
import subprocess

def verify_and_open():

    print("🌐 Fetching your Remote Repository URL...")

    cmd = subprocess.run(
        ["git", "remote", "get-url", "origin"],
        capture_output=True,
        text=True
    )

    if cmd.returncode == 0:

        url = cmd.stdout.strip().replace(".git", "")

        print(f"✅ Found: {url}")
        print("🚀 Opening your browser for Verification...")

        webbrowser.open(url)

    else:
        print("❌ Error: Could not find remote URL.")


if __name__ == "__main__":
    verify_and_open()