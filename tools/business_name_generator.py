# File: business_name_generator.py
import streamlit as st
import cohere

st.set_page_config(page_title="Startup Name Generator 🚀", page_icon="🏢")
st.title("🚀 Business Name Generator")
st.subheader("Generate catchy brand names")

api_key = st.text_input("🔑 Cohere API Key", type="password")
idea = st.text_input("💡 Describe your business idea")

if st.button("Generate Names"):
    if api_key and idea:
        co = cohere.Client(api_key)
        prompt = f"Suggest 5 catchy business names for: {idea}"
        response = co.generate(model="command-r-plus", prompt=prompt, max_tokens=100)
        st.success("💼 Name Ideas:")
        st.write(response.generations[0].text.strip())
