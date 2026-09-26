import streamlit as st
st.title("My first Streamlit App!!!")
st.markdown("**_Welcome to my AI chatbot application!_**")
name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.write(f"Hello, {name}!")