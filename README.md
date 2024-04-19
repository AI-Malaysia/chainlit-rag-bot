# chainlit-rag-bot

## A Simple RAG Chatbot with Chainlit, OpenAI, ChromaDB, and LangChain

Build a Simple RAG Chatbot with Chainlit, OpenAI, ChromaDB, and LangChain. Please insert your own OpenAI Api key.

Main reference: This project is based on the Medium article 'Build a Chatbot in Minutes with Chainlit, GPT-4, and Langchain' (https://medium.com/@cleancoder/build-a-chatbot-in-minutes-with-chainlit-gpt-4-and-langchain-7690968578f0). The original code was sourced from https://github.com/satwikide. I have adapted it by incorporating OpenAI APIs (GPT-3.5-turbo and embedding models), along with fixing issues related to:
- PDF content handling
- Message text attributes
- Other minor adjustments

## Prerequisites

Before running this app, make sure you have the following installed:

- Python (version 3.10 or higher)
- Poetry (dependency management tool)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ai-malaysia/chainlit-rag-bot.git
```

2. Navigate to the project directory:

```bash
cd chainlit-rag-bot
```

3. Install the dependencies using Poetry:

```bash
poetry install
```

5. Usage

```bash
streamlit run app_RAG.py
```

Make sure to enter your own OpenAI_API key

openai_api_key= "sk-"

