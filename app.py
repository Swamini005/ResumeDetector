from flask import Flask, render_template, jsonify, make_response
from flask_restful import Api, Resource, reqparse
import os
import pdfplumber
from docx import Document
import spacy

app = Flask(__name__)
api = Api(app)

# English language model
nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

def extract_text_from_docx(file_path):
    doc = Document(file_path)
    return " ".join([paragraph.text for paragraph in doc.paragraphs])

def is_resume(file_path, content):
    if file_path is None:
        raise ValueError("File path is missing or None.")

    # file extension
    file_extension = os.path.splitext(file_path)[1].lower()

    if file_extension == '.pdf':
        text_content = extract_text_from_pdf(file_path)
    elif file_extension in ['.doc', '.docx']:
        text_content = extract_text_from_docx(file_path)
    elif file_extension in ['.txt']:
        text_content = content
    else:
        raise ValueError(f"Unsupported file type: {file_extension}")

    doc = nlp(text_content)

    # Extract named entities
    entities = [ent.text.lower() for ent in doc.ents]

    # resume keywords
    resume_keywords = ["education", "experience", "skills"]
    has_resume_info = any(keyword.lower() in entities for keyword in resume_keywords)

    return has_resume_info

class ResumeUploadResource(Resource):
    @staticmethod
    def post():
        try:
            parser = reqparse.RequestParser()
            parser.add_argument("file", type=str, default=None)  # Assume default value is None
            args = parser.parse_args()

            file_path = args["file"]
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            is_resume_flag = is_resume(file_path, content)

            result = {"is_resume": is_resume_flag}

            return make_response(jsonify(result), 200)

        except Exception as e:
            print(f"Error: {e}")
            return make_response(jsonify({"message": "This is not a resume"}), 500)

api.add_resource(ResumeUploadResource, "/upload")

@app.route("/")
def upload_form():
    return render_template("template.html")

if __name__ == "__main__":
    app.run(debug=True)
