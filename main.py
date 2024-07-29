import streamlit as st
from pages import sarcasmdetector, poemgen

st.set_page_config(page_title="NLP Projects", page_icon="🗣️", layout="wide")

# Display title
st.title("NLP Projects")

# Create a horizontal navigation bar using st.columns()
col1, col2 = st.columns(2)

# Define icons for each page
project1_icon = "💡"
project2_icon = "🦜"

# Create buttons for each page with icons
project1_button = col1.button(f"{project1_icon} Sarcasm Detector")
project2_button = col2.button(f"{project2_icon} Poem Generator")

# Use st.session_state to store the selected page
if 'selected_page' not in st.session_state:
    st.session_state.selected_page = "Sarcasm Detector"  # Default page

# Determine the selected page based on the button click
if project1_button:
    st.session_state.selected_page = "Sarcasm Detector"
elif project2_button:
    st.session_state.selected_page = "Poem Generator"


# Display different content based on the selected menu item
if st.session_state.selected_page == "Sarcasm Detector":
    sarcasmdetector.show()
elif st.session_state.selected_page == "Poem Generator":
    poemgen.show()

