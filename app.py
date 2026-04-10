import streamlit as st
import os

from modules.stt import transcribe_audio
from intent import detect_intent
from modules.tools import create_file, write_code, summarize_text

st.set_page_config(page_title="AI Voice Agent", page_icon="🎙️", layout="centered")

st.title("🎙️ AI Voice Agent")
st.markdown("Upload your voice command and let AI perform actions 🚀")

# Upload
audio_file = st.file_uploader("📤 Upload Audio File", type=["wav", "mp3"])

if audio_file is not None:
    file_path = "temp_audio.wav"

    with open(file_path, "wb") as f:
        f.write(audio_file.read())

    st.audio(file_path)

    with st.spinner("🧠 Processing your voice..."):
        text = transcribe_audio(file_path)
        intents = detect_intent(text)

        results = []

        for intent in intents:
            if intent == "create_file":
                results.append(create_file())

            elif intent == "write_code":
                results.append(write_code())

            elif intent == "summarize":
                results.append(summarize_text(text))

            else:
                results.append("No action taken")

    st.success("✅ Processing Complete!")

    # Output sections
    st.subheader("📝 Transcribed Text")
    st.info(text)

    st.subheader("🎯 Detected Intents")
    st.write(intents)

    st.subheader("⚡ Actions Performed")
    for res in results:
        st.success(res)