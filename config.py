import os
from dotenv import load_dotenv

# This searches for the .env file and loads the keys
load_dotenv()

class Config:
    MINDEE_API_KEY = os.getenv("MINDEE_API_KEY")
    FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    
    # Using Gemini 2.0 Flash via OpenRouter
    LLM_MODEL = "google/gemini-2.0-flash-001"