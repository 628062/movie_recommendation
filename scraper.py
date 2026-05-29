from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Open Chrome browser
driver = webdriver.Chrome()

# IMDb 2024 movies page
url = "https://www.imdb.com/search/title/?title_type=feature&release_date=2024-01-01,2024-12-31"

driver.get(url)

# Wait for page to load
time.sleep(5)

# Find movie titles
movie_elements = driver.find_elements(By.TAG_NAME, "h3")

# Find storylines
story_elements = driver.find_elements(By.CLASS_NAME, "ipc-html-content-inner-div")

# Empty lists
movie_names = []
storylines = []

# Store movie titles
for movie in movie_elements:
    text = movie.text

    # Skip unwanted heading
    if text != "Recently viewed":
        movie_names.append(text)

# Store storylines
for story in story_elements:
    storylines.append(story.text)

# Make both lists same size
min_length = min(len(movie_names), len(storylines))

movie_names = movie_names[:min_length]
storylines = storylines[:min_length]

# Create DataFrame
df = pd.DataFrame({
    "Movie Name": movie_names,
    "Storyline": storylines
})

# Save CSV
df.to_csv("data/movies.csv", index=False)

print(df.head())

print("CSV file saved successfully!")

# Close browser
driver.quit()