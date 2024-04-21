from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import numpy as np
import nltk
from review_scraper import scrape_amazon_reviews
from tensorflow.keras.models import Sequential,Model
from tensorflow.keras.layers import Lambda
import tensorflow_hub as hub
import tensorflow as tf
from tensorflow.keras.layers import Embedding,Dense,LSTM,Dropout,SpatialDropout1D,TextVectorization,GRU


embedding = "https://tfhub.dev/google/nnlm-en-dim50/2"
hub_layer = hub.KerasLayer(embedding, input_shape=[],
                           dtype=tf.string, trainable=True)

class MyModel(Model):
    def __init__(self):
        super(MyModel, self).__init__()
        self.embedding_layer = hub_layer
        self.reshape_layer = tf.keras.layers.Reshape((1,-1))
        self.lstm_layer1 = tf.keras.layers.LSTM(100,dropout=0.2,input_dim=(50), return_sequences=True,activation="relu")
        self.lstm_layer2 = tf.keras.layers.LSTM(100, dropout=0.2,return_sequences=True,activation="relu")
        self.gru_layer3 = tf.keras.layers.GRU(100,activation="relu")
        self.output_layer = tf.keras.layers.Dense(5, activation="softmax")
        
    def call(self, inputs):
        x = self.embedding_layer(inputs)
        x = self.reshape_layer(x)
        x = self.lstm_layer1(x)
        x = self.lstm_layer2(x)
        x = self.gru_layer3(x)
        return self.output_layer(x)
    

model = MyModel()
model.load_weights("./review_model.keras")



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

    
    return render_template("index.html", prediction_text="The predicted score is {}".format(final_predictions))


if __name__ == "__main__":
    app.run(debug=True)
