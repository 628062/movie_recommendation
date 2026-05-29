import pandas as pd
import re
from nltk.corpus import stopwords

# Load dataset
df = pd.read_csv("data/movies.csv")

# Lowercase
df["Cleaned_Storyline"] = df["Storyline"].str.lower()

# Remove punctuation
df["Cleaned_Storyline"] = df["Cleaned_Storyline"].apply(
    lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', x)
)

# Load English stopwords
stop_words = set(stopwords.words('english'))

# Remove stopwords
df["Cleaned_Storyline"] = df["Cleaned_Storyline"].apply(
    lambda x: " ".join(
        word for word in x.split() if word not in stop_words
    )
)

# Show result
print(df[["Storyline", "Cleaned_Storyline"]].head())

# Save cleaned dataset
df.to_csv("data/cleaned_movies.csv", index=False)

print("Cleaned dataset saved successfully!")