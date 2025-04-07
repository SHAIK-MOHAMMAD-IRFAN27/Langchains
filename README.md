# Langchain Applications

This repository contains various applications built using LangChain, demonstrating different use cases and implementations of the LangChain framework.

## Project Structure

- `/agents`: Custom LangChain agents implementations
- `/rag`: Retrieval Augmented Generation implementations
- `/api`: API integrations and endpoints
- `/chatbot`: Chatbot implementations using LangChain

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file with your API keys and configurations:
```env
OPENAI_API_KEY=your_openai_api_key
# Add other required API keys
```

## Applications

### Chatbot
The chatbot implementation uses LangChain's conversation chains and memory components to create an intelligent chatbot.

### RAG (Retrieval Augmented Generation)
Implementation of document retrieval and question answering using LangChain's document loaders and retrievers.

### Agents
Custom agents built using LangChain's agent framework for specific tasks and workflows.

### API
API endpoints and integrations for various LangChain functionalities.

## Usage

Each subdirectory contains its own README with specific instructions for running and using the applications.

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request 