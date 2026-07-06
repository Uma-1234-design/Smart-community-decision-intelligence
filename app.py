import streamlit as st
import google.generativeai as genai
st.title("Smart Community Decision Intelligence Platform")
key=st.text_input("Gemini API Key",type="password")
q=st.text_area("Ask a community question")
if key:
    genai.configure(api_key=key)
    if st.button("Generate") and q:
        m=genai.GenerativeModel("gemini-1.5-flash")
        st.write(m.generate_content(q).text)
