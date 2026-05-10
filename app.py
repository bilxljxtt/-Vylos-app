import streamlit as st
import pandas as pd
import openai
from supabase import create_client, Client

st.set_page_config(page_title="Anti-Gravity Questionnaire", page_icon="🚀", layout="centered")

st.title("Anti-Gravity Questionnaire")
st.write("Welcome to the Anti-Gravity assessment! Please answer the following 20 questions.")

with st.form("questionnaire_form"):
    # Placeholder for the 20 questions
    for i in range(1, 21):
        st.radio(
            f"Question {i}: Example Question?", 
            ["Option A", "Option B", "Option C"], 
            key=f"q{i}"
        )

    submitted = st.form_submit_button("Submit Answers")
    if submitted:
        st.success("Your answers have been submitted successfully! We are processing your results.")
        # Future Logic: Send data to OpenAI and save results in Supabase
