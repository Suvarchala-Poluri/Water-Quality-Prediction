## Water Quality Prediction

Water quality is an essential aspect of public health and environmental sustainability. This project utilizes machine learning to predict whether water is potable (safe for drinking) based on its physical and chemical properties.

---

## Features

- **Data Analysis**: Exploratory data analysis to understand the key features affecting water quality.
- **Machine Learning Models**: Implementation of predictive models to classify water as potable or non-potable.
- **Flask API**: A lightweight web API for model deployment and integration.
- **Visualization**: Insights into the data through visualizations.

---

## Dataset

The dataset used for this project is **`water_potability.csv`**, containing information about:

- pH
- Hardness
- Solids
- Chloramines
- Sulfate
- Conductivity
- Organic Carbon
- Trihalomethanes
- Turbidity
- Target Variable: **Potability**

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Suvarchala-Poluri/Water-Quality-Prediction.git
   cd Water-Quality-Prediction
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

---

## Usage

### Local Deployment

1. Launch the Flask app using the command:
   ```bash
   python app.py
   ```

2. Access the web interface in your browser:
   ```
   http://127.0.0.1:5000
   ```

3. Upload water quality data and receive predictions for potability.

---

## Project Structure

- **`app.py`**: Main application file for the Flask web interface.
- **`flask_api.py`**: Backend API logic for serving predictions.
- **`water_potability.csv`**: Dataset used for training and testing the model.
- **Images**: Visualization assets used for documentation and analysis.
- **`code_part.pdf`**: Technical explanation of the project's methodologies and findings.

---

## Results

- **Accuracy**: [Insert Model Accuracy]
- **Key Insights**: [Highlight findings from the data analysis and modeling.]

---

## Future Scope

- Enhance the dataset with additional real-world samples.
- Experiment with more advanced machine learning techniques.
- Deploy the application on a cloud platform for scalability.
