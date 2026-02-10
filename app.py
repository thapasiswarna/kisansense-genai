import streamlit as st

# -------------------------------------------------
# Page Config
# -------------------------------------------------
st.set_page_config(
    page_title="KisanSense GenAI",
    page_icon="🌾",
    layout="wide"
)

# -------------------------------------------------
# Sidebar Navigation
# -------------------------------------------------
st.sidebar.title("🌾 KisanSense GenAI")
page = st.sidebar.radio(
    "Navigate",
    ["Home", "Chatbot", "Crop Advisory", "Schemes", "About"]
)

st.sidebar.caption("AI for Farmers 🌱")

# -------------------------------------------------
# Translation & Advisory Logic
# -------------------------------------------------
def get_advice(query, lang):
    q = query.lower()

    responses = {
        "aphids": {
            "English": "Spray Neem Oil 3–5 ml per litre. Use Imidacloprid if infestation is severe. Avoid excess nitrogen fertilizer.",
            "Telugu": "నీమ్ ఆయిల్ 3–5 మి.లీ లీటర్ నీటిలో కలిపి పిచికారీ చేయాలి. ఎక్కువ నత్రజని ఎరువులు వేయకండి.",
            "Hindi": "नीम तेल 3–5 मि.ली. प्रति लीटर पानी में छिड़कें। अधिक नाइट्रोजन से बचें।",
            "Tamil": "நீம் எண்ணெய் 3–5 மி.லி. ஒரு லிட்டர் தண்ணீரில் தெளிக்கவும்."
        }
    }

    if "aphid" in q or "ఆఫిడ్" in q or "एफिड" in q or "அஃபிட" in q:
        return responses["aphids"][lang]

    return {
        "English": "Please consult your local agriculture officer for this issue.",
        "Telugu": "ఈ సమస్యకు స్థానిక వ్యవసాయ అధికారిని సంప్రదించండి.",
        "Hindi": "इस समस्या के लिए स्थानीय कृषि अधिकारी से संपर्क करें।",
        "Tamil": "இந்த பிரச்சனைக்கு அருகிலுள்ள வேளாண் அதிகாரியை அணுகவும்."
    }[lang]

# -------------------------------------------------
# HOME PAGE
# -------------------------------------------------
if page == "Home":
    st.markdown("## 🌾 Empowering Farmers with AI")
    st.write(
        "KisanSense GenAI is a smart agricultural assistance platform designed "
        "to help farmers with crop advisory, pest control, fertilizer guidance, "
        "and government schemes — all in their native language."
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.success("🌱 Crop Advisory\n\nStage-wise recommendations")

    with col2:
        st.info("🐛 Pest & Disease Help\n\nInstant expert guidance")

    with col3:
        st.warning("🏛️ Government Schemes\n\nPM-Kisan & subsidies")

    st.divider()

    st.markdown("### 💡 Why KisanSense?")
    st.write(
        "- Simple and farmer-friendly\n"
        "- Works even without external AI APIs\n"
        "- Multilingual and inclusive\n"
        "- Designed for rural accessibility"
    )

# -------------------------------------------------
# CHATBOT PAGE
# -------------------------------------------------
if page == "Chatbot":
    st.header("💬 KisanSense Chatbot")
    st.caption("Ask questions in your native language")

    language = st.selectbox(
        "Select your language",
        ["English", "Telugu", "Hindi", "Tamil"]
    )

    if "chat" not in st.session_state:
        st.session_state.chat = []

    user_query = st.chat_input("Type your farming question here...")

    if user_query:
        st.session_state.chat.append(("user", user_query))
        bot_reply = get_advice(user_query, language)
        st.session_state.chat.append(("bot", bot_reply))

    for role, msg in st.session_state.chat:
        if role == "user":
            st.chat_message("user").write(msg)
        else:
            st.chat_message("assistant").write(msg)

# -------------------------------------------------
# CROP ADVISORY PAGE
# -------------------------------------------------
if page == "Crop Advisory":
    st.header("🌱 Crop Advisory")

    crop = st.selectbox("Select Crop", ["Wheat", "Rice", "Cotton"])
    stage = st.selectbox("Growth Stage", ["Sowing", "Vegetative", "Flowering"])

    st.success(
        f"Recommended practices for **{crop}** during **{stage}** stage will be shown here."
    )

# -------------------------------------------------
# SCHEMES PAGE
# -------------------------------------------------
if page == "Schemes":
    st.header("🏛️ Government Schemes")

    st.markdown("""
    ### PM-Kisan Samman Nidhi
    - ₹6000 per year
    - Direct bank transfer
    - Eligibility: Small & marginal farmers
    - Apply via: https://pmkisan.gov.in
    """)

    st.markdown("""
    ### Crop Insurance (PMFBY)
    - Protection against crop loss
    - Low premium rates
    - Apply through banks
    """)

# -------------------------------------------------
# ABOUT PAGE
# -------------------------------------------------
if page == "About":
    st.header("ℹ️ About KisanSense GenAI")
    st.write(
        "KisanSense GenAI is built to bridge the knowledge gap between "
        "agricultural experts and farmers using AI-inspired advisory systems. "
        "The platform is modular, scalable, and designed for real-world rural use."
    )

    st.markdown("### 🔮 Future Scope")
    st.write(
        "- Integration with Large Language Models (LLMs)\n"
        "- Offline FAISS-based knowledge retrieval\n"
        "- Voice-based interaction\n"
        "- District-specific advisory"
    )

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.divider()
st.caption("© 2026 KisanSense GenAI | AI for Farmers 🌾")




















