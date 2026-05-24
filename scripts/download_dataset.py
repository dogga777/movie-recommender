import urllib.request

# Dataset URL
url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/ufo.csv"

# Save location
output_file = "data/movies_5000.csv"

print("Downloading dataset...")

# Download the file
urllib.request.urlretrieve(url, output_file)

print("Download complete!")
print(f"Dataset saved to: {output_file}")