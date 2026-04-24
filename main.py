from fastapi import FastAPI, UploadFile, File
from services import (
    mindee_service, pdf_service, firecrawl_service, 
    openrouter_service, transformer_service
)
import shutil
import os
import uvicorn

app = FastAPI()

@app.post("/upload_resume")
async def upload_resume(file: UploadFile = File(...)):
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    try:
        # 1. Extract Structured Data + raw_text
        structured = mindee_service.parse_resume_with_mindee(temp_path)
        
        # 2. Extract URLs (GitHub, LinkedIn)
        links = pdf_service.extract_links_from_pdf(temp_path)
        
        # 3. Scrape the first link found (if any)
        web_context = ""
        if links:
            web_context = firecrawl_service.scrape_url(links[0])
            
        # 4. Generate the AI Recruiter Profile
        profile = openrouter_service.generate_recruiter_profile(structured, web_context)
        
        # 5. Return both profile and raw resume text
        raw_text = structured.get("raw_text", "")
        return {"profile": profile, "raw_text": raw_text}
    
    except Exception as e:
        return {"error": str(e)}
    
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

@app.post("/score_resume")
async def score_resume(data: dict):
    # Uses raw_text for scoring instead of AI-generated profile
    text_to_score = data.get('raw_text') or data.get('profile')
    score = transformer_service.calculate_ats_score(text_to_score, data['jd'])
    return {"score": score}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)