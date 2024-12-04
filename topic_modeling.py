import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import os

os.chdir('/Users/yongjunkim/Desktop/snippet')
# Download required NLTK data if not already present
nltk.download('punkt_tab')
nltk.download('stopwords')

def topic_modeling(texts, n_topics=5, n_keywords=10):
    """
    Perform topic modeling on a list of input texts using LDA.
    
    Args:
        texts (list): List of input texts.
        n_topics (int): Number of topics to extract.
        n_keywords (int): Number of keywords per topic.
        
    Returns:
        list: A list of topics, each represented by a list of keywords.
    """
    # Preprocessing function
    def preprocess_text(text):
        # Lowercase
        text = text.lower()
        # Remove punctuation and numbers
        text = re.sub(r'\d+', '', text)
        text = re.sub(r'[^\w\s]', '', text)
        # Tokenize
        tokens = word_tokenize(text)
        # Remove stopwords
        stop_words = set(stopwords.words('english'))
        tokens = [word for word in tokens if word not in stop_words]
        return " ".join(tokens)
    
    # Preprocess all texts
    processed_texts = [preprocess_text(text) for text in texts]
    
    # Convert texts to a document-term matrix
    vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
    dtm = vectorizer.fit_transform(processed_texts)
    
    # Perform LDA
    lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
    lda.fit(dtm)
    
    # Extract keywords for each topic
    keywords = []
    feature_names = vectorizer.get_feature_names_out()
    for topic_idx, topic in enumerate(lda.components_):
        topic_keywords = [feature_names[i] for i in topic.argsort()[:-n_keywords - 1:-1]]
        keywords.append(topic_keywords)
    
    return keywords

# Example usage
texts = [
    "Usable security ensures that security features are intuitive and user-friendly.",
    "Privacy tools must balance user experience with robust protection.",
    "Phishing detection relies on educating users about secure practices.",
    "Designing interfaces for security involves understanding user behavior.",
    "Two-factor authentication is a cornerstone of secure systems, improving user trust."
]

#topics = topic_modeling(texts, n_topics=3, n_keywords=5)
#for i, topic in enumerate(topics):
    #print(f"Topic {i+1}: {', '.join(topic)}")