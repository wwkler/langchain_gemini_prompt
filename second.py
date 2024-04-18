
# Fat Secret API 주소 (한국어 검색 불가능)
fatsecret_url = "https://www.fatsecret.kr/%EC%B9%BC%EB%A1%9C%EB%A6%AC-%EC%98%81%EC%96%91%EC%86%8C/search?q=%EC%8A%A4%ED%83%80%EB%B2%85%EC%8A%A4+(Starbucks)+%EC%BB%A4%ED%94%BC"

# Fat Secret API 주소 (영문 검색)
fatsecret_url = "https://www.fatsecret.com/search?q=Starbucks"

import os
from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_text_splitters import RecursiveCharacterTextSplitter





if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = "AIzaSyDlmba06dnGqJTW4dw5C44Nba9MoUtY74w"




# Fat Secret API 주소 (영문 검색)
fatsecret_url = "https://www.fatsecret.com/search?q=Starbucks"


chain = prompt | chat
response = chain.invoke(
    {'message': [HumanMessage('user saying:')]}
)
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer all questions to the best of your ability.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)



#저장

from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

store = {}


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


with_message_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)



from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

store = {}

from langchain.memory import ChatMessageHistory
demo_ephemeral_chat_history = ChatMessageHistory()
demo_ephemeral_chat_history.add_user_message()
demo_ephemeral_chat_history.add_ai_message()
demo_ephemeral_chat_history.messages

demo_ephemeral_chat_history = ChatMessageHistory()


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


with_message_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)



# Remembers
with_message_history.invoke(
    {"coffee": "name", "input": "What?"},
    config={"configurable": {"session_id": "abc123"}},
)

 # New session_id --> does not remember.
with_message_history.invoke(
    {"coffee": "name", "input": "What?"},
    config={"configurable": {"session_id": "def234"}},
)



# from langchain.memory import ChatMessageHistory
# demo_ephemeral_chat_history = ChatMessageHistory()
# demo_ephemeral_chat_history.add_user_message("다이어트할 때 마시기 좋은 음료를 추천해줘")
# demo_ephemeral_chat_history.add_ai_message("저칼로리 음료는 다음과 같습니다. 물(0kal) 등이 있습니다.")
# demo_ephemeral_chat_history.messages


demo_ephemeral_chat_history = ChatMessageHistory()

while True:
    new_input = input("User: ")

    if new_input == "Bye!":
        break

    demo_ephemeral_chat_history.add_user_message(new_input)
    response = chain.invoke(
        {
            "messages": demo_ephemeral_chat_history.messages,
        }
    )


    #https://python.langchain.com/docs/expression_language/how_to/message_history/