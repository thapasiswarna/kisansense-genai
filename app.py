import streamlit as st
from datetime import datetime

# =====================================================
# CONFIG
# =====================================================
st.set_page_config(
    page_title="KisanSense AI Backend",
    page_icon="🌾",
    layout="wide"
)

# =====================================================
# HEADER
# =====================================================
st.markdown("# 🌾 KisanSense – AI Advisory Backend")
st.caption(
    "Internal AI engine powering the KisanSense agritech platform | Hackathon Prototype"
)
st.divider()

# =====================================================
# SIDEBAR – SYSTEM CONTROLS
# =====================================================
st.sidebar.title("⚙️ System Controls")

response_language = st.sidebar.selectbox(
    "Response Language",
    ["English", "Telugu", "Hindi", "Tamil"]
)

service = st.sidebar.selectbox(
    "AI Service",
    [
        "Pest & Disease Advisory",
        "Crop Recommendation",
        "Fertilizer Guidance",
        "Government Schemes",
        "General Advisory"
    ]
)

confidence_level = st.sidebar.slider(
    "Advisory Confidence Level",
    min_value=1,
    max_value=5,
    value=4,
    help="Simulates AI confidence scoring"
)

st.sidebar.divider()
st.sidebar.caption("Frontend (Lovable) → AI Backend (This App)")

# =====================================================
# AI KNOWLEDGE BASE
# =====================================================
KNOWLEDGE_BASE = {
    "pest": {
        "aphid": {
            "English": "Apply Neem oil 3–5 ml/L. Avoid excess nitrogen. Use Imidacloprid only if infestation is severe.",
            "Telugu": "నీమ్ ఆయిల్ 3–5 మి.లీ/లీటర్ పిచికారీ చేయాలి. అధిక నత్రజని నివారించండి.",
            "Hindi": "नीम तेल 3–5 मि.ली/लीटर छिड़कें। अधिक नाइट्रोजन से बचें।",
            "Tamil": "நீம் எண்ணெய் 3–5 மி.லி/லிட்டர் தெளிக்கவும்."
        }
    },
    "fertilizer": {
        "general": {
            "English": "Apply balanced NPK based on soil test and crop growth stage.",
            "Telugu": "నేల పరీక్ష ఆధారంగా సమతుల్య NPK వాడాలి.",
            "Hindi": "मृदा परीक्षण के अनुसार संतुलित NPK का उपयोग करें।",
            "Tamil": "மண் பரிசோதனை அடிப்படையில் NPK பயன்படுத்தவும்."
        }
    },
    "schemes": {
        "pm kisan": {
            "English": "PM-Kisan provides ₹6000 per year via direct benefit transfer.",
            "Telugu": "పీఎం-కిసాన్ ద్వారా సంవత్సరానికి ₹6000 లభిస్తుంది.",
            "Hindi": "पीएम किसान योजना से ₹6000 प्रति वर्ष मिलते हैं।",
            "Tamil": "PM-Kisan திட்டம் வருடத்திற்கு ₹6000 வழங்குகிறது."
        }
    }
}

# =====================================================
# AI ENGINE
# =====================================================
def run_ai_engine(query, lang, service):
    q = query.lower()

    if service == "Pest & Disease Advisory":
        for k, v in KNOWLEDGE_BASE["pest"].items():
            if k in q:
                return v[lang], "Pest Knowledge Base"

    if service == "Fertilizer Guidance":
        return KNOWLEDGE_BASE["fertilizer"]["general"][lang], "Fertilizer Rules"

    if service == "Government Schemes":
        for k, v in KNOWLEDGE_BASE["schemes"].items():
            if k in q:
                return v[lang], "Scheme Database"

    fallback = {
        "English": "Query escalated to agricultural expert system.",
        "Telugu": "ప్రశ్న వ్యవసాయ నిపుణుల వ్యవస్థకు పంపబడింది.",
        "Hindi": "प्रश्न कृषि विशेषज्ञ प्रणाली को भेजा गया है।",
        "Tamil": "கேள்வி வேளாண் நிபுணர் அமைப்பிற்கு அனுப்பப்பட்டது."
    }

    return fallback[lang], "Fallback Handler"

# =====================================================
# REQUEST INPUT
# =====================================================
st.markdown("## 📥 Incoming Request (from Frontend)")

query = st.text_area(
    "Farmer Query Payload",
    placeholder="Example: Aphids observed in cotton crop",
    height=120
)

# =====================================================
# EXECUTION
# =====================================================
if st.button("▶ Run AI Advisory Engine"):
    if not query.strip():
        st.warning("No input query received.")
    else:
        with st.spinner("Executing advisory pipeline..."):
            response, source = run_ai_engine(query, response_language, service)

        st.divider()

        col1, col2, col3 = st.columns([2, 1, 1])

        with col1:
            st.markdown("### 🧠 AI Response")
            st.success(response)

        with col2:
            st.markdown("### 📊 Decision Info")
            st.info(f"""
            **Service:** {service}  
            **Language:** {response_language}  
            **Confidence:** {confidence_level}/5  
            **Source:** {source}
            """)

        with col3:
            st.markdown("### 🕒 System Metadata")
            st.write(f"""
            **Timestamp:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
            **Engine Type:** Rule-based AI  
            **LLM Status:** Ready for integration
            """)

# =====================================================
# SYSTEM STATUS
# =====================================================
st.divider()
st.markdown("## 🖥️ System Status")

c1, c2, c3 = st.columns(3)
c1.metric("AI Modules Active", "5")
c2.metric("Supported Languages", "4")
c3.metric("API Dependency", "None")

# =====================================================
# FOOTER
# =====================================================
st.caption(
    "KisanSense AI Backend | Modular • Explainable • Scalable • Hackathon-Ready"
)























