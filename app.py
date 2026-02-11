import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="KisanSense AI Engine",
    page_icon="🌾",
    layout="centered"
)

st.title("🌾 KisanSense – AI Advisory Engine")
st.caption("Backend intelligence layer for the KisanSense agritech platform")
st.divider()

# ---------------- LANGUAGE SELECTION ----------------
language = st.selectbox(
    "Response Language",
    ["English", "Telugu", "Hindi", "Tamil"]
)

# ---------------- AI ADVISORY LOGIC ----------------
def agri_advice(query, lang):
    q = query.lower()

    if "aphid" in q:
        return {
            "English": "Neem oil 3–5 ml per litre. Avoid excess nitrogen. Use Imidacloprid only if infestation is severe.",
            "Telugu": "నీమ్ ఆయిల్ 3–5 మి.లీ లీటర్ నీటిలో పిచికారీ చేయాలి. అధిక నత్రజని నివారించండి.",
            "Hindi": "नीम तेल 3–5 मि.ली. प्रति लीटर पानी में छिड़कें। अधिक नाइट्रोजन से बचें।",
            "Tamil": "நீம் எண்ணெய் 3–5 மி.லி. ஒரு லிட்டர் தண்ணீரில் தெளிக்கவும்."
        }[lang]

    if "fertilizer" in q:
        return {
            "English": "Apply balanced NPK based on soil test and crop stage.",
            "Telugu": "నేల పరీక్ష ఆధారంగా సమతుల్య NPK వాడాలి.",
            "Hindi": "मृदा परीक्षण के अनुसार संतुलित NPK का उपयोग करें।",
            "Tamil": "மண் பரிசோதனை அடிப்படையில் NPK பயன்படுத்தவும்."
        }[lang]

    if "pm kisan" in q or "scheme" in q:
        return {
            "English": "PM-Kisan provides ₹6000 per year via direct benefit transfer.",
            "Telugu": "పీఎం-కిసాన్ ద్వారా సంవత్సరానికి ₹6000 లభిస్తుంది.",
            "Hindi": "पीएम किसान योजना से ₹6000 प्रति वर्ष मिलते हैं।",
            "Tamil": "PM-Kisan திட்டம் வருடத்திற்கு ₹6000 வழங்குகிறது."
        }[lang]

    return {
        "English": "Query forwarded to agriculture expert. Please provide more details.",
        "Telugu": "ప్రశ్న వ్యవసాయ నిపుణులకు పంపబడింది. దయచేసి మరిన్ని వివరాలు ఇవ్వండి.",
        "Hindi": "प्रश्न कृषि विशेषज्ञ को भेजा गया है। कृपया अधिक विवरण दें।",
        "Tamil": "கேள்வி வேளாண் நிபுணரிடம் அனுப்பப்பட்டுள்ளது. மேலும் விவரம் அளிக்கவும்."
    }[lang]

# ---------------- INPUT ----------------
st.markdown("### 📥 Farmer Query (from frontend)")
query = st.text_area(
    "Query Payload",
    placeholder="Example: Aphids in cotton crop",
    height=100
)

# ---------------- PROCESS ----------------
if st.button("Run Advisory Engine"):
    if not query.strip():
        st.warning("No query received.")
    else:
        with st.spinner("Processing advisory..."):
            answer = agri_advice(query, language)

        st.subheader("🧠 AI Advisory Output")
        st.success(answer)

        st.info(
            f"""
            **Engine Type:** Rule-based AI  
            **Language:** {language}  
            **LLM Status:** Ready for future integration
            """
        )

st.divider()
st.caption("KisanSense AI Engine | Reliable • Explainable • LLM-ready")

























