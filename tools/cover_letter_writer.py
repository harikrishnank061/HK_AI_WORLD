# File: cover_letter_writer.py
import streamlit as st
import cohere

st.set_page_config(page_title="Cover Letter Writer 📬", page_icon="📝")
st.title("📬 AI Cover Letter Generator")
st.subheader("Generate personalized cover letters")

api_key = st.text_input("🔑 Cohere API Key", type="password")
job = st.text_input("💼 Job Role")
about_you = st.text_area("🧑 Tell me about yourself")

if st.button("Write Cover Letter"):
    if api_key and job and about_you:
        co = cohere.Client(api_key)
        prompt = f"Write a professional cover letter for the position of {job}. About me: {about_you}"
        response = co.generate(model="command-r-plus", prompt=prompt, max_tokens=600)
        st.success("📨 Cover Letter:")
        st.write(response.generations[0].text.strip())
