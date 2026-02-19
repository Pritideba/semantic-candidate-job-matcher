import faiss
import numpy as np

# Dimension of embedding
DIMENSION = 384

# FAISS index for candidates
candidate_index = faiss.IndexFlatIP(DIMENSION)

# Memory stores
candidate_ids = []
candidate_metadata = {}

def add_candidate(candidate_id: str, embedding):
    candidate_index.add(np.array([embedding]))
    candidate_ids.append(candidate_id)

def search_candidates(job_embedding, top_k=5):
    scores, indices = candidate_index.search(
        np.array([job_embedding]), top_k
    )
    return scores[0], indices[0]
