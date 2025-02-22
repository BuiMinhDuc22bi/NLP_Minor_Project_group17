# NLP_Minor_Project_group17
Keyword Extraction from Research Papers
This project implements a Keyword Extraction system using TF-IDF to extract important keywords from research papers. The system preprocesses text data, calculates TF-IDF scores, and highlights the most important terms from a collection of papers.

Features
Text Preprocessing: The text is cleaned by converting it to lowercase, removing HTML tags, special characters, digits, and stopwords, as well as lemmatizing the words.
TF-IDF Keyword Extraction: The system uses the Term Frequency-Inverse Document Frequency (TF-IDF) method to extract the most significant keywords from the text.
Flask Web Application: A web interface allows users to upload research papers (in text format), extract the top keywords, and highlight them in the document.
Installation
To run this project, you'll need to have the following dependencies installed:

Python 3.x
Required libraries:
pandas
nltk
sklearn
flask
matplotlib
pickle
You can install the required libraries with the following command:

1. Install Flask using pip
Open your terminal or command prompt and run:

pip install flask
2. Verify the Installation
After installation, check if Flask is installed by running:


python -c "import flask; print(flask.__version__)"
If it prints a version number (e.g., 2.2.5), Flask is installed correctly. 

3. Create a Simple Flask App (Optional)
Create a new Python file (e.g., app.py) and add this code:

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask is working!"

if __name__ == '__main__':
    app.run(debug=True)
Run it with:
python app.py
Then, open http://127.0.0.1:5000/ in your browser to see it running.