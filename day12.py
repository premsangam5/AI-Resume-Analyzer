# Candidate skills
resume_skills = [
    "Python",
    "Java",
    "SQL",
    "Git"
]

# Company required skills
job_skills = [
    "Python",
    "SQL",
    "Machine Learning",
    "Git",
    "React"
]

# Find matching skills
matched_skills = []

for skill in job_skills:

    if skill.lower() in [s.lower() for s in resume_skills]:

        matched_skills.append(skill)

# Find missing skills
missing_skills = []

for skill in job_skills:

    if skill.lower() not in [s.lower() for s in resume_skills]:

        missing_skills.append(skill)

# Calculate score
total_skills = len(job_skills)

match_score = (len(matched_skills) / total_skills) * 100

# Display report
print("===== JOB MATCH REPORT =====")

print("Matched Skills:", matched_skills)

print("Missing Skills:", missing_skills)

print("Match Score:", match_score, "%")
