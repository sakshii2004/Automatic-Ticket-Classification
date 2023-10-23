from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

import pickle

model = pickle.load(open("logisticregmodel.pkl", "rb"))

with open('vectorizer.pickle', 'rb') as file:
  vectorizer = pickle.load(file)


data_point = ['balance transfer use promotion check chase freedom card rep monthly payment approx first bill monthly payment call chase dispute department manager monthly payment amount information keep repeat company term monthly payment calculate confusing tangle option promotional check accompany letter statement balance term monthly payment calculate manager monthly payment amount chase rep transfer sure record mislead deceptive practice financial ruin consumer consumer correct information informed financial decision']

data_point_vec = vectorizer.transform(data_point)

prediction = model.predict(data_point_vec)

print("THE PREIDICTION IS:", prediction)




