# Set NLTK data directory
import nltk
nltk.data.path.append(r"C:\Users\Admin\AppData\Roaming\nltk_data")

# Download required resources
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')