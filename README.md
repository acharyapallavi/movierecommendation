# 🎬 Movie Recommendation System

A machine learning–based movie recommendation system built using Python and Streamlit.  
The app suggests similar movies based on user selection.

## 🚀 Features
- Movie recommendations using cosine similarity
- Interactive Streamlit web interface
- Large model files handled via Google Drive
- Deployed on Render

## 🛠 Tech Stack
- Python
- Streamlit
- Pandas
- Scikit-learn
- Pickle

## 📂 Project Structure
- `app.py` – Streamlit application
- `movie.pkl` – Movie data file (downloaded at runtime)
- `similarity.pkl` – Similarity matrix (downloaded at runtime)
- `requirements.txt` – Python dependencies
- `setup.sh` – Render setup
- `Procfile` – Deployment command

## ▶️ How to Run Locally
1. Clone the repository
```bash
git clone https://github.com/acharyapallavi/movierecommendation.git
