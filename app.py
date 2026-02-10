import streamlit as st

# ------------------------------------------------
# CONFIG
# ------------------------------------------------
st.set_page_config(
    page_title="KisanSense AI Engine",
    page_icon="🤖",
    layout="wide"
)

# ------------------------------------------------
# HEADER
# ------------------------------------------------
st.markdown("## 🤖 KisanSense – AI Advisory Engine")
st.caption("Backend service for agricultural intelligence (Hackathon Prototype)")
st.divider()

# ------------------------------------------------
# SIDEBAR – ENGINE CONTROLS
# ------------------------------------------------
st.sidebar.title("⚙️ Engine Controls")

language = st.sidebar.selectbox(
    "Response Language",
    ["English", "Telugu", "Hindi", "Tamil"]
)

module = st.sidebar.radio(
    "Advisory Module",
    [
        "General Advisory",
        "Pest Management",
        "Fertilizer Guidance",
        "Government Schemes"
    ]
)

st.sidebar.caption("Frontend (Lovable) → Backend (This Engine)")

# ------------------------------------------------
# CORE AI LOGIC
# ------------------------------------------------
def ai_engine(query, lang, module):
    q = query.lower()

    responses = {
        "Pest Management": {
            "aphid": {
                "English": "Neem oil 3–5 ml/L. Avoid excess nitrogen. Use Imidacloprid if severe.",
                "Telugu": "నీమ్ ఆయిల్ 3–5 మి.లీ/లీటర్ పిచికారీ చేయాలి. అధిక నత్రజని నివారించండి.",
                "Hindi": "नीम तेल 3–5 मि.ली./लीटर छिड़कें। अधिक नाइट्रोजन से बचें।",
                "Tamil": "நீம் எண்ணெய் 3–5 மி.லி/லிட்டர் தெளிக்கவும்."
            }
        },
        "Fertilizer Guidance": {
            "fertilizer": {
                "English": "Use balanced NPK based on soil testing and crop stage.",
                "Telugu": "నేల పరీక్ష ఆధారంగా సమతుల్య NPK వాడండి.",
                "Hindi": "मृदा परीक्षण के अनुसार संतुलित NPK का उपयोग करें।",
                "Tamil": "மண் பரிசோதனை அடிப்படையில் NPK பயன்படுத்தவும்."
            }
        },
        "Government Schemes": {
            "pm kisan": {
                "English": "PM-Kisan provides ₹6000/year to eligible farmers.",
                "Telugu": "పీఎం కిసాన్ ద్వారా రైతులకు సంవత్సరానికి ₹6000 లభిస్తుంది.",
                "Hindi": "पीएम किसान योजना से ₹6000 प्रति वर्ष मिलते हैं।",
                "Tamil": "PM-Kisan திட்டம் வருடத்திற்கு ₹6000 வழங்குகிறது."
            }
        }
    }

    # Module-based reasoning
    if module in responses:
        for keyword, reply in responses[module].items():
            if keyword in q:
                return reply[lang], module

    # Fallback
    fallback = {
        "English": "Query forwarded to agriculture expert. Please refine the input.",
        "Telugu": "ప్రశ్న వ్యవసాయ నిపుణులకు పంపబడింది. దయచేసి స్పష్టంగా అడగండి.",
        "Hindi": "प्रश्न कृषि विशेषज्ञ को भेजा गया है। कृपया स्पष्ट पूछें।",
        "Tamil": "கேள்வி வேளாண் நிபுணரிடம் அனுப்பப்பட்டது. தெளிவாக கேளுங்கள்."
    }

    return fallback[lang], "Fallback Handler"

# ------------------------------------------------
# MAIN INPUT AREA
# ------------------------------------------------
st.markdown("### 📥 Incoming Farmer Query")

query = st.text_area(
    "Query Payload (from frontend)",
    placeholder="e.g. Aphids in cotton crop",
    height=100
)

# ------------------------------------------------
# PROCESSING
# ------------------------------------------------
if st.button("Run AI Advisory Engine"):
    if query.strip() == "":
        st.warning("No query received from frontend.")
    else:
        with st.spinner("Processing through AI engine..."):
            answer, used_module = ai_engine(query, language, module)

        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🧠 Engine Output")
            st.success(answer)

        with col2:
            st.markdown("### 🧩 Decision Metadata")
            st.info(f"""
            **Language:** {language}  
            **Module Used:** {used_module}  
            **Engine Type:** Rule-based AI  
            **LLM Status:** Plug-in Ready
            """)

# ------------------------------------------------
# FOOTER
# ------------------------------------------------
st.divider()
st.caption(
    "KisanSense AI Engine | Modular • Explainable • LLM-ready | Hackathon Prototype"
)























