import streamlit as st
from googletrans import Translator

# Set page config
st.set_page_config(page_title="🌍 AI Translator App", page_icon="🌐")
st.title("🌍 AI Translator App")
st.markdown("Translate text between languages in real-time using AI.")

# Language options
LANGUAGES = {
    'en': 'English',
    'hi': 'Hindi',
    'bn': 'Bengali',
    'fr': 'French',
    'es': 'Spanish',
    'de': 'German',
    'zh-cn': 'Chinese (Simplified)',
    'ja': 'Japanese',
    'ko': 'Korean',
    'ru': 'Russian',
    'ar': 'Arabic',
    'ta': 'Tamil',
    'te': 'Telugu',
    'gu': 'Gujarati',
}

lang_codes = list(LANGUAGES.keys())
translator = Translator()

# Input text
text_input = st.text_area("✏️ Enter text to translate:")

col1, col2 = st.columns(2)
with col1:
    src_lang = st.selectbox("From Language", options=lang_codes, format_func=lambda x: LANGUAGES[x])
with col2:
    dest_lang = st.selectbox("To Language", options=lang_codes, format_func=lambda x: LANGUAGES[x])

# Translate on button click
if st.button("🔁 Translate"):
    if text_input:
        with st.spinner("Translating..."):
            result = translator.translate(text_input, src=src_lang, dest=dest_lang)
            st.success("✅ Translated Text:")
            st.write(result.text)
    else:
        st.warning("Please enter some text to translate.")
