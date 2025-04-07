import requests
import streamlit as st


def get_essay(topic):
    response = requests.post(
        "http://127.0.0.1:8000/essay/invoke",
        json={"input": {"topic": topic}}
    )
    return response.json()['output']['content']

def get_poem(topic):
    response = requests.post(
        "http://127.0.0.1:8000/poem/invoke",
        json={"input": {"topic": topic}}
    )
    return response.json()['output']['poem']['content']


st.title("Langchain API Client")
input_text = st.text_input("Write an essay about:")
input_text2 = st.text_input("Write a poem about:")

if input_text:
    st.write(get_essay(input_text))

if input_text2:
    st.write(get_poem(input_text2))
