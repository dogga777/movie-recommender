# Import pandas to handle our movie table
import pandas as pd

# Import the text-to-math tool
from sklearn.feature_extraction.text import TfidfVectorizer

# Import the similarity calculator
from sklearn.metrics.pairwise import cosine_similarity


# Function to verify tools are working
def system_check():
    try:
        # Load the clean dataset
        df = pd.read_csv('data/processed_movies.csv')

        # Initialize the vectorizer
        tfidf = TfidfVectorizer(stop_words='english')

        # Dummy check for cosine similarity
        check_math = cosine_similarity

        # Success messages
        print("✅ Industrial Tools Imported Successfully!")
        print(f"✅ Dataset with {len(df)} movies loaded and ready for math.")

    except Exception as e:
        # Error message
        print(f"❌ System Check Failed: {e}")


# Run the function
system_check()