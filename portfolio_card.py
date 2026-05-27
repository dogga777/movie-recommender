import subprocess

def generate_portfolio_snippet():

    repo_url_raw = subprocess.getoutput("git remote get-url origin")

    repo_url = repo_url_raw.replace(".git", "")

    project_title = "Movie Recommendation Engine"

    tech_used = "Python, Pandas, Scikit-Learn, Cosine Similarity"

    key_achievement = "Built a content-based filtering engine for 5,000+ movies."

    print("\n" + "="*50)
    print("🚀 YOUR PROFESSIONAL PORTFOLIO SNIPPET 🚀")
    print("="*50)
    print(f"Project: {project_title}")
    print(f"URL:     {repo_url}")
    print(f"Stack:   {tech_used}")
    print(f"Impact:  {key_achievement}")
    print("="*50)

if __name__ == "__main__":
    generate_portfolio_snippet()