import os
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from pathlib import Path

app = Flask(__name__)

# Resolve model path relative to this file for portability
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / 'model.pkl'

# Load model
model = None
if MODEL_PATH.exists():
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
else:
    print("Warning: model.pkl not found. App will run without prediction capability.")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    int_features  = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    if model is None:
        return render_template('index.html', prediction_text='Model is not available on this environment.')
    prediction = model.predict(final_features)
    output = round(prediction[0])
    return render_template('index.html', prediction_text=f"Number of Weekly Rides Should be {output}")

if __name__ == '__main__':
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', '5000'))
    debug = os.environ.get('FLASK_DEBUG', '0') == '1'
    app.run(host=host, port=port, debug=debug)
