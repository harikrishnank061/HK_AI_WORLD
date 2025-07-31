import streamlit as st
import cohere

# UI setup
st.set_page_config(page_title="Plant Buddy 🌿", page_icon="🌱")
st.title("🌿 Plant Buddy")
st.subheader("AI-Powered Plant Care Advisor")

# Get API key from user
api_key = st.text_input("🔑 Enter your Cohere API Key", type="password")

# Get plant name
plant = st.text_input("🌱 Enter a plant name (e.g., Aloe Vera)")

if st.button("Get Care Tips"):
    if not api_key.strip():
        st.warning("Please enter your Cohere API key.")
    elif not plant.strip():
        st.warning("Please enter a plant name.")
    else:
        with st.spinner("Talking to your leafy friend... 🌿"):
            try:
                co = cohere.Client(api_key)
                prompt = f"""
                You are a friendly plant care assistant. Give detailed care tips for the plant: {plant}.
                Respond in this exact format:
                💧 Watering: 
                ☀️ Light Requirements: 
                🐛 Common Issues: 
                🌿 Bonus Tip: 
                🌸 Emoji Summary: 
                Make sure to write each section completely and clearly.
                """

                response = co.generate(
                    model="command-r-plus",
                    prompt=prompt,
                    max_tokens=800,
                    temperature=0.7,
                    stop_sequences=["---"]
                )

                st.success("Here's how to care for your plant:")
                st.markdown(response.generations[0].text.strip())
            except Exception as e:
                st.error(f"Error: {e}")
