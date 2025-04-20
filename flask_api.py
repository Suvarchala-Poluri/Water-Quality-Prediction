from flask import Flask, request, jsonify
import numpy as np
import pickle
import pandas as pd
import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

# Loading the model
with open("KNeighborsClassifier.pkl", "rb") as pickle_in:  
classifier = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome to the Water Potability Prediction API"

@app.route('/predict', methods=["GET"])
def predict_water_potability():
    """Predict Water Potability
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: ph
        in: query
        type: number
        required: true
      - name: hardness
        in: query
        type: number
        required: true
      - name: chloramines
        in: query
        type: number
        required: true
      - name: sulfate
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values (0 for not potable, 1 for potable)
        
    """
    # Getting the input features from the request
    ph = request.args.get("ph", type=float)
    hardness = request.args.get("hardness", type=float)
    chloramines = request.args.get("chloramines", type=float)
    sulfate = request.args.get("sulfate", type=float)

    # Checking for not potable conditions
    if (ph < 6.5 or ph > 8.5):
        return jsonify({"result": "Not Potable", "reason": "pH level is out of range."}), 200
    if (hardness > 200.0):
        return jsonify({"result": "Not Potable", "reason": "Hardness exceeds acceptable limits."}), 200
    if (chloramines > 4.0):
        return jsonify({"result": "Not Potable", "reason": "Chloramines exceed acceptable limits."}), 200
    if (sulfate > 250.0):
        return jsonify({"result": "Not Potable", "reason": "Sulfate exceeds acceptable limits."}), 200

    # Creates a feature array for prediction (only original features)
    features = np.array([[ph, hardness, chloramines, sulfate]])
    
    # Debugging: Print the shape of the features
    print("Features shape:", features.shape)  # Should be (1, 4)

    # Making prediction
    prediction = classifier.predict(features)
    print(prediction)
    
    return jsonify({"result": "Potable" if prediction[0] == 1 else "Not Potable"}), 200

@app.route('/predict_file', methods=["POST"])
def predict_file():
    """Predict Water Potability from a CSV file
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values (list of predictions)
        
    """
    df_test = pd.read_csv(request.files.get("file"))
    print(df_test.head())
    
    
    required_columns = ['ph', 'Hardness', 'Chloramines', 'Sulfate']
    if not all(col in df_test.columns for col in required_columns):
        return jsonify({"error": "The input file must contain the following columns: " + ", ".join(required_columns)}), 400
    
  
    predictions = []
    for index, row in df_test.iterrows():
        result = predict_water_potability(row['ph'], row['Hardness'], row['Chloramines'], row['Sulfate'])
        predictions.append(result)
    
    return jsonify(predictions), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)