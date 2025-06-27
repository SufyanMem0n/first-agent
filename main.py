import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import logging

# --- Setup ---
load_dotenv()
logging.basicConfig(level=logging.INFO)

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("❌ GEMINI_API_KEY not found. Please add it to your .env file.")
    st.stop()

try:
    genai.configure(api_key=api_key)
except Exception as config_error:
    st.error("❌ Failed to configure Gemini API.")
    logging.error("Configuration error:", exc_info=True)
    st.stop()

# --- Initialize Model ---
model = None
init_error = None
try:
    model = genai.GenerativeModel("gemini-1.5-flash")  # You can also use "gemini-pro"
except Exception as e:
    init_error = str(e)
    logging.error("Model initialization failed:", exc_info=True)

# --- Streamlit UI ---
st.set_page_config(page_title="Gemini AI Assistant", page_icon="🤖")
st.title("🤖 Gemini AI Assistant (Free Tier)")

if init_error:
    st.warning("⚠️ Gemini model failed to load. Please check your API key or model name.")
    st.text(f"Details: {init_error}")
    st.stop()

user_input = st.text_input("Ask me anything:")

if user_input:
    with st.spinner("Thinking..."):
        try:
            response = model.generate_content(user_input)
            st.success(response.text)
        except Exception as e:
            st.error("❌ Something went wrong while generating content.")
            logging.error("Content generation error:", exc_info=True)
