import numpy as np
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('predict.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    return render_template('predict.html', prediction_text = "THE STUDENT IS LIKELY TO GET A GRADE OF: {}".format(prediction))

if __name__== "__main__":
    app.run(host='0.0.0.0', debug=True)
