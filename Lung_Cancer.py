import streamlit as st
import numpy as np
import pickle

# Page config
st.set_page_config(page_title="Lung Cancer Prediction", layout="centered")

# Load the trained model
try:
    lung_model = pickle.load(open("model_lung_update.pkl", "rb"))
except Exception as e:
    st.error(f"❌ Failed to load model: {e}")
    lung_model = None

# Page title
st.title("🫁 Lung Cancer Prediction")
st.markdown("### Fill in the details below to predict your risk.")

# Encode function
def encode(val): return 1 if val == "Yes" else 0

# Input form
with st.form("lung_form"):
    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        age = st.slider("Age", 5, 100, 40)
        smoking = st.selectbox("Do you smoke?", ["Yes", "No"])
        yellow_fingers = st.selectbox("Do you have yellow fingers?", ["Yes", "No"])
        anxiety = st.selectbox("Do you suffer from anxiety?", ["Yes", "No"])
        peer_pressure = st.selectbox("Are you influenced by peer pressure?", ["Yes", "No"])
        chronic_disease = st.selectbox("Do you have chronic disease?", ["Yes", "No"])
        fatigue = st.selectbox("Do you often feel fatigue?", ["Yes", "No"])

    with col2:
        allergy = st.selectbox("Do you have allergies?", ["Yes", "No"])
        wheezing = st.selectbox("Do you experience wheezing?", ["Yes", "No"])
        alcohol_consuming = st.selectbox("Do you consume alcohol?", ["Yes", "No"])
        coughing = st.selectbox("Do you cough frequently?", ["Yes", "No"])
        shortness_breath = st.selectbox("Do you experience shortness of breath?", ["Yes", "No"])
        swallowing_difficulty = st.selectbox("Do you have difficulty swallowing?", ["Yes", "No"])
        chest_pain = st.selectbox("Do you feel chest pain?", ["Yes", "No"])

    submit = st.form_submit_button("🔍 Predict Risk")

# Prediction logic
if submit and lung_model:
    input_data = np.array([
        1 if gender == "Male" else 0,
        age,
        encode(smoking),
        encode(yellow_fingers),
        encode(anxiety),
        encode(peer_pressure),
        encode(chronic_disease),
        encode(fatigue),
        encode(allergy),
        encode(wheezing),
        encode(alcohol_consuming),
        encode(coughing),
        encode(shortness_breath),
        encode(swallowing_difficulty),
        encode(chest_pain)
    ]).reshape(1, -1)

    prediction = lung_model.predict(input_data)[0]
    probability = lung_model.predict_proba(input_data)[0][1] * 100

    st.markdown("---")
    if prediction == 1:
        st.error(f"❌ High Risk of Lung Cancer\n\nEstimated Risk: {probability:.2f}%")
    else:
        st.success(f"✅ Low Risk of Lung Cancer\n\nEstimated Risk: {probability:.2f}%")

    st.markdown("> ℹ️ This tool is for educational purposes and not a medical diagnosis.")
    st.markdown("---")
    st.markdown("💡 Note: This result should not replace professional medical advice.")

# Sidebar footer
st.sidebar.markdown("---")
st.sidebar.info("🏠 Go back to Home to explore other cancer prediction tools.")
if st.sidebar.button("⬅️ Go to Home"):
    st.switch_page("Home.py")
