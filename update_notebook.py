import json
import os

notebook_path = "recomendation.ipynb"

with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

# Cell 1: Update pip install
nb["cells"][0]["source"] = [
    "!pip install pandas matplotlib numpy scikit-learn\n"
]

# Cell 2: Replace functions
new_cell_2_code = """import ast
import json
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def clean_text(text):
    if pd.isna(text):
        return ""
    return str(text)

def safe_parse_topics(value):
    if pd.isna(value):
        return ""
    if isinstance(value, list):
        return " ".join(value)
    if isinstance(value, str):
        try:
            topics = json.loads(value)
            if isinstance(topics, list):
                return " ".join(topics)
        except (TypeError, json.JSONDecodeError):
            try:
                topics = ast.literal_eval(value)
                if isinstance(topics, list):
                    return " ".join(topics)
            except:
                pass
    return ""

def prepare_data(df):
    # Combine description, language, and topics into a single text feature
    df['description'] = df['description'].apply(clean_text)
    df['language'] = df['language'].apply(clean_text)
    df['topics_str'] = df['topics'].apply(safe_parse_topics)
    
    # We concatenate these fields to create a rich 'tags' column for TF-IDF
    df['tags'] = df['description'] + " " + df['language'] + " " + df['topics_str']
    return df

def build_feature_matrix(df):
    \"\"\"
    REMPLACEMENT: 
    L'approche originale utilisait un vocabulaire manuel et un produit scalaire.
    Ici, nous utilisons TF-IDF (Term Frequency-Inverse Document Frequency).
    Cela permet de pénaliser les termes trop communs (comme 'software', 'tool') 
    et de donner plus de poids aux mots-clés spécifiques.
    \"\"\"
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(df['tags'])
    return vectorizer, tfidf_matrix

def recommend(repository_name, df, feature_matrix, top_n=10):
    \"\"\"
    REMPLACEMENT:
    Utilisation de la Similarité Cosinus au lieu du produit scalaire brut.
    Le produit scalaire favorisait les films avec beaucoup d'acteurs/équipes (vecteurs non normalisés).
    La similarité Cosinus normalise les vecteurs, assurant des scores entre 0 et 1.
    \"\"\"
    if repository_name not in df["repository_name"].values:
        raise ValueError(f"Repository '{repository_name}' not found in the dataset.")

    idx = df.index[df["repository_name"] == repository_name][0]
    
    # Calculate cosine similarity between this repository and all others
    cosine_similarities = cosine_similarity(feature_matrix[idx], feature_matrix).flatten()
    
    # Exclude the repository itself (-1 ensures it will be at the bottom)
    cosine_similarities[idx] = -1
    
    # Get top_n most similar indices
    top_indices = np.argsort(cosine_similarities)[::-1][:top_n]
    
    recommended = df.iloc[top_indices][["repository_name", "owner", "language", "stars"]].copy()
    recommended["similarity_score"] = cosine_similarities[top_indices]
    
    return recommended.reset_index(drop=True)
"""
nb["cells"][1]["source"] = [line + "\n" for line in new_cell_2_code.split("\n")]

# Cell 3: Update Execution Example
new_cell_3_code = """df = pd.read_csv("data/github_repositories.csv")
df = prepare_data(df)
vectorizer, feature_matrix = build_feature_matrix(df)

# Example Recommendation
try:
    example_repo = df['repository_name'].iloc[0]
    print(f"Recommendations for: {example_repo}")
    recommended = recommend(example_repo, df, feature_matrix, top_n=10)
    display(recommended)
except Exception as e:
    print("Error:", e)
"""
nb["cells"][2]["source"] = [line + "\n" for line in new_cell_3_code.split("\n")]

with open(notebook_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1)

print("Notebook updated successfully.")
