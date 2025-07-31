# File: poem_generator.py
import streamlit as st
import cohere

st.set_page_config(page_title="Poem Generator ✨", page_icon="🖋️")
st.title("🖋️ AI Poem Generator")
st.subheader("Generate creative poems")

api_key = st.text_input("🔑 Cohere API Key", type="password")
topic = st.text_input("🧠 Enter a poem topic")

if st.button("Generate Poem"):
    if api_key and topic:
        co = cohere.Client(api_key)
        prompt = f"Write a beautiful poem about: {topic}"
        response = co.generate(model="command-r-plus", prompt=prompt, max_tokens=300)
        st.success("Here’s your poem:")
        st.write(response.generations[0].text.strip())
