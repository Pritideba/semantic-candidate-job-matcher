from app.db.vector_store import search_candidates, candidate_ids
from app.api.candidates import candidates

from app.services.cache import get_cache, set_cache

def match_candidates(job_embedding, min_experience=0):
    
    # -------- CACHE CHECK --------
    cache_key = str(job_embedding[:5]) + str(min_experience)

    cached = get_cache(cache_key)
    if cached:
        print("Returning cached result")
        return cached
    # -----------------------------

    scores, indices = search_candidates(job_embedding)
    results = []

    for score, idx in zip(scores, indices):
        if idx == -1:
            continue

        candidate_id = candidate_ids[idx]
        candidate = candidates[candidate_id]

        if candidate.experience < min_experience:
            continue

        results.append({
            "candidateId": candidate.id,
            "similarityScore": float(score),
            "experience": candidate.experience
        })

    results.sort(key=lambda x: (x["similarityScore"], x["experience"]), reverse=True)

    # -------- SAVE TO CACHE --------
    set_cache(cache_key, results)
    # -------------------------------

    return results
