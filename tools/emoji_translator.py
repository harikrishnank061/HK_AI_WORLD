# File: emoji_translator.py
import streamlit as st
import cohere

st.set_page_config(page_title="Emoji Translator 😊", page_icon="😀")
st.title("😀 Emoji Translator")
st.subheader("Convert your message into emojis")

api_key = st.text_input("🔑 Cohere API Key", type="password")
message = st.text_input("💬 Enter a sentence")

if st.button("Translate to Emoji"):
    if api_key and message:
        co = cohere.Client(api_key)
        prompt = f"Translate this into emojis:\nText: {message}\nEmoji:"
        response = co.generate(model="command-r-plus", prompt=prompt, max_tokens=100)
        st.success("Emoji Translation:")
        st.write(response.generations[0].text.strip())
