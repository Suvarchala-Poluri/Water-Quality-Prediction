# Importing necessary libraries
import streamlit as st
import numpy as np
import pickle
from PIL import Image  # Importing the Image module from PIL

# Loading pickle file
with open("KNeighborsClassifier.pkl", "rb") as pickle_in:
    classifier = pickle.load(pickle_in)

def predict_water_potability(ph, hardness, chloramines, sulfate):
    """Predict water potability based on input features."""
    
    # Calculating binary features based on thresholds
    is_ph_ok = int((ph >= 6.5) and (ph <= 8.5))
    is_hardness_ok = int(hardness <= 200.0)
    is_chloramines_ok = int(chloramines <= 4.0)
    is_sulfate_ok = int(sulfate <= 250.0)
    
    # Checking for non-potable conditions
    non_potable_conditions = (
        ph < 6.5 or ph > 8.5 or
        hardness > 200.0 or
        chloramines > 4.0 or
        sulfate > 250.0
    )

    if non_potable_conditions:
        return 0  # Non-potable

    # Creating a feature array for prediction
    features = np.array([[ph, hardness, chloramines, sulfate,
                          is_ph_ok, is_hardness_ok, is_chloramines_ok, is_sulfate_ok]])
    
    # Making prediction
    prediction = classifier.predict(features)
    return prediction[0]  # Returns the first element of the prediction array

def main():
    st.title("Water Potability Predictor")

    # background image using CSS
    image_path = r"C:\Users\suchi\Desktop\water_quality_two\background.jpg"  
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpeg;base64,{get_base64_image(image_path)});
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            height: 100vh;
            color: blue;  /* Change text color to white for better visibility */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Input fields for the features
    ph = st.number_input("pH", min_value=0.0, max_value=14.0, value=7.0, step=0.1)
    hardness = st.number_input("Hardness", min_value=0.0, value=200.0, step=1.0)
    chloramines = st.number_input("Chloramines", min_value=0.0, value=4.0, step=0.1)
    sulfate = st.number_input("Sulfate", min_value=0.0, value=250.0, step=1.0)

    result = ""
    if st.button("Predict"):
        result = predict_water_potability(ph, hardness, chloramines, sulfate)
        if result == 1:
            st.success('The predicted water potability is: Potable')
        else:
            st.error('The predicted water potability is: Not Potable')

    if st.button("About"):
        st.text("Let's Learn")
        st.text("Built with Streamlit")

def get_base64_image(image_path):
    """Convert an image to base64 for embedding in HTML."""
    import base64
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

if __name__ == '__main__':
    main()