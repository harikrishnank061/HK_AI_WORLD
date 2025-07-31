import streamlit as st
import cohere

st.set_page_config(page_title="Mood Buddy 🧘", page_icon="💬")
st.title("🧘 Mood Buddy")
st.subheader("Reflect on your thoughts & get support tips")

api_key = st.text_input("🔑 Enter your Cohere API Key", type="password")
entry = st.text_area("📝 Write how you feel today")

if st.button("Get Support"):
    if not api_key or not entry.strip():
        st.warning("Please enter your API key and mood journal.")
    else:
        with st.spinner("Analyzing your mood..."):
            try:
                co = cohere.Client(api_key)
                prompt = f"""
                You are a friendly mental health assistant.
                Analyze the following journal entry, identify the writer’s emotional tone, and give gentle advice or an affirmation.

                Entry: {entry}

                Respond like:
                🧠 Mood: 
                ❤️ Support Tip:
                🌈 Affirmation:
                """

                response = co.generate(
                    model="command-r-plus",
                    prompt=prompt,
                    max_tokens=500,
                    temperature=0.7
                )

                st.success("Here's your emotional insight:")
                st.markdown(response.generations[0].text.strip())
            except Exception as e:
                st.error(f"Error: {e}")
