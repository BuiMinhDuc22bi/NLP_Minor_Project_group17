import pickle
from flask import Flask, render_template, request
import re
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize

app = Flask(__name__)
# Set NLTK data directory
nltk.data.path.append(r"C:\Users\Admin\AppData\Roaming\nltk_data")

# Load pickled files & data
with open('count_vectorizer.pkl', 'rb') as f:
    cv = pickle.load(f)

with open('tfidf_transformer.pkl', 'rb') as f:
    tfidf_transformer = pickle.load(f)

with open('feature_names.pkl', 'rb') as f:
    feature_names = pickle.load(f)

# Cleaning data:
stop_words = set(stopwords.words('english'))
new_stop_words = ["fig","figure","image","sample","using",
             "show", "result", "large",
             "also", "one", "two", "three",
             "four", "five", "seven","eight","nine"]
stop_words = list(stop_words.union(new_stop_words))

# Preprocessing function with highlighting
def preprocess_and_highlight(txt, keywords):
    # Lower case the text
    original_txt = txt.lower()
    
    # Remove HTML tags (if any)
    txt = re.sub(r"<.*?>", " ", txt)
    
    # Remove non-alphabetic characters
    txt = re.sub(r"[^a-zA-Z]", " ", txt)
    
    # Tokenization
    words = nltk.word_tokenize(txt)
    
    # Lemmatization and removing stopwords
    lmtr = WordNetLemmatizer()
    stop_words = set(stopwords.words("english"))
    filtered_words = [lmtr.lemmatize(word) for word in words if word not in stop_words and len(word) >= 3]
    
    # Highlight keywords in original text
    for keyword in keywords:
        keyword_lower = keyword.lower()  # To match case-insensitive
        if keyword_lower in original_txt:
            # Highlight the keyword by wrapping it in <mark> tags
            original_txt = re.sub(rf"({re.escape(keyword_lower)})", r"<mark>\1</mark>", original_txt)

    return original_txt, filtered_words  # Now returning filtered_words

def sort_coo(coo_matrix):
    tuples = zip(coo_matrix.col, coo_matrix.data)
    return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)

def extract_topn_from_vector(feature_names, sorted_items, topn=10):
    sorted_items = sorted_items[:topn]
    score_vals = []
    feature_vals = []
    for idx, score in sorted_items:
        fname = feature_names[idx]
        score_vals.append(round(score, 3))
        feature_vals.append(fname)

    results = []
    for idx in range(len(feature_vals)):
        results.append({
            'keyword': feature_vals[idx],
            'score': score_vals[idx]
        })
    
    return results
# Generate Summary
def generate_summary(text, keywords, topn=5):
    sentences = sent_tokenize(text)
    sentence_scores = {
        sentence: sum(keywords.get(word, 0) for word in sentence.split() if word in keywords)
        for sentence in sentences
    }
    sorted_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)
    summary = " ".join([sent[0] for sent in sorted_sentences[:topn]])
    return summary
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/extract_keywords', methods=['POST'])
def extract_summary():
    document = request.files['file']
    if document.filename == '':
        return render_template('index.html', error='No document selected')

    if document:
        text = document.read().decode('utf-8', errors='ignore')

        # Extract keywords using TF-IDF
        tf_idf_vector = tfidf_transformer.fit_transform(cv.fit_transform([text]))
        feature_names = cv.get_feature_names_out()
        sorted_items = sort_coo(tf_idf_vector.tocoo())
        keywords = extract_topn_from_vector(feature_names, sorted_items, 20)

        # Convert keyword list into a dictionary for summary generation
        keyword_dict = {kw['keyword']: kw['score'] for kw in keywords}

        # Generate summary
        summary = generate_summary(text, keyword_dict, 5)

        # Highlight keywords in the original text
        highlighted_text = preprocess_and_highlight(text, [kw['keyword'] for kw in keywords])

        return render_template('keywords.html', summary=summary, keywords=keywords, highlighted_text=highlighted_text)

    return render_template('index.html')



@app.route('/search_keywords', methods=['POST'])
def search_keywords():
    search_query = request.form['search']
    if search_query:
        keywords = []
        for keyword in feature_names:
            if search_query.lower() in keyword.lower():
                keywords.append(keyword)
                if len(keywords) == 20:  # Limit to 20 keywords
                    break
        return render_template('keywordslist.html', keywords=keywords)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    
