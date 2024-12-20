import os
import requests
from tqdm import tqdm  # For progress bar
import pandas as pd

# Load CSV
csv_path = '.\~Not Used\Docs\movie_genre_sample_500.csv'
data = pd.read_csv(csv_path)

# Folder to save the images
save_dir = '.\images'
os.makedirs(save_dir, exist_ok=True)

# Download
for index, row in tqdm(data.iterrows(), total=len(data)):
    url = row['Poster']
    imdb_id = row['imdbId']
    
    if pd.notnull(url):  # Check URL is valid
        try:
            response = requests.get(url, stream=True, timeout=10)
            if response.status_code == 200:
                # Save image with the imdbId as the filename
                file_path = os.path.join(save_dir, f"{imdb_id}.jpg")
                with open(file_path, 'wb') as f:
                    f.write(response.content)
        except Exception as e:
            print(f"Failed to download {url}: {e}")

print(f"Images have been downloaded to: {save_dir}")
