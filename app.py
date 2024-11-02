import streamlit as st
import numpy as np
import pickle

# Load the model
with open('final_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Define means and stds
mean_values = [41.885856, 0.07485, 0.03942, 27.320767, 5.527507, 138.058060]
std_values = [22.516840, 0.26315, 0.194593, 6.636783, 1.070672, 40.708136]

# Custom CSS for styling
st.markdown("""
    <style>
    body, .stApp {
        font-family: 'Segoe UI', sans-serif;
        background-color: #f4f4f9;
    }
    .title {
        font-size: 36px;
        color: #333;
        text-align: center;
        margin-bottom: 30px;
    }
    .input-header {
        font-size: 24px;
        color: #007BFF;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .btn {
        background-color: #007BFF;
        color: white;
        padding: 10px;
        border-radius: 5px;
        border: none;
        cursor: pointer;
    }
    .result {
        font-weight: bold;
        font-size: 24px;
        margin-top: 20px;
        text-align: center;
    }
    .diabetic {
        color: #d9534f;
    }
    .not-diabetic {
        color: #5cb85c;
    }
    .stButton>button {
        background-color: #007BFF;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #0056b3;
        transition: background-color 0.3s ease;
    }
    .stSlider>div {
        color: #007BFF;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.markdown('<div class="title">Diabetes Prediction App</div>', unsafe_allow_html=True)
st.write("This app predicts diabetes risk based on user input. Fill in the details below to get a prediction.")

# User input section
st.markdown('<div class="input-header">Enter Patient Information:</div>', unsafe_allow_html=True)
age = st.slider('Age', 0, 100, 50)
hypertension = st.selectbox('Hypertension', ['No', 'Yes'])
heart_disease = st.selectbox('Heart Disease', ['No', 'Yes'])
bmi = st.slider('BMI', 10.0, 50.0, 25.0, 0.1)
HbA1c_level = st.slider('HbA1c Level', 4.0, 15.0, 7.0, 0.1)
blood_glucose_level = st.slider('Blood Glucose Level', 50, 400, 100)

# Feature scaling function
def scale_features(age, hypertension, heart_disease, bmi, HbA1c_level, blood_glucose_level):
    scaled_features = [(x - mean) / std for x, mean, std in zip(
        [age, hypertension == 'Yes', heart_disease == 'Yes', bmi, HbA1c_level, blood_glucose_level],
        mean_values, std_values
    )]
    return scaled_features

# Prediction function
def make_prediction(scaled_features):
    return loaded_model.predict([scaled_features])

# Prediction button
if st.button('Predict Diabetes'):
    with st.spinner('Calculating...'):
        scaled_features = scale_features(age, hypertension, heart_disease, bmi, HbA1c_level, blood_glucose_level)
        prediction = make_prediction(scaled_features)
        if prediction[0] == 1:
            st.markdown('<div class="result diabetic">Prediction: Diabetic</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="result not-diabetic">Prediction: Not Diabetic</div>', unsafe_allow_html=True)
    st.balloons()  # Adds a fun animation when the prediction is made
