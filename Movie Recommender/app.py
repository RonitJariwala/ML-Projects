import streamlit as st
import pickle
import pandas as pd
import requests

# Load data
movies_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)  # Ensure this correctly forms a DataFrame
similarity = pickle.load(open('similarity.pkl', 'rb'))

# TMDb API key (Replace with your actual key)
API_KEY = "b99d9cbcb815f545549aabca7c5dea5b"

def fetch_poster(movie_id):
    """Fetch movie poster URL from TMDb API."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return f"https://image.tmdb.org/t/p/w500{data['poster_path']}" if data['poster_path'] else None
    return None

def recommend(movie):
    """Recommend similar movies and fetch their posters."""
    try:
        # Ensure the movie exists in the dataset
        if movie not in movies['title'].values:
            st.error("❌ Movie not found! Please try another title.")
            return [], []

        # Find the index of the selected movie
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]

        # Get the top 5 similar movies
        recommended_movies = sorted(
            list(enumerate(distances)), reverse=True, key=lambda x: x[1]
        )[1:6]

        movie_titles = []
        posters = []

        for i in recommended_movies:
            movie_id = movies.iloc[i[0]]['movie_id'] 
            movie_titles.append(movies.iloc[i[0]]['title'])
            posters.append(fetch_poster(movie_id))

        return movie_titles, posters

    except Exception as e:
        st.error(f"⚠️ An error occurred: {e}")
        return [], []

# Streamlit UI
st.title("🎬 Movie Recommender System")
movie_titles = movies['title'].values
selected_movie_name = st.selectbox("🔍 Select a movie:", movie_titles)

if st.button("Recommend"):
    recommendations, posters = recommend(selected_movie_name)

    if recommendations:
        st.write("### ✅ Recommended Movies:")
        
        cols = st.columns(5)  # Create 5 columns for layout
        for col, movie, poster in zip(cols, recommendations, posters):
            with col:
                st.text(movie)
                st.image(poster if poster else "https://via.placeholder.com/500", width=150)
