import fitz  # PyMuPDF
import re

def parse_resume_with_mindee(file_path):
    """Extracts resume text using PyMuPDF - no Mindee API needed."""
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()

    # Extract email
    email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    email = email_match.group(0) if email_match else "N/A"

    # First non-empty line is usually the candidate's name
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    name = lines[0] if lines else "Unknown"

    return {
        "name": name,
        "email": email,
        "skills": [],
        "experience": [],
        "raw_text": text  # Full resume text sent to the LLM
    }