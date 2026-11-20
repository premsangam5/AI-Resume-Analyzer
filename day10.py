'''import re

text = "My email is prem@gmail.com"

email = re.search(r"\S+@\S+\.\S+", text)

if email:
    print(email.group())
    '''


import re

resume_text = """
Prem Sangam
Email: prem@gmail.com
Phone: 9876543210
Education: B.Tech ECE
Skills: Python, Java, SQL, Git
"""

# email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

# email = re.search(email_pattern, resume_text)

# if email:
#     print("Email:", email.group())
# else:
#     print("Email not found")

# phone_pattern = r"\b\d{10}\b"

# phone = re.search(phone_pattern, resume_text)

# if phone:
#     print("Phone:", phone.group())
# else:
#     print("Phone not found")

import re

resume_text = """
Prem Sangam
Email: prem@gmail.com
Phone: 9876543210
Education: B.Tech ECE
Skills: Python, Java, SQL, Git
"""

# Extract email
email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
email = re.search(email_pattern, resume_text)

# Extract phone
phone_pattern = r"\b\d{10}\b"
phone = re.search(phone_pattern, resume_text)

# Extract skills
skills_list = [
    "Python", "Java", "SQL", "HTML",
    "CSS", "JavaScript", "Machine Learning", "Git"
]

found_skills = []

for skill in skills_list:
    if skill.lower() in resume_text.lower():
        found_skills.append(skill)

# Display results
print("===== RESUME ANALYSIS =====")

print("Email:", email.group() if email else "Not found")
print("Phone:", phone.group() if phone else "Not found")
print("Skills:", found_skills)