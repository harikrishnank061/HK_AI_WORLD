# File: quote_generator.py
import streamlit as st
import cohere

st.set_page_config(page_title="Motivational Quotes 💡", page_icon="✨")
st.title("✨ Motivation Generator")
st.subheader("Get a fresh motivational quote")

api_key = st.text_input("🔑 Cohere API Key", type="password")

if st.button("Inspire Me"):
    if api_key:
        co = cohere.Client(api_key)
        prompt = "Give me a short motivational quote to inspire someone who's feeling stuck."
        response = co.generate(model="command-r-plus", prompt=prompt, max_tokens=60)
        st.success("💬 Your Quote:")
        st.write(response.generations[0].text.strip())
