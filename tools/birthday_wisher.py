# File: birthday_wisher.py
import streamlit as st
import cohere

st.set_page_config(page_title="Birthday Wish Generator 🎉", page_icon="🎂")
st.title("🎂 AI Birthday Wish")
st.subheader("Craft heartfelt birthday messages")

api_key = st.text_input("🔑 Cohere API Key", type="password")
recipient = st.text_input("🎁 Who is the wish for?")
tone = st.selectbox("😊 Tone", ["Sweet", "Funny", "Heartfelt", "Casual"])

if st.button("Generate Wish"):
    if api_key and recipient:
        co = cohere.Client(api_key)
        prompt = f"Write a {tone.lower()} birthday wish for {recipient}."
        response = co.generate(model="command-r-plus", prompt=prompt, max_tokens=150)
        st.success("🎉 Birthday Wish:")
        st.write(response.generations[0].text.strip())
