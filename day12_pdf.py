import pymupdf


def extract_resume_text(pdf_path):

    document = pymupdf.open(pdf_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text


def extract_skills(text):

    skills_list = [
        "Python",
        "Java",
        "SQL",
        "HTML",
        "CSS",
        "JavaScript",
        "Machine Learning",
        "Git",
        "React",
        "Django"
    ]

    found_skills = []

    for skill in skills_list:

        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills


def calculate_match(resume_skills, job_skills):

    matched = []

    for skill in job_skills:

        if skill.lower() in [s.lower() for s in resume_skills]:
            matched.append(skill)

    missing = []

    for skill in job_skills:

        if skill.lower() not in [s.lower() for s in resume_skills]:
            missing.append(skill)

    score = (len(matched) / len(job_skills)) * 100

    return matched, missing, score


# Read PDF
resume_text = extract_resume_text("resumes/sample_resume.pdf")

# Extract candidate skills
resume_skills = extract_skills(resume_text)

# Company job requirements
job_skills = [
    "Python",
    "SQL",
    "Machine Learning",
    "Git",
    "React"
]

# Compare
matched, missing, score = calculate_match(
    resume_skills,
    job_skills
)

# Display report
print("\n===== AI RESUME ANALYZER =====")

print("Candidate Skills:", resume_skills)

print("Matched Skills:", matched)

print("Missing Skills:", missing)

print("Job Match Score:", round(score, 2), "%")