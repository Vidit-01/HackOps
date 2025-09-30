import PyPDF2
import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

# Download stopwords if not already done
nltk.download('stopwords')
from nltk.corpus import stopwords

# Step 1: Extract text from PDF using PyPDF2
class KeyWordGenerator():
    def extract_text_from_pdf(self,pdf_path):
        text = ""
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() or ""
        return text

    # Step 2: Preprocess text
    def preprocess(self,text):
        text = text.lower()
        text = re.sub(r'[^a-z\s]', '', text)
        return text

    # Step 3: Extract keywords with TF-IDF
    def extract_keywords_tfidf(self,text, top_n=15):
        stop_words = stopwords.words('english')
        
        vectorizer = TfidfVectorizer(stop_words=stop_words)
        tfidf_matrix = vectorizer.fit_transform([text])  # single document
        scores = tfidf_matrix.toarray()[0]
        
        # Map terms to scores
        terms = vectorizer.get_feature_names_out()
        term_scores = list(zip(terms, scores))
        
        # Sort by score
        sorted_terms = sorted(term_scores, key=lambda x: x[1], reverse=True)
        
        return [term for term, score in sorted_terms[:top_n]]

    def run(self,pdf_text):
        clean_text = self.preprocess(pdf_text)
        keywords = self.extract_keywords_tfidf(clean_text, top_n=20)
        return keywords

