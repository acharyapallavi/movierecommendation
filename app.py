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

# -------- REQUIRED FIXES BELOW --------
SIMILARITY_FILE = "similarity.pkl"
GDRIVE_URL = "https://drive.google.com/file/d/1J3dlEWIL_VKGQhXBeB4x4yP6zD9OnOsg/view?usp=sharing"

if not os.path.exists(SIMILARITY_FILE):
    print("Downloading similarity.pkl from Google Drive...")
    gdown.download(GDRIVE_URL, SIMILARITY_FILE, quiet=False)

movie = pickle.load(open('movie.pkl', 'rb'))        # ← was missing
similarity = pickle.load(open('similarity.pkl','rb'))
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



