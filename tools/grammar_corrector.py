# File: grammar_corrector.py
import streamlit as st
import cohere

st.set_page_config(page_title="Grammar Corrector ✍️", page_icon="📝")
st.title("✍️ Grammar & Spelling Corrector")
st.subheader("Fix grammar, spelling, and punctuation")

api_key = st.text_input("🔑 Cohere API Key", type="password")
text = st.text_area("🧾 Enter your sentence or paragraph")

if st.button("Correct"):
    if api_key and text.strip():
        co = cohere.Client(api_key)
        prompt = f"Correct the grammar, spelling, and punctuation:\nOriginal: {text}\nCorrected:"
        response = co.generate(model="command-r-plus", prompt=prompt, max_tokens=300)
        st.success("Corrected Text:")
        st.write(response.generations[0].text.strip())
    else:
        st.warning("Enter both text and API key.")
