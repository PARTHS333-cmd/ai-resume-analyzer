from skills import SKILLS

# Path to extracted resume text
TEXT_FILE = "data/extracted/extracted_resume.txt"


def load_resume_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read().lower()


def extract_skills(text, skills_list):
    found_skills = []

    for skill in skills_list:
        if skill.lower() in text:
            found_skills.append(skill)

    return sorted(set(found_skills))


if __name__ == "__main__":
    print("Loading extracted resume text...")

    resume_text = load_resume_text(TEXT_FILE)

    detected_skills = extract_skills(resume_text, SKILLS)

    print("\nDetected Skills:\n")

    for skill in detected_skills:
        print(f"- {skill}")