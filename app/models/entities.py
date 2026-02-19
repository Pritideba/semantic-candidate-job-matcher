from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class Candidate:
    id: str
    name: str
    skill_description: str
    experience: int
    embedding: List[float]
    created_at: datetime
