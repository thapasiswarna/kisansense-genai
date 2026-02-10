import streamlit as st

st.set_page_config(
    page_title="KisanSense GenAI",
    layout="centered"
)

st.title("🌾 KisanSense GenAI")
st.write("AI-Powered Agricultural Advisory Assistant")

st.divider()

query = st.text_input("Enter your farming question")

if query:
    st.info("Processing your query...")
    st.success("Your AI-based agricultural advice will appear here.")
