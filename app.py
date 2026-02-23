import streamlit as st
import pandas as pd
import os
from groq import Groq

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("Pulse – AI Customer Feedback Analyzer")
st.write("Upload customer reviews and get instant insights.")

# File uploader
uploaded = st.file_uploader("Upload a CSV file with a column named 'review'", type=["csv"])

if uploaded:
    # Read CSV safely with flexible parsing
    df = pd.read_csv(uploaded, dtype=str)

    # Normalize column names (lowercase, strip spaces)
    df.columns = df.columns.str.strip().str.lower()

    # Validate presence of review column
    if "review" not in df.columns:
        st.error("Your CSV must contain a column named 'review'.")
    else:
        # Extract review text safely
        all_reviews = "\n".join(df["review"].dropna().astype(str).tolist())

        # Button to trigger analysis
        if st.button("Analyze Feedback"):
            with st.spinner("Analyzing reviews..."):

                prompt = f"""
                You are analyzing customer feedback for a small business.

                Analyze the following customer reviews and provide:

                1. Key themes (3–5)
                2. Top complaints
                3. Top compliments
                4. Actionable recommendations
                5. A short weekly health summary

                Reviews:
                {all_reviews}
                """

                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.3
                )

                st.subheader("AI Insights")
                st.write(response.choices[0].message["content"])
