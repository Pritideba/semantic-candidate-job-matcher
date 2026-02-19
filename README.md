# Semantic Candidate–Job Matching Engine

An AI-powered backend service that performs semantic matching between candidate profiles and job descriptions using sentence embeddings and vector similarity search.

This system intelligently matches candidates and jobs even when wording differs by understanding meaning rather than relying on keyword matching.

---

## 🚀 Features

- Create candidate profiles  
- Create job descriptions  
- Generate sentence embeddings using HuggingFace  
- Store vectors using FAISS  
- Semantic similarity search (cosine similarity)  
- Rank candidates by similarity + experience  
- Explanation endpoint  
- Minimum experience filtering  
- Caching layer  
- SQLite database persistence  
- Dockerized deployment  

---

## 🧠 Tech Stack

- Python 3.10  
- FastAPI  
- SentenceTransformers (HuggingFace)  
- FAISS  
- SQLite + SQLAlchemy  
- Docker  

---

## 📂 Project Structure

semantic-matcher/
│
├── app/
│ ├── main.py
│ ├── api/
│ │ ├── candidates.py
│ │ └── jobs.py
│ ├── services/
│ │ ├── embedding_service.py
│ │ ├── matching_service.py
│ │ ├── explanation_service.py
│ │ └── cache.py
│ ├── db/
│ │ ├── database.py
│ │ └── tables.py
│ ├── models/
│ │ └── entities.py
│ └── schemas/
│ └── schemas.py
│
├── Dockerfile
├── README.md
└── requirements.txt


---

## ⚙️ How It Works

1. Convert text into embeddings  
2. Store embeddings in FAISS  
3. Perform cosine similarity search  
4. Rank by similarity score and experience  

---

## 🧪 API Endpoints

### Create Candidate
POST `/candidates`
{
  "name": "Rahul",
  "skill_description": "Registered nurse with ICU experience and German A2",
  "experience": 4,
  "location": "India"
}


### Create Job
POST `/jobs`
{
  "title": "ICU Nurse",
  "country": "Germany",
  "description": "Looking for ICU nurse with basic German"
}


Match Candidates
GET /jobs/{job_id}/match?min_experience=3

Explanation
GET /jobs/{job_id}/explain/{candidate_id}


▶️ Run Without Docker
cd semantic-matcher
venv\Scripts\activate
uvicorn app.main:app --reload

Open browser:
http://127.0.0.1:8000/docs


🐳 Run With Docker
docker build -t semantic-matcher .
docker run -p 8000:8000 semantic-matcher

Open browser:
http://127.0.0.1:8000/docs


📈 Example Results
| Case               | Similarity   |
| ------------------ | ------------ |
| ICU Nurse + German | High (>0.75) |
| General Nurse      | Medium       |
| Electrician        | Low          |


🔮 Future Improvements
Persistent vector database
Authentication
Frontend UI
Cloud deployment


👨‍💻 Author
Developed by: Pritideba Patra

---

# ✅ AFTER PASTING
1. Press **CTRL + S**
2. Close file
