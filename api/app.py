from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
from langchain_core.runnables import RunnableParallel, RunnableLambda
import uvicorn
import os
# from langchain_community.llms import Ollama
from dotenv import load_dotenv
from pydantic import BaseModel

# Load environment variables
load_dotenv()

# Verify API key is loaded
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables")

os.environ["OPENAI_API_KEY"] = api_key

# Define input models
# class TopicInput(BaseModel):
#     topic: str

# Initialize FastAPI
app = FastAPI(
    title="Langchain API",
    description="A simple API for Langchain integration",
    version="1.0"
)

# Create chat model
model = ChatOpenAI(temperature=0.7)

# Create essay chain
essay_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that writes essays."),
    ("user", "Write an essay about {topic} in 100 words.")
])
# essay_chain = RunnableParallel({
#     "essay": essay_prompt | model
# })

# Create poem chain
poem_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a creative poet."),
    ("user", "Write a poem about {topic} in 100 words.")
])
poem_chain = RunnableParallel({
    "poem": poem_prompt | model
})

# Add routes
add_routes(
    app,
    essay_prompt | model,
    path="/essay",
    enabled_endpoints=["invoke"]
)

add_routes(
    app,
    poem_chain,
    path="/poem",
    enabled_endpoints=["invoke"]
)

# Add a root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Langchain API"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
