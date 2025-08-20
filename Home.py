import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Cancer Prediction App", layout="centered")

st.title("🧬 Cancer Prediction System")
st.markdown("""
Welcome to the **Cancer Prediction Web App**.  
This tool uses trained Machine Learning models to predict the risk of:
- 🫁 **Lung Cancer**
- 🎀 **Breast Cancer**

Select a prediction module from the sidebar to begin.
""")
st.markdown("---")


image_url = "https://ec.europa.eu/newsroom/repository/document/2024-3/jrc202310_1200x540px_Newsroom_NewsletterBanner_KCC_CmT9lluun3jTOLZflpF1oy5sRw_101425.png"

st.image(image_url, caption="Early detection saves lives", use_container_width=True)

st.markdown("""
<div style="
    padding: 1.2rem;
    background: linear-gradient(135deg, #ffe0ec, #fce4ec);
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    border-left: 8px solid #e91e63;
    font-family: 'Segoe UI', sans-serif;
">
    <span style="font-size: 1.25rem; font-weight: 500; color: #880e4f;">
        💡 <em>The best protection is early detection.</em>
    </span>
</div>
""", unsafe_allow_html=True)


st.markdown("---")

# 📊 Optional: Add model stats
col1, col2 = st.columns(2)
col1.metric("🫁 Lung Cancer", "87% Accuracy", "↑ 3.2%")
col2.metric("🎀 Breast Cancer", "95% Accuracy", "↑ 1.5%")


# Sidebar navigation using streamlit-option-menu
with st.sidebar:
    selected = option_menu(
        menu_title="Select Prediction Module",
        options=["Home", "Lung Cancer", "Breast Cancer"],
        icons=["house", "lungs", "heart-pulse", "sun"],
        menu_icon="cast",
        default_index=0,
    )

# Navigation logic

if selected == "Lung Cancer":
    st.switch_page("pages/Lung_Cancer.py")
elif selected == "Breast Cancer":
    st.switch_page("pages/Breast_Cancer.py")
else:
    st.info("Use the sidebar to navigate to a prediction page.")
