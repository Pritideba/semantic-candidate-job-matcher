from pydantic import BaseModel

class CandidateCreate(BaseModel):
    name: str
    skill_description: str
    experience: int
    location: str

class JobCreate(BaseModel):
    title: str
    country: str
    description: str
