from flask import Flask, request, render_template
from flask_cors import CORS
from utils import extract_text_from_pdf, extract_keywords
from matcher import get_similarity
import os

app = Flask(__name__)
CORS(app)  # enable CORS
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB upload limit

@app.route('/', methods=['GET', 'POST'])
def index():
    similarity = None
    missing_keywords = None
    error_message = None

    if request.method == 'POST':
        try:
            job_text = request.form.get('job', '')
            resume_file = request.files.get('resume')
            
            if not job_text:
                error_message = "Please enter the job description."
            elif not resume_file:
                error_message = "Please upload a resume."
            else:
                resume_text = extract_text_from_pdf(resume_file)
                raw_sim = get_similarity(resume_text, job_text)
                similarity = round(raw_sim * 100, 2)

                job_keywords = extract_keywords(job_text)
                resume_keywords = extract_keywords(resume_text)
                missing_keywords = sorted(list(job_keywords - resume_keywords))[:50]
        except Exception as e:
            error_message = f"Error processing request: {e}"

    return render_template(
        'index.html',
        similarity=similarity,
        missing_keywords=missing_keywords,
        error_message=error_message
    )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
