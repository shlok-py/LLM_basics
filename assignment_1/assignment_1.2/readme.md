# 📊 Word Embedding Explorer

An interactive and educational **Flask-based web app** and **REST API** for visualizing and exploring **word embeddings**. Built for Assignment 1.2, this project demonstrates the use of **TF-IDF** and **GloVe** embeddings along with **PCA visualization** and **nearest neighbor retrieval**.

---

## 🚀 Features

✅ GloVe + fallback to TF-IDF vector embeddings
✅ REST API to get embeddings & nearest neighbors
✅ PCA-based 2D visualization using Matplotlib
✅ Interactive UI using Bootstrap
✅ Educational comparison of semantic word distances

---

## 🏗️ Project Structure

```
assignment_1/assignment_1.2
├── main.py                      # Flask app & API routes
├── processor/
|   ├── __init__.py
│   ├── embeddings_loader.py     # Embedding engine (GloVe + TF-IDF)
│   ├── visualizer.py            # PCA/t-SNE reduction and plotting
├── static/
│   └── plot.png                # Generated visualization image
├── templates/
│   └── embedding_ui.html       # Web app UI
└── models/
    └── glove.6B.100d.txt       # Download if not available from (https://nlp.stanford.edu/projects/glove/)
└── README.md
```

---

## 🛠️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/shlokkoirala/LLM_basics.git
cd LLM_basics/assignment_1/assignment_1.2
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Download GloVe (100D)

```bash
# Download from:
https://nlp.stanford.edu/projects/glove/

# Extract and place this file in the models folder:
glove.6B.100d.txt
```

### 4. Run the App

```bash
python main.py
```

Open your browser: `http://127.0.0.1:5000`

---

## 📥 API Endpoint

### `POST /embedding`

```json
{
  "word": "learning"
}
```

**Response:**

* GloVe/TF-IDF vector for input word
* Nearest neighbor words
* Path to 2D plot image of semantic space

---

## 🖼️ Web UI Preview

### Enter a word and see:

* Embedding vector
* Nearest neighbor words
* PCA visualization of their relationships

![Demo Screenshot](images/embedding_demo.png)

---

## 📘 Educational Use

This app demonstrates:

* Semantic relationships in vector space
* Dimensionality reduction (PCA)
* Interactive NLP visualization
* RESTful NLP microservices using Python

---

## 💡 Example Nearest Neighbors

Input: `intelligence`

```json
[
  ["learning", 0.87],
  ["artificial", 0.82],
  ["machine", 0.79]
]
```

---

## 👨‍💻 Author

Made with ❤️ by **Shlok Koirala** for Assignment 1.2 of AICL 434 LLM
Feel free to fork, improve, and learn!

---
