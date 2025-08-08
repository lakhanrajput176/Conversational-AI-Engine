
import os
import json
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Demo app showing how ChatGPT API could be called for conversational screening.
# NOTE: This app contains placeholders. Do NOT expose real API keys in public repos.
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

app = Flask(__name__)

# Load dummy resumes
with open("data/dummy_resumes.json") as f:
    DUMMY_RESUMES = json.load(f)

# Simple scoring logic (demo)
def score_candidate(skills_required, candidate_skills):
    matched = set(skills_required).intersection(set(candidate_skills))
    score = int(len(matched) / max(1, len(skills_required)) * 100)
    return score, list(matched)

@app.route("/candidates", methods=["GET"])
def list_candidates():
    return jsonify(DUMMY_RESUMES)

@app.route("/screen", methods=["POST"])
def screen_candidate():
    # Expected JSON:
    # {
    #   "candidate_id": 1,
    #   "job_criteria": {"skills": ["python","azure","nlp"], "min_experience": 2}
    # }
    payload = request.json or {}
    cid = payload.get("candidate_id")
    criteria = payload.get("job_criteria", {})
    skills_required = [s.lower() for s in criteria.get("skills", [])]

    candidate = next((c for c in DUMMY_RESUMES if c["id"] == cid), None)
    if not candidate:
        return jsonify({"error": "candidate not found"}), 404

    candidate_skills = [s.lower() for s in candidate.get("skills", [])]
    score, matched = score_candidate(skills_required, candidate_skills)
    recommendation = "Proceed" if score >= 60 else "Further review"
    result = {
        "candidate_name": candidate["name"],
        "skills": candidate["skills"],
        "score": score,
        "matched_skills": matched,
        "recommendation": recommendation
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
