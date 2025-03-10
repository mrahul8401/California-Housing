from flask import Flask, request, app, jsonify, url_for, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load trained model
model = pickle.load(open("regmodel.pkl", "rb"))
scalar = pickle.load(open("scalar.pkl", "rb "))

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/predict_api', methods=['POST'])

def predict_api():
    data = request.json["data"]  # Get JSON input
    print(data)
    print(np.array(list(data.values())).reshape(1, -1)))
    new_data = scalar.transform(np.array(list(data.values())).reshape(1, -1))
    output = model.predict(new_data)
    print(output[0])
    return jsonify(output[0])

if __name__ == '__main__':
    app.run(debug=True)

