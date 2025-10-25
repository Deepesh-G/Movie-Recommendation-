import streamlit as st
from rec.data_preprocessing import load_data, preprocess_movies
from rec.Content_Based import create_genre_matrix, get_content_recommendations

# -------------- PAGE CONFIG -----------------
st.set_page_config(
    page_title="Movie Recommendation System 🎥",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -------------- CUSTOM CSS -----------------
st.markdown("""
    <style>
    /* Main background */
    .stApp {
        background: linear-gradient(120deg, #0f2027, #203a43, #2c5364);
        color: #fff;
        font-family: 'Poppins', sans-serif;
    }
    
    /* Title styling */
    .main-title {
        font-size: 40px;
        text-align: center;
        font-weight: 700;
        color: #ffcc70;
        text-shadow: 1px 1px 3px rgba(255,255,255,0.3);
        margin-bottom: 10px;
    }

    /* Subtitle styling */
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #e0e0e0;
        margin-bottom: 40px;
    }

    /* Input box */
    input {
        border-radius: 10px !important;
    }

    /* Table styling */
    table {
        background-color: rgba(255,255,255,0.1);
        color: white;
        border-radius: 10px;
    }
    th {
        background-color: #ffcc70 !important;
        color: black !important;
    }
    tr:nth-child(even) {
        background-color: rgba(255,255,255,0.05);
    }

    /* Button */
    div.stButton > button {
        background-color: #ffcc70;
        color: black;
        border: none;
        padding: 0.6em 2em;
        border-radius: 12px;
        font-weight: 600;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #fff176;
        transform: scale(1.05);
    }

    </style>
""", unsafe_allow_html=True)


# -------------- PAGE TITLE -----------------
st.markdown("<div class='main-title'>🎬 Movie Recommendation System</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Find movies similar to your favorites using content-based filtering</div>", unsafe_allow_html=True)


# -------------- LOAD DATA -----------------
@st.cache_data(show_spinner=True)
def load_and_prepare_data():
    movies, ratings = load_data('H:\\machine\\ml-100k\\u.item', 'H:\\machine\\ml-100k\\u.data')
    movies = preprocess_movies(movies)
    genre_mat, _ = create_genre_matrix(movies)
    return movies, genre_mat

with st.spinner("Loading data..."):
    movies, genre_mat = load_and_prepare_data()

# -------------- INPUT -----------------
movie_name = st.text_input("🎞️ Enter your favorite movie:")

if movie_name:
    try:
        recs = get_content_recommendations(movie_name, movies, genre_mat)
        st.markdown("### 🍿 Top Recommendations")
        st.table(recs)
    except Exception as e:
        st.error(f"⚠️ {e}")

# -------------- FOOTER -----------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center;color:#ccc;'>Made with ❤️ using Streamlit & Scikit-learn</p>",
    unsafe_allow_html=True
)
