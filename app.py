import streamlit as st
import requests

st.title("Anon Board")


with st.form("Write a message"):
    message = st.text_input("Your message: ")
    submit = st.form_submit_button("Send")

if submit:
    data = {"message": message}
    response = requests.post("http://127.0.0.1:8000/messages", json=data)
    st.write(response.json())

    