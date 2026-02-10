import streamlit as st

st.set_page_config(page_title="KisanSense GenAI", layout="centered")

st.title("🌾 KisanSense GenAI")
st.write("AI-Powered Agricultural Advisory Assistant")

query = st.text_input("Enter your farming question")

def agri_advice(q):
    q = q.lower()

    if "aphid" in q:
        return """🔹 **Aphids Control (Expert Advisory)**  
• Spray Neem Oil 3–5 ml per litre of water  
• Use Imidacloprid 0.3 ml per litre if infestation is severe  
• Avoid excess nitrogen fertilizer  
• Encourage natural predators like ladybird beetles"""

    elif "fertilizer" in q:
        return """🔹 **Fertilizer Recommendation**  
• Apply fertilizer based on crop growth stage  
• Use NPK in balanced ratio  
• Avoid over-fertilization  
• Prefer soil testing before application"""

    elif "pest" in q:
        return """🔹 **Pest Management Advice**  
• Monitor crop regularly  
• Use integrated pest management (IPM)  
• Prefer bio-pesticides first  
• Use chemical pesticides only if required"""

    elif "scheme" in q or "pm kisan" in q:
        return """🔹 **Government Scheme Guidance**  
• PM-Kisan provides ₹6000/year  
• Apply via pmkisan.gov.in  
• Aadhaar and land records required"""

    else:
        return """🔹 **General Agricultural Advice**  
• Follow recommended practices  
• Maintain crop hygiene  
• Consult local agriculture officer  
• Use certified seeds"""

if query:
    with st.spinner("Analyzing like an agriculture expert..."):
        answer = agri_advice(query)

    st.subheader("🤖 Advisory Recommendation")
    st.success(answer)

















