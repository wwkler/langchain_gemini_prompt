# 
#1.

# Fat Secret API 주소 (한국어 검색 불가능)
fatsecret_url = "https://www.fatsecret.kr/%EC%B9%BC%EB%A1%9C%EB%A6%AC-%EC%98%81%EC%96%91%EC%86%8C/search?q=%EC%8A%A4%ED%83%80%EB%B2%85%EC%8A%A4+(Starbucks)+%EC%BB%A4%ED%94%BC"

# Fat Secret API 주소 (영문 검색)
fatsecret_url = "https://www.fatsecret.com/search?q=Starbucks"

import os
from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_text_splitters import RecursiveCharacterTextSplitter

if os.getenv("GOOGLE_API_KEY") is None:
    os.environ["GOOGLE_API_KEY"] = "YOUR_GEMINI_API_KEY"

# Fat Secret API 주소 (영문 검색)
fatsecret_url = "https://www.fatsecret.com/search?q=Starbucks"

chat = ChatGoogleGenerativeAI(model='gemini-pro')

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




# #2.
# import os
# from langchain_community.document_loaders import WabBaseLoader
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
# from langchain_core.messages import HumanMessage, SystemMessage
# from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate, MessagesPla
# from langchain_text_splitters import RecursiveCharacterTextSplitter

# os.environ["GEMINI_API_KEY"] = "YOUR_GEMINI_API_KEY"  # Gemini API 키 입력

# # Fat Secret API 주소 (영문 검색)
# fatsecret_url = "https://www.fatsecret.com/search?q=Starbucks"

# # WabBaseLoader를 사용하여 Fat Secret URL 로드
# fatsecret_document = WabBaseLoader.load_document(fatsecret_url)

# # Fat Secret 문서에서 원하는 영양 정보 필드 추출 (예: 칼로리, 설탕)
# kcal = fatsecret_document.get("kcal")
# sugar = fatsecret_document.get("sugar")

# chat = ChatGoogleGenerativeAI(model='offline4')

# # 오늘 먹은 음료의 칼로리
# kcal_response = chat.invoke(input=f"오늘 먹은 음료의 칼로리가 {kcal}kcal인 음료는 무엇인가요?")
# kcal_drink = kcal_response.content

# # 오늘 먹은 음료의 설탕 함량
# sugar_response = chat.invoke(input=f"오늘 먹은 음료의 설탕 함량이 {sugar}g인 음료는 무엇인가요?")
# sugar_drink = sugar_response.content

# # 스타벅스에서 가장 칼로리가 낮은 음료
# low_kcal_response = chat.invoke(input=f"스타벅스 음료 중에서 칼로리가 가장 낮은 음료는 무엇인가요?")
# low_kcal_drink = low_kcal_response.content

# # 스타벅스에서 가장 설탕 함량이 낮은 음료
# low_sugar_response = chat.invoke(input=f"스타벅스 음료 중에서 설탕 함량이 가장 낮은 음료는 무엇인가요?")
# low_sugar_drink = low_sugar_response.content

# print(f"오늘 먹은 음료: {kcal_drink}")
# print(f"스타벅스에서 가장 칼로리가 낮은 음료: {low_kcal_drink}")
# print(f"스타벅스에서 가장 설탕 함량이 낮은 음료: {low_sugar_drink}")



# prompt = ChatPromptTemplate.from_messages(
#     [
#         ('system','andswer by fatsecret_url'),
#         MessagesPlaceholder(variable_name='message')
#     ]
# )

# chain = prompt | chat
# response = chain.invoke(
#     {'message': [HumanMessage('user saying:')]}
# )





# #3
# import os
# from langchain_community.document_loaders import WabBaseLoader
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
# from langchain_core.messages import HumanMessage, SystemMessage
# from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate, MessagesPla
# from langchain_text_splitters import RecursiveCharacterTextSplitter

# os.environ["GEMINI_API_KEY"] = "YOUR_GEMINI_API_KEY"  # Gemini API key

# # Fat Secret API URL (English search)
# fatsecret_url = "https://www.fatsecret.com/search?q=Starbucks"

# chat = ChatGoogleGenerativeAI(model='offline4')

# # Today's drink calorie
# kcal_response = chat.invoke(input=f"오늘 먹은 음료의 칼로리를 알려줘")
# kcal = kcal_response.content

# # Today's drink sugar content
# sugar_response = chat.invoke(input=f"오늘 먹은 음료의 설탕 함량을 알려줘")
# sugar = sugar_response.content

# # Print today's drink information
# print(f"오늘 먹은 음료: 칼로리 {kcal}kcal, 설탕 함량 {sugar}g")

# # Compare calorie/sugar content and search based on user's questions

# def answer_by_url(url, question, high_or_low):
#     # Load document information from Fat Secret API
#     document = WabBaseLoader.load_document(url)

#     # Extract calorie/sugar content
#     kcal = document.get("kcal")
#     sugar = document.get("sugar")

#     # Set response conditions based on question
#     if question.lower() == "칼로리":
#         if high_or_low == "높은":
#             condition = kcal >= max_kcal
#         else:
#             condition = kcal <= min_kcal

#     elif question.lower() == "설탕 함량":
#         if high_or_low == "높은":
#             condition = sugar >= max_sugar
#         else:
#             condition = sugar <= min_sugar

 
#     if condition:
#         return f"{document.get('name')}은 {high_or_low} {question} 음료입니다. {question}: {kcal if question.lower() == '칼로리' else sugar}g"
#     else:
#         return f"아직 {high_or_low} {question} 음료를 찾지 못했습니다."

# # Starbucks drink with highest calorie
# max_kcal_response = chat.invoke(input=f"스타벅스에서 가장 칼로리가 높은 음료를 알려줘")
# max_kcal = max_kcal_response.content

# # Starbucks drink with highest sugar content
# max_sugar_response = chat.invoke(input=f"스타벅스에서 가장 설탕 함량이 높은 음료를 알려줘")
# max_sugar = max_sugar_response.content

# # Starbucks drink with lowest calorie
# min_kcal_response = chat.invoke(input=f"스타벅스에서 가장 칼로리가 낮은 음료를 알려줘")
# min_kcal = min_kcal_response.content

# # Starbucks drink with lowest sugar content
# min_sugar_response = chat.invoke(input=f"스타벅스에서 가장 설탕 함량이 낮은 음료를 알려줘")
# min_sugar = min_sugar_response.content

# # Print calorie/sugar content comparison and search results
# print(f"스타벅스에서 가장 칼로리가 높은 음료: {answer_by_url(fatsecret_url, '칼로리', '높은')}")
# print(f"스타벅스에서 가장 설탕 함량이 높은 음료: {answer_by_url(fatsecret_url, '설탕 함량', '높은')}")
# print(f"스타벅스에서 가장 칼로리가 낮은 음료: {answer_by_url(fatsecret_url, '칼로리', '낮은')}")
# print(f"스타벅스에서 가장 설탕 함량이 낮은 음료: {answer_by_url(fatsecret_url, '설탕 함량', '낮은')}")


# prompt = ChatPromptTemplate.from_messages(
#     [
#         ('system','andswer by fatsecret_url'),
#         MessagesPlaceholder(variable_name='message')
#     ]
# )

# chain = prompt | chat
# response = chain.invoke(
#     {'message': [HumanMessage('user saying:')]}
# )



