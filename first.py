import os
from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = "AIzaSyAx9lO9hy47eonRelKdNheDLvgrYjsP7AY"

chat = [GOOGLE_API_KEY]

loader = WebBaseLoader("https://www.fatsecret.kr/%EC%B9%BC%EB%A1%9C%EB%A6%AC-%EC%98%81%EC%96%91%EC%86%8C/search?q=%EC%8A%A4%ED%83%80%EB%B2%85%EC%8A%A4+(Starbucks)+%EC%BB%A4%ED%94%BC")

from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer all questions to the best of your ability.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)
chain = prompt | chat
chain.invoke(
    {
        "messages": [
            HumanMessage(
                content="Translate this sentence from English to French: I love programming."
            ),
            AIMessage(content="J'adore la programmation."),
            HumanMessage(content="What did you just say?"),
        ],
    }
)

#저장
from langchain.memory import ChatMessageHistory
demo_ephemeral_chat_history = ChatMessageHistory()
demo_ephemeral_chat_history.add_user_message(
    "Translate this sentence from English to French: I love programming."
)
demo_ephemeral_chat_history.add_ai_message("J'adore la programmation.")
demo_ephemeral_chat_history.messages



demo_ephemeral_chat_history = ChatMessageHistory()
input1 = "Translate this sentence from English to French: I love programming."
demo_ephemeral_chat_history.add_user_message(input1)
response = chain.invoke(
    {
        "messages": demo_ephemeral_chat_history.messages,
    }
)
demo_ephemeral_chat_history.add_ai_message(response)
input2 = "What did I just ask you?"
demo_ephemeral_chat_history.add_user_message(input2)
chain.invoke(
    {
        "messages": demo_ephemeral_chat_history.messages,
    }
)