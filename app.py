from flask import Flask, request, render_template
from utils import extract_text_from_pdf, extract_words
from matcher import get_similarity

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    similarity = None
    missing_keywords = None

    if request.method == 'POST':
        job_text = request.form.get('job', '')
        resume_file = request.files.get('resume')
        if resume_file:
            resume_text = extract_text_from_pdf(resume_file)
            raw_sim = get_similarity(resume_text, job_text)
            similarity = round(raw_sim * 100, 2)

            job_keywords = extract_words(job_text)
            resume_keywords = extract_words(resume_text)
            missing_keywords = sorted(list(job_keywords - resume_keywords))

    return render_template('index.html',
                           similarity=similarity,
                           missing_keywords=missing_keywords)

if __name__ == '__main__':
    app.run(debug=True)
