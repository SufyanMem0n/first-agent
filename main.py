import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load your .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Try initializing the model
try:
    model = genai.GenerativeModel("gemini-1.5-flash")  # or gemini-pro, etc.
except Exception as e:
    model = None
    st.warning(f"⚠️ Failed to load model: {e}")

# Streamlit UI
st.set_page_config(page_title="Gemini AI Assistant", page_icon="🔮")
st.title("🔮 Gemini AI Assistant (Free)")

user_input = st.text_input("Ask something:", "")

if user_input:
    if model is None:
        st.error("Model couldn't be loaded. Check your model name or API key.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = model.generate_content(user_input)
                st.success(response.text)
            except Exception as e:
                st.error(f"Error from Gemini: {e}")
