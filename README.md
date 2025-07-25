🌍AI-Powered Translator with Text-to-Speech
This is an interactive multilingual translator built with Streamlit, integrating GoogleTranslator (via deep_translator) and gTTS (Google Text-to-Speech) to not only translate text between multiple languages but also read it aloud using natural voice synthesis.

🛠️ Tech Stack:

Python

Streamlit – for the UI/UX frontend

deep_translator – for translation powered by Google Translate API

gTTS – for speech synthesis from translated text

tempfile & base64 – for audio streaming directly in the browser

🌍 Features:

Translate text across 12+ popular languages

Instant playback of translated text via text-to-speech

Responsive, clean UI with select boxes for language input/output

Embedded audio player for real-time listening

Error handling and temporary file cleanup for smoother UX

🌐 Supported Languages:

English, Hindi, Bengali, French, German, Spanish, Chinese, Tamil, Telugu, Marathi, Arabic, Japanese, Korean

🎯 How It Works:

User enters text and selects the source and target languages.

On clicking "🔁 Translate and Speak":

The app uses GoogleTranslator to translate the text.

The result is spoken out loud using gTTS, rendered as an embedded audio player.

Users can read and listen to the translated output instantly.

💡 Example Use Case:

Input (English): "Good morning, how are you?"
Target Language: Hindi
Output (Text): "सुप्रभात, आप कैसे हैं?"
Output (Audio): ✅ Played automatically in Hindi




