from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import re

model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_keywords(text):
    """Extract individual words, lowercased."""
    return set(re.findall(r'\b[a-zA-Z][a-zA-Z+#.-]{1,}\b', text.lower()))

def calculate_ats_score(profile_text, job_description):
    """Hybrid: 60% semantic similarity + 40% keyword overlap."""
    
    # 1. Semantic similarity (existing logic)
    embeddings = model.encode([profile_text, job_description])
    semantic_score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    
    # 2. Keyword overlap score
    profile_keywords = extract_keywords(profile_text)
    jd_keywords = extract_keywords(job_description)
    
    if len(jd_keywords) == 0:
        keyword_score = 0
    else:
        matched = profile_keywords.intersection(jd_keywords)
        keyword_score = len(matched) / len(jd_keywords)
    
    # 3. Weighted hybrid
    final_score = (semantic_score * 0.6) + (keyword_score * 0.4)
    return round(float(final_score) * 100, 2)