import streamlit as st
import google.generativeai as genai

st.title("Smart Community Decision Intelligence Platform")

api_key = st.text_input("Enter Gemini API Key", type="password")
question = st.text_area("Ask a community question")

if api_key:
    genai.configure(api_key=api_key)

    if st.button("Generate Response"):
        if question:
            try:
                model = genai.GenerativeModel("gemini-2.5-pro")
                response = model.generate_content(question)
                st.success(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please enter a question.")
