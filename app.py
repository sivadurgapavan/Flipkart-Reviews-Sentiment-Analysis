import streamlit as st
import joblib
import re

# Load saved components
model = joblib.load("sentiment_svm_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Text cleaning
def clean_text(text):
    text = text.lower()
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Set page config and background image via HTML
st.set_page_config(page_title="Flipkart Sentiment Analyzer", layout="centered")

# Set background using base64 encoding
def set_background_image(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        .main-title {{
            text-align: center;
            color: white;
            padding: 1rem;
            font-size: 2.5rem;
        }}
        .result-box {{
            background-color: rgba(255, 255, 255, 0.8);
            padding: 1rem;
            border-radius: 10px;
            font-size: 1.2rem;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# 👇 Replace this URL with your own background image link
set_background_image("https://images.unsplash.com/photo-1654573817889-296cad084c97?q=80&w=1462&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")

# Title
st.markdown('<h1 class="main-title">🛍️ Flipkart Review Sentiment Analyzer</h1>', unsafe_allow_html=True)

# Input
user_input = st.text_area("📝 Write your product review here:", height=150)

# Predict Button
if st.button("🔍 Predict Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        cleaned = clean_text(user_input)
        vec = vectorizer.transform([cleaned])
        pred = model.predict(vec)
        sentiment = label_encoder.inverse_transform(pred)[0]

        # Show Result
        st.markdown(
            f'<div class="result-box">✅ **Predicted Sentiment:** <b>{sentiment.capitalize()}</b></div>',
            unsafe_allow_html=True
        )
