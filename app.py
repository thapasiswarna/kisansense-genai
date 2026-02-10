import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="KisanSense Platform",
    page_icon="🌾",
    layout="wide"
)

# ---------------- SESSION STATE ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "farmer" not in st.session_state:
    st.session_state.farmer = {}

# ---------------- LOGIN PAGE ----------------
def login_page():
    st.markdown("## 🌾 KisanSense – Farmer Login")

    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Farmer Name")
        village = st.text_input("Village")
        crop = st.selectbox("Primary Crop", ["Rice", "Wheat", "Cotton", "Maize"])
    with col2:
        phone = st.text_input("Mobile Number")
        language = st.selectbox("Preferred Language", ["English", "Telugu", "Hindi", "Tamil"])

    if st.button("Login"):
        st.session_state.logged_in = True
        st.session_state.farmer = {
            "name": name,
            "village": village,
            "crop": crop,
            "phone": phone,
            "language": language
        }
        st.rerun()

# ---------------- TRANSLATION LOGIC ----------------
def translate(text, lang):
    translations = {
        "Telugu": {
            "Welcome": "స్వాగతం",
            "Ask Question": "మీ ప్రశ్నను అడగండి"
        },
        "Hindi": {
            "Welcome": "स्वागत है",
            "Ask Question": "अपना प्रश्न पूछें"
        },
        "Tamil": {
            "Welcome": "வரவேற்கிறோம்",
            "Ask Question": "உங்கள் கேள்வியை கேளுங்கள்"
        }
    }
    return translations.get(lang, {}).get(text, text)

# ---------------- AI ADVISORY ----------------
def ai_advisory(q, lang):
    q = q.lower()
    if "aphid" in q:
        return {
            "English": "Spray Neem Oil 3–5 ml per litre. Avoid excess nitrogen.",
            "Telugu": "నీమ్ ఆయిల్ 3–5 మి.లీ లీటర్ నీటిలో పిచికారీ చేయాలి.",
            "Hindi": "नीम तेल 3–5 मि.ली. प्रति लीटर पानी में छिड़कें।",
            "Tamil": "நீம் எண்ணெய் 3–5 மி.லி. தெளிக்கவும்."
        }[lang]
    return {
        "English": "Please consult local agriculture officer.",
        "Telugu": "స్థానిక వ్యవసాయ అధికారిని సంప్రదించండి.",
        "Hindi": "स्थानीय कृषि अधिकारी से संपर्क करें।",
        "Tamil": "உள்ளூர் வேளாண் அதிகாரியை அணுகவும்."
    }[lang]

# ---------------- DASHBOARD ----------------
def dashboard():
    farmer = st.session_state.farmer
    lang = farmer["language"]

    st.sidebar.title("🌾 KisanSense")
    page = st.sidebar.radio(
        "Menu",
        ["Dashboard", "AI Assistant", "Crop Recommendation", "Disease Detection",
         "Schemes", "Weather & Advisory", "Notifications", "About", "Contact"]
    )

    # ---------------- DASHBOARD HOME ----------------
    if page == "Dashboard":
        st.markdown(f"## {translate('Welcome', lang)}, {farmer['name']} 👋")
        st.info(f"Village: {farmer['village']} | Crop: {farmer['crop']}")

        col1, col2, col3 = st.columns(3)
        col1.success("🌱 Crop Advisory")
        col2.info("🐛 Disease Detection")
        col3.warning("🤖 AI Assistant")

    # ---------------- AI ASSISTANT ----------------
    if page == "AI Assistant":
        st.header("🤖 AI Assistant")
        q = st.text_input(translate("Ask Question", lang))
        if q:
            st.success(ai_advisory(q, lang))

    # ---------------- CROP RECOMMENDATION ----------------
    if page == "Crop Recommendation":
        st.header("🌱 Recommended Crops")
        st.write("Based on soil, season, and region")
        st.success("Recommended: Rice, Pulses, Millets")

    # ---------------- DISEASE DETECTION ----------------
    if page == "Disease Detection":
        st.header("📸 Crop Disease Detection")
        st.file_uploader("Upload leaf image (AI-ready module)")
        st.info("Disease detection model will analyze this image")

    # ---------------- SCHEMES ----------------
    if page == "Schemes":
        st.header("🏛️ Government Schemes")
        st.markdown("""
        **PM-Kisan Samman Nidhi**
        - ₹6000 per year  
        - Direct Bank Transfer  

        **Crop Insurance (PMFBY)**
        - Protection from crop loss
        """)

    # ---------------- WEATHER ----------------
    if page == "Weather & Advisory":
        st.header("🌦️ Weather & Advisory")
        st.warning("Weather integration ready")
        st.write("Advisory: Avoid spraying pesticides today")

    # ---------------- NOTIFICATIONS ----------------
    if page == "Notifications":
        st.header("🔔 Notifications")
        st.info("No new alerts")

    # ---------------- ABOUT ----------------
    if page == "About":
        st.header("ℹ️ About KisanSense")
        st.write("""
        KisanSense is a farmer-first digital platform combining AI,
        advisory systems, and multilingual interaction.
        """)

    # ---------------- CONTACT ----------------
    if page == "Contact":
        st.header("📞 Contact")
        st.write("Email: support@kisansense.ai")
        st.write("Helpline: 1800-000-000")

# ---------------- MAIN ----------------
if not st.session_state.logged_in:
    login_page()
else:
    dashboard()






















