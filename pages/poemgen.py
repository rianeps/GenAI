import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv  

load_dotenv()

api_key = os.getenv('API_KEY')

def poem_generator(user_text):
    genai.configure(api_key=api_key) 
    model = genai.GenerativeModel('gemini-pro')

    chat_model = genai.GenerativeModel('gemini-pro')
    chat = chat_model .start_chat(history=[])

    response = chat.send_message(f"Can you write poetry {user_text}. The poem should have short lines. If the topic of the poem is explicit siply ask the user to choose another topic.")
    st.write(response.text)
    # response = chat.send_message("")
    # return response.text

def show():
    st.markdown("# Poem Generator in the style of your favourite artists")
    key2 = st.session_state.get("user_text", 1)       
    user_text = st.text_input("Enter your text:", key=key2)
    if st.button("Generate poem"):
        poem_generator(user_text)
        

if __name__ == "__main__":
    show()