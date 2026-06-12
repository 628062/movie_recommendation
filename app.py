import streamlit as st
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load dataset
df = pd.read_csv("data/cleaned_movies.csv")


# Fill missing values
df["Cleaned_Storyline"] = df["Cleaned_Storyline"].fillna("")


# TF-IDF Vectorization
tfidf = TfidfVectorizer()

tfidf_matrix = tfidf.fit_transform(df["Cleaned_Storyline"])


# Cosine Similarity Matrix
similarity = cosine_similarity(tfidf_matrix)


# Recommendation Function
def recommend(movie_name):

    # Find matching movies
    matches = df[df["Movie Name"].str.contains(movie_name, case=False)]

    # If movie not found
    if matches.empty:
        return []

    # Get movie index
    idx = matches.index[0]

    # Get similarity scores
    distances = list(enumerate(similarity[idx]))

    # Sort movies based on similarity
    sorted_movies = sorted(
        distances,
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    recommendations = []

    # Store recommended movie name + storyline
    for i in sorted_movies:

        movie_title = df.iloc[i[0]]["Movie Name"]

        movie_story = df.iloc[i[0]]["Storyline"]

        recommendations.append((movie_title, movie_story))

    return recommendations


# Streamlit UI
st.title("IMDb Movie Recommendation System")

st.write("Get top 5 movie recommendations based on storyline similarity")


# User input
movie_input = st.text_input("Enter Movie Name")


# Button
if st.button("Recommend"):

    recommendations = recommend(movie_input)

    # If movie not found
    if len(recommendations) == 0:

        st.error("Movie not found in dataset")

    else:

        st.subheader("Top 5 Recommended Movies")

        # Show recommendations
        for movie, story in recommendations:

            st.subheader(movie)

            st.write(story)

            st.write("-----------")