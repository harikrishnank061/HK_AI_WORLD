# File: tweet_generator.py
import streamlit as st
import cohere

st.set_page_config(page_title="Tweet Generator 🐦", page_icon="🐤")
st.title("🐤 Tweet Generator")
st.subheader("Create engaging tweets on any topic")

api_key = st.text_input("🔑 Cohere API Key", type="password")
topic = st.text_input("📢 Tweet about:")

if st.button("Generate Tweet"):
    if api_key and topic:
        co = cohere.Client(api_key)
        prompt = f"Write a creative, short tweet about: {topic}"
        response = co.generate(model="command-r-plus", prompt=prompt, max_tokens=80)
        st.success("Here's your tweet:")
        st.write(response.generations[0].text.strip())
