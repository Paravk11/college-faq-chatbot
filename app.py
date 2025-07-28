import streamlit as st
import pandas as pd
import google.generativeai as genai

# Gemini API Key
genai.configure(api_key="AIzaSyAqYKyniCsK0O-SGjhXUB0S-RnmqhKFwdk")

# Supported model (v1beta compatible)
model = genai.GenerativeModel("gemini-2.5-pro")

# Load CSV
df = pd.read_csv("college_faq_data.csv")

def generate_prompt(user_question):
    context = "\n".join([f"Q: {q}\nA: {a}" for q, a in zip(df['Question'], df['Answer'])])
    return f"{context}\n\nUser: {user_question}\nAI:"

# Streamlit App
st.title("College FAQ Chatbot 🤖")
user_input = st.text_input("Ask your college-related question:")

if user_input:
    prompt = generate_prompt(user_input)
    response = model.generate_content(prompt)
    st.markdown(f"**Answer:** {response.text}")
