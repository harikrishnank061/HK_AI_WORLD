# File: recipe_generator.py
import streamlit as st
import cohere

st.set_page_config(page_title="Recipe Creator 🍲", page_icon="👩‍🍳")
st.title("👩‍🍳 Recipe Generator")
st.subheader("Create recipes from ingredients")

api_key = st.text_input("🔑 Cohere API Key", type="password")
ingredients = st.text_area("🥕 Enter ingredients (comma-separated)")

if st.button("Get Recipe"):
    if api_key and ingredients:
        co = cohere.Client(api_key)
        prompt = f"Create a recipe using only: {ingredients}"
        response = co.generate(model="command-r-plus", prompt=prompt, max_tokens=400)
        st.success("🍽️ Recipe:")
        st.write(response.generations[0].text.strip())
