import streamlit as st

st.set_page_config(page_title="KisanSense GenAI", layout="centered")

st.title("🌾 KisanSense GenAI")
st.caption("AI-powered multilingual agricultural chatbot")

# ---------- Language Selector ----------
language = st.selectbox(
    "Select your language / మీ భాషను ఎంచుకోండి / अपनी भाषा चुनें",
    ["English", "Telugu", "Hindi", "Tamil"]
)

# ---------- Translation Dictionary ----------
translations = {
    "English": {
        "aphids": "Aphids Control",
        "answer_aphids": "Spray Neem Oil 3–5 ml per litre. Use Imidacloprid if severe. Avoid excess nitrogen."
    },
    "Telugu": {
        "aphids": "ఆఫిడ్స్ నియంత్రణ",
        "answer_aphids": "నీమ్ ఆయిల్ 3–5 మి.లీ లీటర్ నీటిలో కలిపి పిచికారీ చేయాలి. ఎక్కువ నత్రజని ఎరువులు వేయకండి."
    },
    "Hindi": {
        "aphids": "एफिड्स नियंत्रण",
        "answer_aphids": "नीम तेल 3–5 मि.ली. प्रति लीटर पानी में छिड़कें। अधिक नाइट्रोजन से बचें।"
    },
    "Tamil": {
        "aphids": "அஃபிட்ஸ் கட்டுப்பாடு",
        "answer_aphids": "நீம் எண்ணெய் 3–5 மி.லி. ஒரு லிட்டர் தண்ணீரில் தெளிக்கவும்."
    }
}

# ---------- Chat History ----------
if "chat" not in st.session_state:
    st.session_state.chat = []

# ---------- User Input ----------
user_query = st.chat_input("Type your question here...")

def get_advice(query, lang):
    q = query.lower()

    if "aphid" in q or "ఆఫిడ్" in q or "एफिड" in q:
        return translations[lang]["answer_aphids"]

    return {
        "English": "Please consult your local agriculture officer for this issue.",
        "Telugu": "ఈ సమస్యకు స్థానిక వ్యవసాయ అధికారిని సంప్రదించండి.",
        "Hindi": "इस समस्या के लिए स्थानीय कृषि अधिकारी से संपर्क करें।",
        "Tamil": "இந்த பிரச்சனைக்கு அருகிலுள்ள வேளாண் அதிகாரியை அணுகவும்."
    }[lang]

# ---------- Chatbot Flow ----------
if user_query:
    st.session_state.chat.append(("user", user_query))
    bot_reply = get_advice(user_query, language)
    st.session_state.chat.append(("bot", bot_reply))

# ---------- Display Chat ----------
for role, msg in st.session_state.chat:
    if role == "user":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)


















