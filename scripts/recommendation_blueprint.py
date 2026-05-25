# Import necessary libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Function 1: Load and clean dataset
def load_and_clean_data(path):

    try:
        # Load dataset
        df = pd.read_csv(path)

        # Replace missing overview values
        df['overview'] = df['overview'].fillna('')

        # Return cleaned dataframe
        return df

    except FileNotFoundError:

        # Error message
        print("❌ Error: The dataset file was not found!")

        return None


# Function 2: Create similarity matrix
def create_similarity_matrix(df):

    # Initialize TF-IDF vectorizer
    tfidf = TfidfVectorizer(
        stop_words='english',
        max_features=5000
    )

    # Convert text into vectors
    tfidf_matrix = tfidf.fit_transform(df['overview'])

    # Return cosine similarity matrix
    return cosine_similarity(tfidf_matrix)


# Function 3: Get movie recommendations
def get_recommendations(movie_title, df, sim_matrix):

    try:
        # Find movie index
        idx = df[df['title'] == movie_title].index[0]

        # Get similarity scores
        scores = list(enumerate(sim_matrix[idx]))

        # Sort scores
        scores = sorted(
            scores,
            key=lambda x: x[1],
            reverse=True
        )

        # Return top 3 recommendations
        return scores[1:4]

    except (IndexError, KeyError):

        return "❌ Movie not found in database."


# --- MASTER LOGIC FLOW ---

# Step 1: Load data
movies = load_and_clean_data('data/tmdb_5000_movies.csv')

# Step 2: Continue only if successful
if movies is not None:

    # Step 3: Create similarity matrix
    matrix = create_similarity_matrix(movies)

    # Step 4: User search
    user_search = "Iron Man"

    # Step 5: Get recommendations
    recommendations = get_recommendations(
        user_search,
        movies,
        matrix
    )

    # Step 6: Display results
    print(f"🎬 Recommendations for '{user_search}':")
    print(recommendations)