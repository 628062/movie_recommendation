import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load cleaned dataset
df = pd.read_csv("data/cleaned_movies.csv")

# Fill missing values (safety)
df["Cleaned_Storyline"] = df["Cleaned_Storyline"].fillna("")

# STEP 1: Convert text to vectors
tfidf = TfidfVectorizer()

tfidf_matrix = tfidf.fit_transform(df["Cleaned_Storyline"])

# STEP 2: Compute similarity
similarity = cosine_similarity(tfidf_matrix)

# Show shape
print("Similarity matrix shape:", similarity.shape)

def recommend(movie_name):
    idx = df[df["Movie Name"].str.contains(movie_name, case=False)].index[0]
    
    distances = list(enumerate(similarity[idx]))
    
    sorted_movies = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]
    
    for i in sorted_movies:
        print(df.iloc[i[0]]["Movie Name"])


recommend("Dune")