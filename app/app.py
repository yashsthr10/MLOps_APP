import streamlit as st
import pandas as pd
import joblib
import os


# Get absolute path to project root
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Point to model path safely
MODEL_PATH = os.path.join(BASE_DIR, "../scripts/models/model.pkl")

# Load model
model = joblib.load(MODEL_PATH)

st.title("🌸 Iris Classifier — Powered by ML & Streamlit")

# Form for user input
sepal_length = st.slider("Sepal Length", 4.0, 8.0, 5.1)
sepal_width = st.slider("Sepal Width", 2.0, 5.0, 3.5)
petal_length = st.slider("Petal Length", 1.0, 7.0, 1.4)
petal_width = st.slider("Petal Width", 0.1, 2.5, 0.2)

# Prediction
if st.button("🌟 Predict"):
    input_df = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]],
                            columns=["sepal_length", "sepal_width", "petal_length", "petal_width"])
    prediction = model.predict(input_df)[0]
    probs = model.predict_proba(input_df)[0]

    st.success(f"Predicted Class: **{prediction}**")
    st.write("Class Probabilities:")
    st.bar_chart(probs)
