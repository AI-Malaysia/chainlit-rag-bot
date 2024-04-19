# chainlit-rag-bot

## Simple Streamlit app demonstrating LLM interaction with an API

This is a simple application built using OpenAI APIs (whisper-1, tts-1, GPT-3.5-turbo-instruct), streamlit and LangChain,  the app utilizes the `APIChain` component from LangChain to make external API calls and retrieve data from News api https://newsapi.org/

## Prerequisites

Before running this app, make sure you have the following installed:

- Python (version 3.10 or higher)
- Poetry (dependency management tool)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ai-malaysia/audio-newsapi-chatbot.git
```

2. Navigate to the project directory:

```bash
cd audio-newsapi-chatbot
```

3. Install the dependencies using Poetry:

```bash
poetry install
```

5. Usage

```bash
streamlit run news_search_audio.py
```

Make sure to enter your own OpenAI_API and New_sAPI keys in news_search_audio

os.environ["OPENAI_API_KEY"] = "sk-"

os.environ['NEWS_API_KEY'] = "="
