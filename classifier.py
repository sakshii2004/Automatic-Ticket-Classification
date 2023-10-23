from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import contractions
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import spacy
nltk.download('punkt')
nltk.download('stopwords')

nlp = spacy.load("en_core_web_md")
import re

model = pickle.load(open("logisticregmodel.pkl", "rb"))

with open('vectorizer.pickle', 'rb') as file:
  vectorizer = pickle.load(file)


def preprocess(text):
  text = text.lower()
  text = contractions.fix(text)

  exclude = string.punctuation
  remove_punctuation = str.maketrans('', '', exclude)
  text = text.translate(remove_punctuation)

  pattern = r'xxxx xxxx|xxxx2018|xxxx|xxxxxxxx'
  text = re.sub(pattern, '', text)

  text = word_tokenize(text)
  stop_words = set(stopwords.words('english'))
  text = [token for token in text if token not in stop_words]
  text = ' '.join(text)

  lemmatized_list = []
  doc = nlp(text)
  text = " ".join([token.lemma_ for token in doc])

  doc = nlp(text)
  text = [
    token.text for token in doc if token.pos_ in ('ADJ', 'NOUN', 'PROPN')
  ]

  text = ' '.join(text)

  return text


def predict(text):
  data_point_vec = vectorizer.transform([text])
  prediction = model.predict(data_point_vec)
  return prediction[0]


#data_point_vec = vectorizer.transform(data_point)

#prediction = model.predict(data_point_vec)

#print("THE PREIDICTION IS:", prediction)
