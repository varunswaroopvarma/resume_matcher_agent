import PyPDF2
import re

def extract_text_from_pdf(file_stream):
    text = ""
    reader = PyPDF2.PdfReader(file_stream)
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def extract_words(text):
    # Lowercase and remove punctuation/special characters
    text = re.sub(r'[^\w\s]', '', text.lower())
    words = set(text.split())

    # Common stopwords to ignore
    stopwords = {
        'the', 'and', 'a', 'an', 'to', 'is', 'in', 'of', 'for', 'on', 'with',
        'as', 'by', 'from', 'at', 'it', 'be', 'that', 'this', 'are', 'was',
        'were', 'or', 'but', 'if', 'their', 'has', 'have', 'had', 'will', 'can',
        'not', 'so', 'do', 'we', 'you', 'they', 'he', 'she', 'him', 'her', 'i',
        'my', 'your', 'our', 'us'
    }

    filtered_words = {word for word in words if word not in stopwords and len(word) > 2}
    return filtered_words
