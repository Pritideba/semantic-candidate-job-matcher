from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db.database import Base

class CandidateTable(Base):
    __tablename__ = "candidates"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    skill_description = Column(String)
    experience = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

class JobTable(Base):
    __tablename__ = "jobs"

    id = Column(String, primary_key=True, index=True)
    title = Column(String)
    country = Column(String)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
