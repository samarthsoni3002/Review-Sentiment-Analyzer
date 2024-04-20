from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import numpy as np
import nltk
from review_scraper import scrape_amazon_reviews
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Lambda
import tensorflow_hub as hub
import tensorflow as tf
from tensorflow.keras.layers import Embedding,Dense,LSTM,Dropout,SpatialDropout1D,TextVectorization,GRU



model = load_model("./review_model.keras")


app = Flask(__name__)


nltk.download("wordnet")
nltk.download("stopwords")


lm = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

def text_preprocessing(text):
    text = re.sub("[^a-zA-Z]", ' ', str(text))
    text = text.lower()
    text = text.split()
    text = [lm.lemmatize(word) for word in text if word not in stop_words]
    text = ' '.join(text)
    return text

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.form['review']
    reviews = scrape_amazon_reviews(data)
    summ = 0
    for i in reviews:
        data = text_preprocessing(i)
        data = [data]
        data = tf.convert_to_tensor(data)
        print(type(data))
        predictions = np.argmax(model.predict(data))
        summ += predictions
    
    final_predictions = int(summ/len(reviews))


    #return render_template("index.html", prediction_text="The predicted score is {}".format(np.argmax(prediction)))
    #print(final_predictions)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
