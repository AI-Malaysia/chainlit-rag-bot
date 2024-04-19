# chainlit-rag-bot

## A Simple RAG Chatbot with Chainlit, OpenAI, ChromaDB, and LangChain

Build a Simple RAG Chatbot with Chainlit, OpenAI, ChromaDB, and LangChain. Please insert your own OpenAI Api key.

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

Make sure to enter your own OpenAI_API and New_sAPI keys in news_search_audio

os.environ["OPENAI_API_KEY"] = "sk-"

os.environ['NEWS_API_KEY'] = "="
