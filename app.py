import streamlit as st
import os
import requests

st.set_page_config(page_title="KisanSense GenAI", layout="centered")

st.title("🌾 KisanSense GenAI")
st.write("AI-Powered Agricultural Advisory Assistant")

API_KEY = os.getenv("GEMINI_API_KEY")

query = st.text_input("Enter your farming question")

if query:
    with st.spinner("Thinking like an agriculture expert..."):

        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.0-pro:generateContent"

        headers = {
            "Content-Type": "application/json",
            "x-goog-api-key": API_KEY
        }

        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [
                        {
                            "text": f"""
You are an expert agricultural advisor in India.
Answer in simple, practical language.

Question: {query}
"""
                        }
                    ]
                }
            ]
        }

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            data = response.json()
            answer = data["candidates"][0]["content"]["parts"][0]["text"]
            st.subheader("🤖 AI Recommendation")
            st.success(answer)
        else:
            st.error("Gemini API Error")
            st.code(response.text)













