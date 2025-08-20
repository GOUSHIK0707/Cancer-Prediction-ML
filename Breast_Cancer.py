import streamlit as st
import numpy as np
import pickle

# Load model
with open("model_breast.pkl", "rb") as file:
    model = pickle.load(file)

# All 30 feature names
feature_names = [
    "mean radius", "mean texture", "mean perimeter", "mean area", "mean smoothness",
    "mean compactness", "mean concavity", "mean concave points", "mean symmetry", "mean fractal dimension",
    "radius error", "texture error", "perimeter error", "area error", "smoothness error",
    "compactness error", "concavity error", "concave points error", "symmetry error", "fractal dimension error",
    "worst radius", "worst texture", "worst perimeter", "worst area", "worst smoothness",
    "worst compactness", "worst concavity", "worst concave points", "worst symmetry", "worst fractal dimension"
]


presets = {
    "Manual Entry": [0.0] * 30,
    "Healthy Case": [
        13.0, 14.5, 85.0, 550.0, 0.09,
        0.08, 0.04, 0.03, 0.17, 0.06,
        0.45, 1.2, 3.2, 30.0, 0.006,
        0.02, 0.02, 0.01, 0.02, 0.002,
        14.0, 16.0, 90.0, 600.0, 0.10,
        0.12, 0.10, 0.07, 0.25, 0.08
    ],
    "High Risk Case": [
        22.0, 28.0, 145.0, 1500.0, 0.17,
        0.22, 0.23, 0.20, 0.28, 0.09,
        1.2, 2.6, 5.1, 80.0, 0.02,
        0.09, 0.12, 0.08, 0.04, 0.01,
        26.0, 30.0, 200.0, 2500.0, 0.22,
        0.30, 0.34, 0.29, 0.35, 0.13
    ]
}

st.set_page_config(page_title="Breast Cancer Predictor", layout="wide")
st.title("🎀 Breast Cancer Risk Predictor")

preset_option = st.selectbox("Choose an Input Mode", list(presets.keys()))
default_values = presets[preset_option]

with st.form("bc_form"):
    st.subheader("🔬 Diagnostic Features Input")
    cols = st.columns(3)
    input_values = []

    for idx, name in enumerate(feature_names):
        with cols[idx % 3]:
            val = st.text_input(f"{name}", value=f"{default_values[idx]:.4f}")
            try:
                input_values.append(float(val))
            except ValueError:
                st.error(f"Invalid input for {name}. Please enter a numeric value.")
                st.stop()

    submitted = st.form_submit_button("🔍 Predict Risk")

if submitted:
    input_array = np.array(input_values).reshape(1, -1)
    try:
        prediction = model.predict(input_array)[0]
        prob = model.predict_proba(input_array)[0]

        high_risk_prob = prob[0] * 100  # Probability for class 0 (High Risk)

        st.markdown("---")
        if prediction == 0:
            st.error(f"❌ High Risk of Breast Cancer\n\nEstimated Risk: {high_risk_prob:.2f}%")
        else:
            st.success(f"✅ No Risk Detected\n\nEstimated Risk: {high_risk_prob:.2f}%")

    except Exception as e:
        st.error(f"Prediction failed: {e}")

    st.markdown("> ℹ️ This tool does not replace professional medical diagnosis.")

# Sidebar footer
st.sidebar.markdown("---")
st.sidebar.info("🏠 Go back to Home to explore other cancer prediction tools.")
if st.sidebar.button("⬅️ Go to Home"):
    st.switch_page("Home.py")