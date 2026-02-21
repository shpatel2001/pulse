import streamlit as st
import pandas as pd
import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("Pulse – AI Customer Feedback Analyzer")
st.write("Upload customer reviews and get instant insights.")

uploaded = st.file_uploader("Upload a CSV file with a column named 'review'", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)
    all_reviews = " ".join(df['review'].astype(str).tolist())

    if st.button("Analyze Feedback"):
        with st.spinner("Analyzing reviews..."):

            prompt = f"""
            You are analyzing customer feedback for a small business.

            Reviews:
            {all_reviews}

            Provide:
            1. A summary of key themes
            2. Top 3 complaints
            3. Top 3 compliments
            4. 3 actionable improvements the business should make
            5. A weekly health report (tone, trends, risks)
            """

            response = client.chat.completions.create(
                 model="llama-3.1-8b-instant",
                 messages=[{"role": "user", "content": prompt}]
            )


            st.subheader("AI Insights")
            st.write(response.choices[0].message.content)
