# Q&A Chatbot
#from langchain.llms import OpenAI
import os
import pathlib
import textwrap
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv


## take environment variables from .env.
load_dotenv() 

## Configure the gemini api key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# initializ the model
model = genai.GenerativeModel("gemini-pro")

# function to load GeminiPro model and its responses
def get_gemini_response(question):
    model.generate_content(question)
    response = model.generate_content(question)
    return response.text

##initialize our streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")
input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

## When submit button is clicked
if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)
