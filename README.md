# Movie Recommendation System

A lightweight, content‑based movie recommender.  Feed it a film you love and it will suggest five similar titles, complete with posters fetched live from **TMDB**.

---

##  Key Features

* **Content‑based filtering** – cosine‑similarity on a CountVectorizer matrix of text metadata (genres, cast, crew & keywords).
* **Streamlit UI** – clean single‑page app that works locally or on Heroku.
* **Live posters** – uses the TMDB API to pull high‑resolution poster images at runtime.
* **Docker‑/Heroku‑ready** – `Procfile` & `setup.sh` are included; large model files are stored via **Git LFS**.

---

## Repository Structure

| Path                         | Brief Description                                                              |
| ---------------------------- | ------------------------------------------------------------------------------ |
| `.ipynb_checkpoints/`        | Jupyter auto‑saves – can be ignored.                                           |
| `.gitattributes`             | Tells Git that `*.pkl` should be stored with **Git LFS**.                      |
| `.gitignore`                 | Patterns for files that should *not* be committed (e.g. virtual‑env, secrets). |
| `Procfile`                   | Declares the web process for Heroku/Render (`streamlit run app.py`).           |
| `README.md`                  | **You are here** – project documentation.                                      |
| `app.py`                     | Main **Streamlit** application that loads the models and renders the UI.       |
| `movie.pkl`                  | Pickled dataframe of the cleaned TMDB dataset (used for look‑ups).             |
| `movie_recommendation.ipynb` | Notebook that prepares data, engineers features and exports `*.pkl` files.     |
| `requirements.txt`           | All Python dependencies (Streamlit, scikit‑learn, requests, etc.).             |
| `setup.sh`                   | Shell script to install system‑level libs on Heroku build slug.                |
| `similarity.pkl`             | Cosine‑similarity matrix (≈ 176 MB) – stored via Git LFS.                      |
| `tmdb_5000_credits.csv`      | Original TMDB credits dataset.                                                 |
| `tmdb_5000_movies.csv`       | Original TMDB movies dataset.                                                  |

> **Note**: The large pickle files are tracked with Git LFS. After cloning, run `git lfs pull` to fetch them.

---

##  Getting Started

### 1. Clone the repo (with Git LFS)

```bash
# Install Git LFS once on your machine
brew install git-lfs     # macOS, or see https://git-lfs.github.com
git lfs install

# Then clone the project
git clone https://github.com/<your‑username>/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your TMDB API key

The app expects an environment variable called `TMDB_API_KEY`.

```bash
export TMDB_API_KEY="<your‑tmdb‑key>"     # macOS/Linux
set TMDB_API_KEY="<your‑tmdb‑key>"        # Windows PowerShell
```

Alternatively, open **`app.py`** and hard‑code the key (not recommended for public repos).

### 5. Run the Streamlit app

```bash
streamlit run app.py
```

The app will open at **`http://localhost:8501`**.  Choose a movie from the dropdown and enjoy your recommendations!

---



## 🖼️ Screenshots

| Home Screen                   | Recommendations                             |
| ----------------------------- | ------------------------------------------- |
| ![Home](screenshots/home.png) | ![Results](screenshots/recommendations.png) |

> Place your PNG/JPG files in a `screenshots/` directory so the images render on GitHub.

---

## 💡 Future Work

* Switch to **TF‑IDF** or embeddings for richer similarity.
* Add user‑based collaborative filtering.
* Containerise with Docker & add CI/CD.
* Paginated results and trailer previews.

---

## 📜 License

This project is licensed under the MIT License – see `LICENSE` for details.

---

### Credits

* [TMDB](https://www.themoviedb.org/) for the datasets & posters.
* Inspired by countless community tutorials on content‑based filtering.
