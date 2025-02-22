NLP Minor Project (Group 17)
Keyword Extraction from Research Papers
This project implements a Keyword Extraction system using TF-IDF to extract important keywords from research papers. The system preprocesses text data, calculates TF-IDF scores, and highlights the most important terms from a collection of papers.

Features
Text Preprocessing:

Converts text to lowercase
Removes HTML tags, special characters, digits, and stopwords
Applies lemmatization for better word processing
TF-IDF Keyword Extraction:

Uses Term Frequency-Inverse Document Frequency (TF-IDF) to extract the most significant keywords
Flask Web Application:

Allows users to upload research papers (in text format)
Extracts top keywords from the document
Highlights the most important terms in the text
Installation

Prerequisites
Ensure you have Python 3.x installed.
Then, install the required libraries:


pip install pandas nltk scikit-learn flask matplotlib pickle

Verify Flask Installation

To check if Flask is installed correctly, run:


python -c "import flask; print(flask.__version__)"

If it prints a version number (e.g., 2.2.5), Flask is installed correctly.

Run the Flask App

Create a new Python file (e.g., app.py) and add this code:

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask is working!"

if __name__ == '__main__':
    app.run(debug=True)

Run the script in your terminal:

python app.py

Open the application in your browser:
Go to http://127.0.0.1:5000/ to see the Flask app running. 

Usage
Upload a research paper (text format).

Extract keywords using TF-IDF.

View highlighted keywords in the document.

