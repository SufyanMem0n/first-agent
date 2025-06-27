import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import asyncio
import nest_asyncio

# Apply patch to allow nested event loops (for Streamlit)
nest_asyncio.apply()

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

st.title("🧠 SM_Assistant (By Sufyan)")
user_input = st.text_input("Ask something:", "")

if user_input:
    with st.spinner("Thinking..."):
        try:
            response = model.generate_content(user_input)
            st.success(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
