'''import pymupdf

pdf_path = "resumes/sample_resume.pdf"

document = pymupdf.open(pdf_path)

for page in document:
    text = page.get_text()
    print(text)

document.close()'''



import pymupdf

def extract_resume_text(pdf_path):

    document = pymupdf.open(pdf_path)

    full_text = ""

    for page in document:
        full_text += page.get_text()

    document.close()

    return full_text


resume_text = extract_resume_text("resumes/sample_resume.pdf")

print("===== EXTRACTED RESUME =====")
print(resume_text)
