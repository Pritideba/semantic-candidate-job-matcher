from fastapi import APIRouter
from app.schemas.schemas import JobCreate
from app.services.embedding_service import generate_embedding
from app.services.matching_service import match_candidates
from app.services.explanation_service import generate_explanation
from app.api.candidates import candidates

from app.db.database import SessionLocal
from app.db.tables import JobTable

import uuid

router = APIRouter()

# In-memory storage for runtime use
jobs = {}

# ---------------- CREATE JOB ----------------

@router.post("/")
def create_job(data: JobCreate):

    # Generate job id
    jid = str(uuid.uuid4())

    # Generate embedding
    embedding = generate_embedding(data.description)

    # Store in memory
    jobs[jid] = {
        "embedding": embedding,
        "description": data.description
    }

    # -------- SAVE TO SQLITE DATABASE --------
    db = SessionLocal()

    db_job = JobTable(
        id=jid,
        title=data.title,
        country=data.country,
        description=data.description
    )

    db.add(db_job)
    db.commit()
    db.close()
    # -----------------------------------------

    return {
        "id": jid,
        "message": "Job created and saved to database"
    }

# ---------------- MATCH JOB ----------------

@router.get("/{job_id}/match")
def match(job_id: str, min_experience: int = 0):
    return match_candidates(jobs[job_id]["embedding"], min_experience)

# ------------- EXPLANATION ENDPOINT -------------

@router.get("/{job_id}/explain/{candidate_id}")
def explain(job_id: str, candidate_id: str):

    job = jobs[job_id]
    candidate = candidates[candidate_id]

    matches = match_candidates(job["embedding"])
    match = next(m for m in matches if m["candidateId"] == candidate_id)

    explanation = generate_explanation(
        candidate,
        job["description"],
        match["similarityScore"]
    )

    return {
        "explanation": explanation
    }
