# NLP Minor Project (Group 17)

## Project Overview


This project focuses on keyword extraction to identify the most frequently used keywords in research papers. Using TF-IDF and CountVectorizer techniques, it extracts key terms and generates a concise summary based on the most relevant words found in the text. This tool is useful for researchers, students, and professionals who need quick insights from large documents.

## Features


### Text Preprocessing:
- Converts text to lowercase
- Removes HTML tags, special characters, digits, and stopwords
- Applies lemmatization for better word processing

### TF-IDF Keyword Extraction:
- Uses Term Frequency-Inverse Document Frequency (TF-IDF) to extract the most significant keywords

### Flask Web Application:
- Allows users to upload research papers (in text format)
- Extracts top keywords from the document
- Highlights the most important terms in the text
- Summary based on the most popular keywords




## Installation


### Prerequisites
Ensure you have Python 3.x installed.
Then, install the required libraries:

## Dataset
Our dataset, paper.csv, is included, zipped in the NLP-key-extraction folder and will run automatically in Keyword Extraction with Python.ipynb, so there is no need to unzip it.

```sh
pip install pandas nltk scikit-learn flask matplotlib pickle flask
```

### Verify Flask Installation
To check if Flask is installed correctly, run:

```sh
python -c "import flask; print(flask.__version__)"
```

If it prints a version number (e.g., `2.2.5`), Flask is installed correctly.



## Deployment and Run Flask

Run the script in your terminal:

```sh
python app.py
```

### Open the application in your browser:
Go to (http://127.0.0.1:5000/) to see the Flask app running.

## Usage


1. Upload a research paper (text format).
2. Extract keywords using TF-IDF.
3. View highlighted keywords in the document.

## Resources


Here are some useful resources to understand TF-IDF, CountVectorizer, and Flask:

- TF-IDF Explanation: [Scikit-Learn TF-IDF](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
- CountVectorizer Overview: [Scikit-Learn CountVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html)
- Flask Documentation: [Flask Official Docs](https://flask.palletsprojects.com/en/latest/)
