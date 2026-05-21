from flask import Flask, jsonify

from backend.nlp.skills import SKILLS
from backend.scoring.ats_score import (
    load_text,
    extract_skills,
    calculate_match_score
)

app = Flask(__name__)

# File paths
RESUME_FILE = "data/extracted/extracted_resume.txt"
JOB_DESCRIPTION_FILE = "data/job_descriptions/job_description.txt"


@app.route("/")
def home():
    return jsonify({
        "message": "AI Resume Analyzer API is running"
    })


@app.route("/analyze")
def analyze_resume():

    # Load files
    resume_text = load_text(RESUME_FILE)
    jd_text = load_text(JOB_DESCRIPTION_FILE)

    # Extract skills
    resume_skills = extract_skills(resume_text, SKILLS)
    jd_skills = extract_skills(jd_text, SKILLS)

    # Calculate ATS score
    score, matched_skills = calculate_match_score(
        resume_skills,
        jd_skills
    )

    missing_skills = list(set(jd_skills) - set(resume_skills))

    # JSON response
    result = {
        "ats_score": score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)