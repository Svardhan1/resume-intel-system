import openai
from config import Config

def generate_recruiter_profile(structured_data, scraped_content):
    """Uses an LLM to synthesize a professional recruiter profile."""
    client = openai.OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=Config.OPENROUTER_API_KEY,
    )
    
    prompt = f"""
    You are an expert technical recruiter. 
    Review this Candidate Data: {structured_data}
    Review this Live Web Context: {scraped_content}
    
    Provide a professional summary including:
    - Executive Overview
    - Top 5 High-Level Skills
    - Project Highlights from their web presence
    """
    
    response = client.chat.completions.create(
        model=Config.LLM_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content