# IMDb Movie Recommendation System Using Storylines

## Project Overview

The IMDb Movie Recommendation System is a Content-Based Recommendation System that suggests movies based on storyline similarity. The project extracts movie data from IMDb, preprocesses movie storylines using Natural Language Processing (NLP) techniques, and recommends the most similar movies using TF-IDF Vectorization and Cosine Similarity.

An interactive Streamlit application allows users to enter a movie title and receive the top 5 most similar movie recommendations.

---

# Problem Statement

With thousands of movies available online, users often struggle to find movies that match their interests. This project addresses that challenge by creating a recommendation engine that analyzes movie storylines and suggests movies with similar themes, plots, and content.

The system scrapes IMDb 2024 movie data, processes textual information using NLP techniques, converts storylines into numerical vectors, and calculates similarity scores to generate personalized recommendations.

---

# Business Use Cases

### Movie Recommendation

Users can discover movies similar to their favorite movies based on storyline content.

### Personalized Entertainment Suggestions

Recommend movies that match a user's story preferences and interests.

### Content Discovery

Help streaming platforms improve user engagement through intelligent movie recommendations.

### Recommender System Learning

Demonstrates how NLP and Machine Learning techniques are used in modern recommendation systems.

---

# Skills Demonstrated

* Python Programming
* Selenium Web Scraping
* Data Collection & Storage
* Pandas Data Manipulation
* Natural Language Processing (NLP)
* TF-IDF Vectorization
* Count Vectorization
* Cosine Similarity
* Machine Learning Fundamentals
* Data Cleaning & Preprocessing
* Streamlit Application Development
* Data Analysis
* Recommendation Systems

---

# Project Architecture

## Step 1: Data Scraping

### Source

IMDb 2024 Movies Page

### Tools Used

* Selenium
* Chrome WebDriver

### Extracted Fields

| Column Name | Description              |
| ----------- | ------------------------ |
| Movie_Name  | Name of the Movie        |
| Storyline   | Plot Summary / Storyline |

### Output

Movies are stored in:

```csv
movies.csv
```

---

## Step 2: Data Preprocessing

The movie storylines are cleaned using NLP techniques.

### Preprocessing Tasks

* Convert text to lowercase
* Remove punctuation
* Remove special characters
* Remove stop words
* Remove extra whitespace
* Tokenization

### Example

Original Storyline:

```text
A young wizard begins his journey at a magical school where he makes friends and enemies.
```

Processed Storyline:

```text
young wizard begins journey magical school makes friends enemies
```

---

## Step 3: Text Vectorization

To make storylines understandable for Machine Learning algorithms, text is converted into numerical vectors.

### Techniques Used

#### TF-IDF Vectorizer

Measures the importance of words in a storyline relative to the entire dataset.

Advantages:

* Reduces influence of common words
* Highlights important keywords
* Produces meaningful document vectors

#### Count Vectorizer

Converts text into frequency-based vectors.

---

## Step 4: Similarity Calculation

After vectorization, similarity between movies is calculated using Cosine Similarity.

### Cosine Similarity

Range:

* 1 = Highly Similar
* 0 = Completely Different

The similarity matrix is generated for all movies in the dataset.

---

## Step 5: Recommendation Engine

### Workflow

1. User selects a movie.
2. Retrieve its storyline vector.
3. Compare it with all other movies.
4. Calculate cosine similarity scores.
5. Sort movies by similarity.
6. Return Top 5 Recommended Movies.

---

# Dataset Information

### Dataset Source

IMDb 2024 Movies

### Dataset Format

CSV File

### Columns

| Column     | Description              |
| ---------- | ------------------------ |
| Movie_Name | Movie Title              |
| Storyline  | Original Movie Storyline |

### Processed Dataset

Additional Column:

| Column            | Description            |
| ----------------- | ---------------------- |
| Cleaned_Storyline | Preprocessed Storyline |

---

# Project Structure

```text
IMDb-Movie-Recommendation-System/
│
├── data/
│   ├── movies.csv
│   └── cleaned_movies.csv
│
├── scrape_movies.py
├── clean_data.py
├── recommendation.py
├── app.py
├── requirements.txt
└── README.md
```

---

# Technologies Used

## Programming Language

* Python

## Libraries

### Web Scraping

* Selenium

### Data Processing

* Pandas
* NumPy

### NLP

* NLTK
* SpaCy

### Machine Learning

* Scikit-Learn
* TF-IDF Vectorizer
* Count Vectorizer
* Cosine Similarity

### Visualization

* Matplotlib
* Seaborn

### Web Application

* Streamlit

# Running the Application

Launch Streamlit Application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

# Application Features

### User-Friendly Interface

* Select a movie from the dataset
* Click Recommend
* Instantly view Top 5 similar movies

### Recommendation Output

Displays:

* Recommended Movie Name
* Similarity-Based Suggestions
* Storyline Information

---

# Recommendation Workflow

```text
IMDb Dataset
      ↓
Data Cleaning
      ↓
NLP Preprocessing
      ↓
TF-IDF Vectorization
      ↓
Cosine Similarity Matrix
      ↓
Recommendation Engine
      ↓
Streamlit User Interface
```

---

# Example Use Case

### Input Movie

```text
Dune: Part Two
```

### Output

```text
1. Furiosa: A Mad Max Saga
2. Kingdom of the Planet of the Apes
3. Civil War
4. The Fall Guy
5. Godzilla x Kong: The New Empire
```

*Recommendations may vary depending on the dataset.*

---

# Challenges Faced

* Dynamic Web Scraping using Selenium
* Handling Missing Storylines
* Cleaning Unstructured Text Data
* Feature Extraction from Text
* Similarity Computation
* Recommendation Accuracy

---

# Learning Outcomes

Through this project, I gained practical experience in:

* Web Scraping with Selenium
* Data Collection and Storage
* Natural Language Processing
* TF-IDF and Count Vectorization
* Cosine Similarity
* Recommendation Systems
* Streamlit Development
* End-to-End Machine Learning Projects

---

# Future Enhancements

* Genre-Based Recommendations
* Actor and Director-Based Filtering
* Hybrid Recommendation System
* Deep Learning-Based Recommendations
* Movie Poster Integration
* TMDB API Integration
* Cloud Deployment
* Larger Movie Dataset

---

# Conclusion

The IMDb Movie Recommendation System demonstrates how NLP and Machine Learning techniques can be used to build an intelligent recommendation engine. By analyzing movie storylines and calculating similarity scores, the system successfully recommends movies that share similar themes and content. The project provides valuable hands-on experience in web scraping, text processing, machine learning, and web application development.
