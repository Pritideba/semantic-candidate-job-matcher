from fastapi import FastAPI
from app.api import candidates, jobs
from app.db.database import engine
from app.db.tables import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(candidates.router, prefix="/candidates")
app.include_router(jobs.router, prefix="/jobs")
