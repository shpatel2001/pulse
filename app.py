import streamlit as st
import pandas as pd
import os
from groq import Groq

st.markdown("""
    <style>
        /* Background gradient */
        .stApp {
            background: linear-gradient(135deg, #eef2f3 0%, #d9e2ec 100%);
        }

        /* Main title */
        .main-title {
            font-size: 48px;
            font-weight: 800;
            color: #1f2937;
            text-align: center;
            margin-top: 10px;
            margin-bottom: 0px;
        }

        /* Subtitle */
        .sub-title {
            font-size: 20px;
            color: #4b5563;
            text-align: center;
            margin-bottom: 40px;
        }

        /* Card container */
        .card {
            background: white;
            padding: 30px;
            border-radius: 14px;
            box-shadow: 0 4px 14px rgba(0,0,0,0.08);
            margin-bottom: 30px;
        }

        /* Section headers */
        .section-header {
            font-size: 26px;
            font-weight: 700;
            color: #1f2937;
            margin-bottom: 15px;
        }

        /* Improve file uploader label */
        .stFileUploader label {
            font-size: 18px !important;
            font-weight: 600 !important;
            color: #374151 !important;
        }

        /* Improve text readability */
        .result-text {
            font-size: 18px;
            line-height: 1.6;
            color: #1f2937;
        }
    </style>
""", unsafe_allow_html=True)

# Page Header
st.markdown('<h1 class="main-title">Pulse</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">AI‑powered customer feedback insights for small businesses</p>', unsafe_allow_html=True)

# Groq Client 
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# File Upload 
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="section-header">Upload Customer Reviews</div>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload a CSV file containing a column named 'review'")

st.markdown('</div>', unsafe_allow_html=True)

# Process File
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    if "review" not in df.columns:
        st.error("Your CSV must contain a column named 'review'.")
    else:
        reviews_text = "\n".join(df["review"].astype(str).tolist())

        # AI Prompt
        prompt = f"""
        You are an AI assistant analyzing customer feedback for a small business.

        Analyze the following customer reviews and produce:

        1. Key themes (3–5)
        2. Top complaints
        3. Top compliments
        4. Actionable recommendations
        5. A short weekly health summary

        Reviews:
        {reviews_text}
        """

        with st.spinner("Analyzing feedback..."):
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3
            )

        ai_output = response.choices[0].message["content"]

        # Results Section
        # st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="section-header">Insights</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="result-text">{ai_output}</div>', unsafe_allow_html=True)
        # st.markdown('</div>', unsafe_allow_html=True)
