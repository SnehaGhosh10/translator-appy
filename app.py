import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import os
import base64
import tempfile

st.set_page_config(page_title="🌍 AI Translator", page_icon="🌐")
st.title("🌍 AI Translator with Text-to-Speech")
st.markdown("Translate text and listen to it out loud!")

# Language options
LANGUAGES = {
    'english': 'en', 'hindi': 'hi', 'bengali': 'bn', 'french': 'fr',
    'german': 'de', 'spanish': 'es', 'chinese': 'zh-CN', 'tamil': 'ta',
    'telugu': 'te', 'marathi': 'mr', 'arabic': 'ar', 'japanese': 'ja',
    'korean': 'ko'
}

# User input
text = st.text_area("🔤 Enter text to translate:")

col1, col2 = st.columns(2)
with col1:
    src_lang = st.selectbox("From Language", options=LANGUAGES.keys())
with col2:
    dest_lang = st.selectbox("To Language", options=LANGUAGES.keys())

if st.button("🔁 Translate and Speak"):
    if text:
        try:
            translated = GoogleTranslator(source=LANGUAGES[src_lang], target=LANGUAGES[dest_lang]).translate(text)
            st.success("✅ Translated Text:")
            st.write(translated)

            tts = gTTS(translated, lang=LANGUAGES[dest_lang])
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
                tts.save(tmp.name)
                audio_file = tmp.name

            audio_html = f'''
            <audio autoplay controls>
                <source src="data:audio/mp3;base64,{base64.b64encode(open(audio_file,"rb").read()).decode()}">
            </audio>
            '''
            st.markdown(audio_html, unsafe_allow_html=True)
            os.remove(audio_file)
        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("Please enter some text.")
