import streamlit as st
import os
import requests
import json

st.set_page_config(page_title="KisanSense GenAI", layout="centered")

st.title("🌾 KisanSense GenAI")
st.write("AI-Powered Agricultural Advisory Assistant")

API_KEY = os.getenv("GEMINI_API_KEY")

query = st.text_input("Enter your farming question")

if query:
    with st.spinner("Thinking like an agriculture expert..."):

        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": f"""
You are an expert agricultural advisor in India.
Answer the farmer's question in simple, practical language.

Question: {query}
"""
                        }
                    ]
                }
            ]
        }

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(url, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            result = response.json()
            answer = result["candidates"][0]["content"]["parts"][0]["text"]
            st.subheader("🤖 AI Recommendation")
            st.success(answer)
        else:
            st.error("Error from Gemini API. Please try again.")









