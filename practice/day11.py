import pymupdf
import re


# STEP 1: Extract text from PDF

def extract_resume_text(pdf_path):

    document = pymupdf.open(pdf_path)

    full_text = ""

    for page in document:
        full_text += page.get_text()

    document.close()

    return full_text


# STEP 2: Extract email

def extract_email(text):

    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    email = re.search(pattern, text)

    if email:
        return email.group()

    return "Not found"


# STEP 3: Extract phone number

def extract_phone(text):

    pattern = r"\b\d{10}\b"

    phone = re.search(pattern, text)

    if phone:
        return phone.group()

    return "Not found"


# STEP 4: Extract skills

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


# STEP 5: Analyze resume

pdf_path = "resumes/sample_resume.pdf"

resume_text = extract_resume_text(pdf_path)

email = extract_email(resume_text)

phone = extract_phone(resume_text)

skills = extract_skills(resume_text)


# STEP 6: Display report

print("\n===== AI RESUME ANALYZER =====")

print("Email:", email)

print("Phone:", phone)

print("Skills:", skills)

print("\n===== ANALYSIS COMPLETE =====")
