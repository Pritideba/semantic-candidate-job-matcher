def generate_explanation(candidate, job_description, similarity_score):
    explanation = f"""
Candidate '{candidate.name}' is a good match because:

• Candidate skills: {candidate.skill_description}
• Job requires: {job_description}

The system detected strong semantic similarity between these texts.
Similarity score: {round(similarity_score, 2)}

Additionally, candidate has {candidate.experience} years of experience.
"""
    return explanation.strip()
