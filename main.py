from model import *
import streamlit as st

st.title("English to French Transaltor")

if 'input_text' not in st.session_state:
    st.session_state['input_text'] = ''

if 'translated_lines' not in st.session_state:
    st.session_state['translated_lines'] = []

input_text = st.text_area("Enter your English Text", value=st.session_state['input_text'], key="input_text")

if st.button("Translate"):
    if input_text.strip():
        lines = input_text.split("\n")  # Split input text into lines
        translated_lines = []  # List to store translated lines
        for line in lines:  # Loop through each line
            translated_result = translator(line)  # Pass each line to the translator
            translated_text = translated_result[0]['translation_text']  # Get the translated text
            translated_lines.append(translated_text)  # Append translated text to the list
            
            st.session_state['translated_lines'] = translated_lines
         
        for translated_line in translated_lines:
            st.write(translated_line)  # Display each translated line separately
    else:
        st.write("Error! Please write something in the text area first!")

# Reset button logic
if st.button("Reset"):
    if input_text.strip():
        # Reset both input and translated text
        st.session_state['input_text'] = ' '
        st.session_state['translated_lines'] = []
    else:
        st.write("Error! Please write something in the text area first!")
    


# HOW TO RUN: streamlit run main.py