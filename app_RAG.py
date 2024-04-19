import os
from typing import List

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders.pdf import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.chroma import Chroma
from langchain.chains import (
    ConversationalRetrievalChain,
)
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.docstore.document import Document
from langchain.memory import ChatMessageHistory, ConversationBufferMemory
import chainlit as cl
import PyPDF2

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chat_model_deployment = os.getenv("OPENAI_CHAT_MODEL")

@cl.on_chat_start
async def on_chat_start():
    files = None

    # Wait for the user to upload a file
    while files == None:
        files = await cl.AskFileMessage(
            content="Please upload a text file to begin!",
            accept=["application/pdf"],
            max_size_mb=20,
            timeout=180,
        ).send()

    file = files[0]
    print(file)
    msg = cl.Message(
        content=f"Creating chunks for `{file.name}`...", disable_feedback=True
    )
    await msg.send()

    # Write the file to local file system
    if not os.path.exists("tmp"):
        os.makedirs("tmp")

    pdf_reader = PyPDF2.PdfReader(file.path)

    # Create a PDF writer object
    pdf_writer = PyPDF2.PdfWriter()

    # Add all pages from the input PDF
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])

    # Save the result as a new PDF
    with open(f"tmp/{file.name}", 'wb') as output_file:
        pdf_writer.write(output_file)

    pdf_loader = PyPDFLoader(file_path=f"tmp/{file.name}")

    # Split the text into chunks
    documents = pdf_loader.load_and_split(text_splitter=text_splitter)

    # Create a metadata for each chunk
    metadatas = [{"source": f"{i}-pl"} for i in range(len(documents))]

    msg.content = f"Creating embeddings for `{file.name}`. . ."
    await msg.update()

    # Create a Chroma vector store
    embeddings = OpenAIEmbeddings(
        openai_api_key=""
    ) 
    docsearch = await cl.make_async(Chroma.from_documents)(
        documents,
        embeddings
    )

    message_history = ChatMessageHistory()

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        output_key="answer",
        chat_memory=message_history,
        return_messages=True,
    )

    # Create a chain that uses the Chroma vector store
    chain = ConversationalRetrievalChain.from_llm(
        llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=""),
        chain_type="stuff",
        retriever=docsearch.as_retriever(),
        memory=memory,
        return_source_documents=True,
    )

    # Let the user know that the system is ready
    msg.content = f"Processing `{file.name}` done. You can now ask questions!"
    await msg.update()

    cl.user_session.set("chain", chain)

@cl.on_message
async def main(message: cl.Message):
    chain = cl.user_session.get("chain")  # type: ConversationalRetrievalChain
    cb = cl.AsyncLangchainCallbackHandler()
    res = await chain.acall(message.content, callbacks=[cb])
    answer = res["answer"]
    source_documents = res["source_documents"]  # type: List[Document]

    text_elements = []  # type: List[cl.Text]

    if source_documents:
        for source_idx, source_doc in enumerate(source_documents):
            source_name = f"source_{source_idx}"
            # Create the text element referenced in the message
            text_elements.append(
                cl.Text(content=source_doc.page_content, name=source_name)
            )
        source_names = [text_el.name for text_el in text_elements]

        if source_names:
            answer += f"\nSources: {', '.join(source_names)}"
        else:
            answer += "\nNo sources found"

    await cl.Message(content=answer, elements=text_elements).send()