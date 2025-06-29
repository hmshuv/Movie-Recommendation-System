import streamlit as st
import pandas as pd
import pickle
import requests
import time
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()
retries = Retry(total=3, backoff_factor=0.5, status_forcelist=[429, 500, 502, 503, 504])
session.mount('https://', HTTPAdapter(max_retries=retries))


movie_df = pickle.load(open("movie.pkl", "rb"))
movie_title = movie_df['title'].values
similarity = pickle.load(open("similarity.pkl", "rb"))

@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
       
        response = session.get(url, timeout=5)
        data = response.json()
        poster_path = data.get("poster_path")
        st.text(f"Movie ID: {movie_id}")
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster"
    except Exception as e:
        st.warning(f"Error fetching poster: {e}")
        return "https://via.placeholder.com/500x750?text=Error"

   

def recommend(movie, similarity, df):
    movie_index = df[df["title"] == movie].index[0]
    distances = similarity[movie_index]
    movie_indices = sorted(
        list(enumerate(distances)), reverse=True, key=lambda x: x[1]
    )[1:6]

    recommendations = []
    recommended_posters = []

    for i in movie_indices:
        recommendations.append(df.iloc[i[0]].title)
        movie_id = df.iloc[i[0]].id 
        time.sleep(0.5) 
        recommended_posters.append(fetch_poster(movie_id))

    return recommendations, recommended_posters

st.title("🎬 Movie Recommendation System")

selected_movie_name = st.selectbox("Enter your favorite movie:", movie_title)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name, similarity, movie_df)

    st.subheader("You might also like:")
    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.subheader(names[i])
            st.image(posters[i])