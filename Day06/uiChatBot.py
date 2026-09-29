import streamlit as st
import ollama

st.title("My AI Chatbot Application")

st.markdown("**_Welcome to my AI chatbot application! This chatbot is designed to provide answers in a friendly and funny manner._**")
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.chat_input("Ask me anything:")

if question:

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.write(question)

  
    response = ollama.chat(
        model="llama3.2:3b",
        messages=st.session_state.messages
    )

    answer = response["message"]["content"]
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    with st.chat_message("assistant"):
        st.write(answer)


    