from sentence_transformers import SentenceTransformer
import numpy as np

# Load model once when app starts
model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embedding(text: str):
    """
    Convert text into embedding vector
    """
    embedding = model.encode(text, normalize_embeddings=True)
    return embedding.astype("float32")
