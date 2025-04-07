from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv
from pathlib import Path

# Get the current directory and .env file path
current_dir = Path(__file__).parent.absolute()
env_path = current_dir / '.env'

print(f"Current directory: {current_dir}")
print(f".env file path: {env_path}")
print(f".env file exists: {env_path.exists()}")

# Load environment variables
load_dotenv(dotenv_path=env_path)

# Get API keys
openai_key = os.getenv("OPENAI_API_KEY")
langchain_key = os.getenv("LANGCHAIN_API_KEY")

print("\nAPI Keys loaded:")
print(f"OpenAI API Key exists: {'Yes' if openai_key else 'No'}")
print(f"OpenAI API Key: {openai_key}..." if openai_key else "No OpenAI API Key found")
print(f"Langchain API Key exists: {'Yes' if langchain_key else 'No'}")
print(f"OpenAI API Key: {langchain_key}..." if langchain_key else "No langchain API Key found")
# Set environment variables
os.environ["OPENAI_API_KEY"] = openai_key
os.environ["LANGCHAIN_API_KEY"] = langchain_key
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Initialize the chat model
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that can answer questions."),
    ("user", "Question: {question}")
])

# Initialize Streamlit interface
st.title("Langchain Demo")
input_text = st.text_input("Enter your question")

# Initialize LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")  # Changed from gpt-4o-mini to gpt-3.5-turbo
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text})) 