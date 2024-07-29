import os
import streamlit as st
import google.generativeai as genai

api_key = st.secrets["general"]["API_KEY"]


def sarc_detect(user_text):
    genai.configure(api_key=api_key) 
    model = genai.GenerativeModel('gemini-pro')

    chat_model = genai.GenerativeModel('gemini-pro')
    chat = chat_model .start_chat(history=[])

    response = chat.send_message(f"Can you tell me whether {user_text} is sarcastics or not. If it is sarcastic tell me how you found that out.")
    st.write(response.text)
    # response = chat.send_message("")
    # return response.text

def show():
    st.markdown("# Sarcasm Detection in Customer Reviews")
    key1 = st.session_state.get("user_text", 1)       
    user_text = st.text_input("Enter your text:", key=key1)
    if st.button("Detect sarcasm"):
        sarc_detect(user_text)
        

if __name__ == "__main__":
    show()