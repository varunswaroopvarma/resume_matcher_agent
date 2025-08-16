import PyPDF2
import re

STOPWORDS = {
    'the', 'and', 'a', 'an', 'to', 'is', 'in', 'of', 'for', 'on', 'with',
    'as', 'by', 'from', 'at', 'it', 'be', 'that', 'this', 'are', 'was',
    'were', 'or', 'but', 'if', 'their', 'has', 'have', 'had', 'will', 'can',
    'not', 'so', 'do', 'we', 'you', 'they', 'he', 'she', 'him', 'her', 'i',
    'my', 'your', 'our', 'us', 'all', 'also', 'about', 'any', 'which', 'when',
    'what', 'who', 'how', 'will', 'would', 'should', 'could', 'may', 'might',
    'must', 'shall', 'been', 'because', 'there', 'these', 'those', 'than',
    'then', 'such', 'most', 'some'
}

def extract_text_from_pdf(file_stream):
    text = ""
    reader = PyPDF2.PdfReader(file_stream)
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def extract_keywords(text):
    # Convert to lowercase and remove punctuation
    text = re.sub(r'[^\w\s]', '', text.lower())
    words = set(text.split())

    # Filter stopwords and words shorter than 3 characters
    keywords = {word for word in words if word not in STOPWORDS and len(word) > 2}

    # Remove numeric-only words
    keywords = {word for word in keywords if not word.isdigit()}

    return keywords
