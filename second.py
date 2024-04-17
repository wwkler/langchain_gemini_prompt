
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
    os.environ["GOOGLE_API_KEY"] = ""




# Fat Secret API 주소 (영문 검색)
fatsecret_url = "https://www.fatsecret.com/search?q=Starbucks"


chat = ChatGoogleGenerativeAI(model='gemini-pro')



prompt = ChatPromptTemplate.from_messages(
    [
        ('system','andswer by fatsecret_url'),
        MessagesPlaceholder(variable_name='message')
    ]
)

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

# 오늘 먹은 음료의 칼로리
kcal_response = chat.invoke(input=f"오늘 먹은 음료의 칼로리를 알려줘")
kcal = kcal_response.content

# 오늘 먹은 음료의 설탕 함량
sugar_response = chat.invoke(input=f"오늘 먹은 음료의 설탕 함량을 알려줘")
sugar = sugar_response.content

# 스타벅스에서 가장 칼로리가 낮은 음료
low_kcal_response = chat.invoke(input=f"스타벅스에서 가장 칼로리가 낮은 음료를 알려줘")
low_kcal_drink = low_kcal_response.content

# 스타벅스에서 가장 설탕 함량이 낮은 음료
low_sugar_response = chat.invoke(input=f"스타벅스에서 가장 설탕 함량이 낮은 음료를 알려줘")
low_sugar_drink = low_sugar_response.content

print(f"오늘 먹은 음료의 칼로리: {kcal}")
print(f"오늘 먹은 음료의 설탕 함량: {sugar}")
print(f"스타벅스에서 가장 칼로리가 낮은 음료: {low_kcal_drink}")
print(f"스타벅스에서 가장 설탕 함량이 낮은 음료{low_sugar_drink}")



response = []

#검색
input_prompt = input("User : ")


#저장
from langchain.memory import ChatMessageHistory
demo_ephemeral_chat_history = ChatMessageHistory()
demo_ephemeral_chat_history.add_user_message()
demo_ephemeral_chat_history.add_ai_message()
demo_ephemeral_chat_history.messages

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