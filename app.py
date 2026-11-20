# 



import streamlit as st
import pymupdf
import re

# -------------------------
# PAGE CONFIGURATION
# -------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.write("Analyze your resume and discover how well it matches a job.")

st.divider()

# -------------------------
# SKILL DATABASE
# -------------------------

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
    "Django",
    "C++",
    "Spring Boot",
    "FastAPI",
    "Flask",
    "AWS",
    "Docker",
    "MongoDB"
]

# -------------------------
# PDF EXTRACTION
# -------------------------

def extract_resume_text(uploaded_file):

    document = pymupdf.open(
        stream=uploaded_file.getvalue(),
        filetype="pdf"
    )

    full_text = ""

    for page in document:
        full_text += page.get_text()

    document.close()

    return full_text


# -------------------------
# EMAIL EXTRACTION
# -------------------------

def extract_email(text):

    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    result = re.search(pattern, text)

    if result:
        return result.group()

    return "Not found"


# -------------------------
# PHONE EXTRACTION
# -------------------------

def extract_phone(text):

    pattern = r"\b\d{10}\b"

    result = re.search(pattern, text)

    if result:
        return result.group()

    return "Not found"


# -------------------------
# SKILL EXTRACTION
# -------------------------

def extract_skills(text):

    found_skills = []

    for skill in skills_list:

        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, text, re.IGNORECASE):
            found_skills.append(skill)

    return found_skills


# -------------------------
# JOB MATCHING
# -------------------------

def calculate_match(resume_skills, job_skills):

    resume_set = {s.lower() for s in resume_skills}
    job_set = {s.lower() for s in job_skills}

    matched = [
        skill for skill in job_skills
        if skill.lower() in resume_set
    ]

    missing = [
        skill for skill in job_skills
        if skill.lower() not in resume_set
    ]

    if not job_skills:
        return matched, missing, 0

    score = len(matched) / len(job_skills) * 100

    return matched, missing, score

# -------------------------
# RESUME FEEDBACK ENGINE
# -------------------------

def generate_feedback(resume_text, resume_skills, missing, score):

    feedback = []

    text = resume_text.lower()

    # Check whether projects are mentioned
    if "project" not in text:

        feedback.append(
            "Add a Projects section to demonstrate your practical knowledge."
        )

    # Check whether experience is mentioned
    if "experience" not in text:

        feedback.append(
            "Add relevant internship, work or practical experience if available."
        )

    # Check missing job skills
    for skill in missing:

        feedback.append(
            f"Consider learning and demonstrating {skill} through a practical project."
        )

    # Check resume skills
    if len(resume_skills) < 3:

        feedback.append(
            "Add relevant technical skills that you genuinely know."
        )

    # Check job match score
    if score < 50:

        feedback.append(
            "Review the job requirements and improve the relevance of your resume."
        )

    elif score >= 80:

        feedback.append(
            "Your detected skills match many job requirements. Highlight them clearly."
        )

    # General suggestion
    feedback.append(
        "Use clear bullet points and include measurable achievements wherever possible."
    )

    return feedback


# -------------------------
# USER INPUT
# -------------------------

col1, col2 = st.columns(2)

with col1:
    st.subheader("Upload Resume")

    uploaded_file = st.file_uploader(
        "Choose your PDF resume",
        type=["pdf"]
    )

with col2:
    st.subheader("Job Description")

    job_description = st.text_area(
        "Paste job requirements",
        height=180
    )


# -------------------------
# ANALYSIS
# -------------------------

if st.button("Analyze My Resume", type="primary"):

    if uploaded_file is None:
        st.error("Please upload a PDF resume.")

    elif not job_description.strip():
        st.error("Please enter a job description.")

    else:

        try:

            resume_text = extract_resume_text(uploaded_file)

            if not resume_text.strip():

                st.warning("No readable text found in this PDF.")

            else:

                # Extract information
                email = extract_email(resume_text)
                phone = extract_phone(resume_text)

                resume_skills = extract_skills(resume_text)
                job_skills = extract_skills(job_description)

                # Calculate matching score
                matched, missing, score = calculate_match(
                    resume_skills,
                    job_skills
                )

                st.divider()

                st.header("📊 Analysis Dashboard")

                # Candidate information
                st.subheader("Candidate Information")

                info1, info2 = st.columns(2)

                info1.metric("Email", email)
                info2.metric("Phone", phone)

                # Match score
                st.subheader("Job Match Score")

                if job_skills:

                    st.metric(
                        "Resume Match",
                        f"{score:.2f}%"
                    )

                    st.progress(score / 100)

                else:

                    st.warning(
                        "No recognized technical skills found in the job description."
                    )

                # Skills analysis
                st.subheader("Skills Analysis")

                left, right = st.columns(2)

                with left:

                    st.markdown("### ✅ Matching Skills")

                    if matched:
                        for skill in matched:
                            st.success(skill)
                    else:
                        st.info("No matching skills found.")

                with right:

                    st.markdown("### 📚 Skills to Develop")

                    if missing:
                        for skill in missing:
                            st.warning(skill)
                    else:
                        st.success("All detected job skills matched!")

                # Strengths
                st.subheader("Candidate Strengths")

                if matched:

                    st.write(
                        "Your resume demonstrates these job-relevant skills:"
                    )

                    st.write(", ".join(matched))

                else:

                    st.write(
                        "Add relevant technical skills and projects to your resume where accurate."
                    )

                # Recommendations
                st.subheader("Recommendations")

                if missing:

                    for skill in missing:
                        st.write(
                            f"• Consider learning or demonstrating {skill} through a project."
                        )

                else:

                    st.write(
                        "Your resume contains all the skills detected in this job description. Review your projects and experience for relevance too."
                    )

# -------------------------
# PERSONALIZED FEEDBACK
# -------------------------

st.divider()

st.header("🤖 Resume Improvement Feedback")

feedback = generate_feedback(
    resume_text,
    resume_skills,
    missing,
    score
)

for suggestion in feedback:

    st.info(suggestion)

                # Download report
                report = f"""
AI RESUME ANALYSIS REPORT

Email: {email}
Phone: {phone}

Candidate Skills:
{', '.join(resume_skills)}

Required Job Skills:
{', '.join(job_skills)}

Matching Skills:
{', '.join(matched)}

Missing Skills:
{', '.join(missing)}

Job Match Score: {score:.2f}%
"""

                st.divider()

                st.subheader("Download Your Report")

                st.download_button(
                    label="Download Analysis Report",
                    data=report,
                    file_name="resume_analysis.txt",
                    mime="text/plain"
                )

        except Exception as error:

            st.error(f"Analysis failed: {error}")
