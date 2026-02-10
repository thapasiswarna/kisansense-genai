import streamlit as st
import os
import google.generativeai as genai

# Page config
st.set_page_config(page_title="KisanSense GenAI", layout="centered")

st.title("🌾 KisanSense GenAI")
st.write("AI-Powered Agricultural Advisory Assistant")

# Configure Gemini using Streamlit Secrets
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ✅ UPDATED MODEL (FIXES ERROR)
model = genai.GenerativeModel("models/gemini-1.5-flash")

query = st.text_input("Enter your farming question")

if query:
    with st.spinner("Thinking like an agriculture expert..."):
        prompt = f"""
You are an expert agricultural advisor in India.
Answer the farmer's question in simple, clear language.
Give practical and actionable advice.

Question: {query}
"""
        response = model.generate_content(prompt)

    st.subheader("🤖 AI Recommendation")
    st.success(response.text)




