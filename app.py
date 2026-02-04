import streamlit as st
import pickle
import requests
import gdown
import os
def fetch_poster(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=a986eff7033a86ff0e2a384fcd958219'.format(movie_id)
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        data = response.json()
        poster_path = data.get('poster_path')

        # If poster is missing, return placeholder
        if not poster_path:
            return "https://via.placeholder.com/500"

        return 'https://image.tmdb.org/t/p/w500' + poster_path

    except:
        # In case of network or JSON error
        return "https://via.placeholder.com/500"





def recommend(moviename):
    movie_index = movie[movie['title'] == moviename].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda X: X[1]
    )[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_list:
        movie_id = movie.iloc[i[0]].movie_id
        recommended_movies_posters.append(fetch_poster(movie_id))
        recommended_movies.append(movie.iloc[i[0]].title)

    return recommended_movies,recommended_movies_posters   # ← moved outside loop (REQUIRED)

SIMILARITY_FILE = "similarity.pkl"
MOVIE_FILE = "movie.pkl"

SIMILARITY_URL = "https://drive.google.com/uc?id=1J3dlEWIL_VKGQhXBeB4x4yP6zD9OnOsg"
MOVIE_URL = "https://drive.google.com/uc?id=14q6i9M1JoxHYG-u1SVicKOQ4L7B-BaAU"

# Download similarity.pkl
if not os.path.exists(SIMILARITY_FILE):
    st.write("Downloading similarity.pkl...")
    gdown.download(SIMILARITY_URL, SIMILARITY_FILE, quiet=False)

# Download movie.pkl
if not os.path.exists(MOVIE_FILE):
    st.write("Downloading movie.pkl...")
    gdown.download(MOVIE_URL, MOVIE_FILE, quiet=False)

# SAFETY CHECK
if not os.path.exists(MOVIE_FILE):
    st.error("movie.pkl still not found after download")
    st.stop()

if not os.path.exists(SIMILARITY_FILE):
    st.error("similarity.pkl still not found after download")
    st.stop()

# Load files
movie = pickle.load(open(MOVIE_FILE, "rb"))
similarity = pickle.load(open(SIMILARITY_FILE, "rb"))
st.title('movie recommendation system')
movie_list = movie['title'].values                  # ← fixed
select_movie_name = st.selectbox(
    'How would you like to contacted',
    movie_list
)

if st.button('recommend'):
    names, posters = recommend(select_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    for i, col in enumerate([col1, col2, col3, col4, col5]):
        with col:
            st.text(names[i])
            st.image(posters[i])
            # Show caption if using placeholder
            if posters[i] == "https://via.placeholder.com/500":
                st.write("Poster not available")



