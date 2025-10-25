
# Movie Recommendation System

A hybrid movie recommendation system using MovieLens 100K that combines collaborative filtering with content-based recommendations, wrapped in a Streamlit UI for interactive use.[1][2]

## Project Structure

```
.
├── stream_app.py
├── rec/
│   ├── __init__.py
│   ├── data_preprocessing.py
│   ├── collaborative.py
│   ├── content_based.py
│   └── sentiment.py   # optional
├── data/
│   └── movielens/     # or ml-100k/ raw files (u.data, u.item, etc.)
├── notebooks/
│   └── movie_recommender.ipynb
├── requirements.txt
└── README.md
```


## Prerequisites

- Python 3.8+ installed.[3]
- A virtual environment tool (venv is built into Python 3).[3]
- MovieLens 100K dataset downloaded and extracted.[4]

## Setup

1) Create and activate a virtual environment:
- Windows PowerShell:
  - python -m venv .venv
  - .\.venv\Scripts\Activate.ps1
  - If blocked, run once: Set-ExecutionPolicy -Scope CurrentUser RemoteSigned[5][3]
- macOS/Linux:
  - python3 -m venv .venv
  - source .venv/bin/activate[6][3]

2) Install dependencies:
- pip install -r requirements.txt[2]

3) Place dataset files:
- Put u.data and u.item into data/movielens/ or reference your existing ml-100k path in code.[4]

4) Optional (for sentiment):
- pip install textblob
- python -m textblob.download_corpora[7]

## Running the Streamlit App

From the project root (where app/ and rec/ are siblings), run:
- streamlit run app/stream_app.py[8]

The app will open in your browser at http://localhost:8501 and auto-reload on code changes.[8]

## Paths on Windows

When reading MovieLens 100K raw files, use raw strings or forward slashes to avoid unicode escape errors, for example:
- ratings = pd.read_csv(r'H:\machine\ml-100k\u.data', sep='\t', names=[...])[9]

## What the App Does

- Collaborative filtering: builds a user–movie ratings matrix and uses cosine similarity to find nearest neighbors, recommending highly rated unseen movies.[10][2]
- Content-based filtering: TF–IDF vectorizes genres and retrieves similar movies via cosine similarity.[11][2]
- Hybrid mode: combines candidates from both and returns top 5 recommendations.[2]

## Running the Notebook

Open notebooks/movie_recommender.ipynb to walk through data loading, EDA, model steps, and testing individual functions before integrating with Streamlit.[2]

## Common Issues

- ImportError: No module named 'rec'
  - Ensure rec/__init__.py exists and run from project root: streamlit run app/stream_app.py.[12]
- PowerShell activation error
  - Use .\.venv\Scripts\Activate.ps1 and set execution policy as shown above.[5]
- Git line endings warnings (Windows)
  - Optional: create .gitattributes with “* text=auto” and normalize, or ignore and proceed; warnings are harmless.[5]

## Recommended .gitignore

```
# Python
__pycache__/
*.pyc

# Environments
.venv/
venv/
env/

# Data and artifacts
data/movielens/
ml-100k/
*.zip

# OS
.DS_Store
```


## References

- MovieLens 100K dataset overview and download.[4]
- End-to-end recommendation guides and hybrid examples.[11][2]
- Collaborative filtering basics with cosine similarity.[10]
- Streamlit app setup and running.[8]
- Virtual environments: create, activate, deactivate.[3][5]
- __init__.py usage in Python packages.[12]

[1](https://www.kaggle.com/datasets/parasharmanas/movie-recommendation-system)
[2](https://www.freecodecamp.org/news/build-a-movie-recommendation-system-with-python/)
[3](https://docs.python.org/3/library/venv.html)
[4](https://www.kaggle.com/datasets/prajitdatta/movielens-100k-dataset)
[5](https://realpython.com/python-virtual-environments-a-primer/)
[6](https://docs.python.org/3/tutorial/venv.html)
[7](https://textblob.readthedocs.io/en/dev/install.html)
[8](https://www.codewithfaraz.com/python/45/build-a-movie-recommendation-system-project-in-python-with-source-code)
[9](https://www.geeksforgeeks.org/python/creating-python-virtual-environment-windows-linux/)
[10](https://keras.io/examples/structured_data/collaborative_filtering_movielens/)
[11](https://dev.to/jesse_adu_akowuah_/building-a-movie-recommendation-system-with-streamlit-and-python-5bkm)
[12](https://realpython.com/python-init-py/)
[13](https://code.visualstudio.com/docs/python/environments)

![Screenshot_25-10-2025_184629_localhost](https://github.com/user-attachments/assets/e1c87b04-4616-4b61-9e09-368ea54b24b3)
