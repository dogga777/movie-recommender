# Import the pandas library
import pandas as pd

# Define the dataset path
file_path = 'data/movies_5000.csv'

# Load the dataset
df = pd.read_csv(file_path)

# Count all missing values
null_report = df.isnull().sum()

# Print the report header
print("--- Missing Data Audit (Null Counts) ---")

# Display null counts
print(null_report)

# Extra observation
print("\n🔍 Observation:")
print(f"The 'overview' column has {null_report['overview']} missing values.")