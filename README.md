# 🤖 Resume Intelligence System

An AI-powered resume analysis tool that parses resumes, generates recruiter-ready profiles, and calculates ATS match scores against job descriptions.

## ✨ Features

- 📄 **Resume Parsing** — Extracts text, name, email, and skills from PDF resumes using PyMuPDF
- 🤖 **AI Profile Generation** — Generates a professional recruiter-ready summary using Gemini 2.0 Flash via OpenRouter
- 🌐 **Web Scraping** — Scrapes LinkedIn/GitHub links found in the resume using Firecrawl
- 🎯 **ATS Score Matcher** — Calculates semantic + keyword match percentage between resume and job description
- 📊 **Visual Gauge** — Displays ATS score as an interactive gauge chart

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | FastAPI |
| PDF Parsing | PyMuPDF |
| AI Profile | OpenRouter (Gemini 2.0 Flash) |
| Web Scraping | Firecrawl |
| ATS Scoring | Sentence Transformers + scikit-learn |
| Visualization | Plotly |

## 📁 Project Structure
resume_intel_system/
├── services/
│   ├── __init__.py
│   ├── mindee_service.py       # PDF text extraction (PyMuPDF)
│   ├── pdf_service.py          # Link extraction from PDF
│   ├── firecrawl_service.py    # Web scraping via Firecrawl
│   ├── openrouter_service.py   # AI profile generation
│   └── transformer_service.py  # Hybrid ATS scoring
├── utils/                      # Utility helpers
├── venv/                       # Virtual environment (not pushed)
├── app_ui.py                   # Streamlit frontend
├── config.py                   # API key configuration
├── main.py                     # FastAPI backend
├── requirements.txt            # Python dependencies
├── .env                        # API keys (not pushed)
├── .env.example                # API keys template
└── .gitignore
## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/resume-intel-system.git
cd resume-intel-system
```

### 2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Keys
Rename `.env.example` to `.env` and fill in your API keys:

Get your API keys from:
- 🔑 OpenRouter: [openrouter.ai](https://openrouter.ai)
- 🔑 Firecrawl: [firecrawl.dev](https://firecrawl.dev)
- 🔑 Mindee: [platform.mindee.com](https://platform.mindee.com)

## 🚀 Running the App

You need **two terminals** running simultaneously:

**Terminal 1 — Start the backend:**
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 — Start the frontend:**
```bash
streamlit run app_ui.py
```

Then open your browser at **http://localhost:8501**

## 📖 How to Use

1. Go to the **Candidate Analysis** tab
2. Upload a resume PDF and click **Analyze Resume**
3. Wait for the AI to generate a recruiter-ready profile
4. Switch to the **ATS Matcher** tab
5. Paste a job description and click **Calculate ATS Score**
6. View the match percentage on the gauge chart

## 📊 ATS Scoring Method

The ATS score is calculated using a **hybrid approach:**
- **60%** Semantic similarity using `all-MiniLM-L6-v2` sentence transformer
- **40%** Direct keyword overlap between resume and job description

| Score | Result |
|---|---|
| 0 - 40% | 🔴 Poor Match |
| 40 - 75% | 🟠 Moderate Match |
| 75 - 100% | 🟢 Strong Match |

## 📦 Requirements
fastapi
uvicorn
streamlit
pymupdf
firecrawl-py
openai
sentence-transformers
scikit-learn
plotly
python-multipart
python-dotenv
