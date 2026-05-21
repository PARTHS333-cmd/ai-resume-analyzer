from backend.nlp.skills import SKILLS

# File paths
RESUME_FILE = "data/extracted/extracted_resume.txt"
JOB_DESCRIPTION_FILE = "data/job_descriptions/job_description.txt"


def load_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read().lower()


def extract_skills(text, skills_list):
    detected = []

    for skill in skills_list:
        if skill.lower() in text:
            detected.append(skill)

    return sorted(set(detected))


def calculate_match_score(resume_skills, jd_skills):
    matched_skills = list(set(resume_skills) & set(jd_skills))

    if len(jd_skills) == 0:
        return 0, matched_skills

    score = (len(matched_skills) / len(jd_skills)) * 100

    return round(score, 2), matched_skills


if __name__ == "__main__":

    print("Loading resume and job description...\n")

    resume_text = load_text(RESUME_FILE)
    jd_text = load_text(JOB_DESCRIPTION_FILE)

    resume_skills = extract_skills(resume_text, SKILLS)
    jd_skills = extract_skills(jd_text, SKILLS)

    score, matched_skills = calculate_match_score(
        resume_skills,
        jd_skills
    )

    missing_skills = list(set(jd_skills) - set(resume_skills))

    print("========== ATS MATCH REPORT ==========\n")

    print(f"ATS Match Score: {score}%\n")

    print("Matched Skills:")
    for skill in matched_skills:
        print(f"- {skill}")

    print("\nMissing Skills:")
    for skill in missing_skills:
        print(f"- {skill}")