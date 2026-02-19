from fastapi import APIRouter
from app.schemas.schemas import CandidateCreate
from app.services.embedding_service import generate_embedding
from app.db.vector_store import add_candidate
from app.models.entities import Candidate

from app.db.database import SessionLocal
from app.db.tables import CandidateTable

import uuid
from datetime import datetime

router = APIRouter()

# In-memory storage (for embeddings & runtime use)
candidates = {}

@router.post("/")
def create_candidate(data: CandidateCreate):
    # Generate unique ID
    cid = str(uuid.uuid4())

    # Generate embedding
    embedding = generate_embedding(data.skill_description)

    # Create in-memory object
    candidate = Candidate(
        id=cid,
        name=data.name,
        skill_description=data.skill_description,
        experience=data.experience,
        embedding=embedding,
        created_at=datetime.utcnow()
    )

    # Store in memory
    candidates[cid] = candidate

    # Add vector to FAISS
    add_candidate(cid, embedding)

    # -------- SAVE TO SQLITE DATABASE --------
    db = SessionLocal()

    db_candidate = CandidateTable(
        id=cid,
        name=data.name,
        skill_description=data.skill_description,
        experience=data.experience
    )

    db.add(db_candidate)
    db.commit()
    db.close()
    # -----------------------------------------

    return {
        "id": cid,
        "message": "Candidate created and saved to database"
    }
