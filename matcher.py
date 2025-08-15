# matcher.py
from sentence_transformers import SentenceTransformer, util

MODEL_NAME = 'all-MiniLM-L6-v2'
model = SentenceTransformer(MODEL_NAME)

def get_embedding(text):
    return model.encode(text, convert_to_tensor=True)

def get_similarity(resume_text, job_text):
    embed1 = get_embedding(resume_text)
    embed2 = get_embedding(job_text)
    similarity = util.cos_sim(embed1, embed2)
    return float(similarity)
