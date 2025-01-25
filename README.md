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

bash
Sao chép
Chỉnh sửa
pip install -r requirements.txt
Alternatively, manually install each dependency using pip:

bash
Sao chép
Chỉnh sửa
pip install pandas nltk scikit-learn flask matplotlib
Running the System
Prepare the Dataset:

Place the papers.zip file containing the CSV dataset (papers.csv) in the project directory.
The CSV file should have columns such as title, abstract, and paper_text for the papers.
Start the Flask Application: Run the following command to start the Flask web server:

bash
Sao chép
Chỉnh sửa
python app.py
By default, the application will run at http://127.0.0.1:5000/.

Access the Web Interface:

Visit the web application in your browser.
Upload a text file for keyword extraction.
View the extracted keywords, their corresponding TF-IDF scores, and the document with highlighted keywords.
Instructions for Downloading Data and Models
1. Download the Dataset:
Download the dataset (papers.zip) that contains the file papers.csv containing research papers.

2. Pretrained Models:
The following models and resources are saved as pickle files:

count_vectorizer.pkl – Used to convert the text into a matrix of token counts.
tfidf_transformer.pkl – Transforms the word count matrix to a TF-IDF matrix.
feature_names.pkl – Stores the vocabulary used in TF-IDF transformation.
These files should be loaded when running the application. Ensure that these files are placed in the same directory as the script.

System Design
The main components of the system include:

Preprocessing: Text is preprocessed to remove unwanted characters and words.
TF-IDF Vectorization: The CountVectorizer and TfidfTransformer from sklearn are used to generate the TF-IDF scores.
Flask Web Application: The Flask server serves the web interface, handles file uploads, and processes the extracted keywords.
Instructions for Keyword Extraction
Upload a File: In the Flask web interface, upload a plain text document containing a research paper or any article.
Extract Keywords: The system will process the text, extract the top 10 keywords using TF-IDF, and display the keywords along with their TF-IDF scores.
Highlighted Text: The document will be displayed with the keywords highlighted.
References
TF-IDF: Term Frequency – Inverse Document Frequency
NLTK Documentation
Scikit-learn Documentation
Related Projects
Text Classification with TF-IDF
NLP Keyword Extraction System
Steps to deploy and run the system:
Install Dependencies: Run the pip install commands as shown above.
Prepare the Data: Place the papers.zip in the project folder and extract the CSV file.
Run the Flask App: Execute python app.py to start the Flask server and access the web interface.
Upload Documents: Use the web interface to upload a document and extract keywords.