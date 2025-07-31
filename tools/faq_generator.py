import streamlit as st
import cohere

st.set_page_config(page_title="FAQ Generator ❓", page_icon="📄")
st.title("📄 AI FAQ Generator")
st.subheader("Generate product or website FAQs using AI")

api_key = st.text_input("🔑 Enter your Cohere API Key", type="password")
product_desc = st.text_area("🛍️ Describe your product or website")

if st.button("Generate FAQs"):
    if not api_key.strip() or not product_desc.strip():
        st.warning("Please fill all fields.")
    else:
        try:
            co = cohere.Client(api_key)
            prompt = f"""
            Act as a product documentation writer. Generate 5 common FAQs and answers for the following product or service:
            {product_desc}

            Format:
            Q1: ...
            A1: ...
            Q2: ...
            A2: ...
            """

            response = co.generate(
                model="command-r-plus",
                prompt=prompt,
                max_tokens=600,
                temperature=0.6
            )

            st.success("Here are your FAQs:")
            st.markdown(response.generations[0].text.strip())
        except Exception as e:
            st.error(f"Error: {e}")
