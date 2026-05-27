import subprocess

def check_network_bridge():

    print("🛰️ Testing connection to GitHub 'Remote'...")

    result = subprocess.run(
        ["git", "remote", "-v"],
        capture_output=True,
        text=True
    )

    if "github.com" in result.stdout:

        print("✅ Connection Path Found:")
        print(result.stdout.strip())

        print("\n🚀 You are cleared for launch!")

    else:
        print("❌ Error: No GitHub remote found.")


if __name__ == "__main__":
    check_network_bridge()