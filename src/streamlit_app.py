import streamlit as st
from chatbot import Chatbot

# Load chatbot model
chatbot = Chatbot('chatbot_model.h5', 'intents.json')

st.title("AI-Powered Chatbot")

# User input
user_message = st.text_input("Enter your message:")

if st.button("Send"):
    response = chatbot.respond(user_message)
    st.write("Chatbot Response:", response)
