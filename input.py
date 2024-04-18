# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# class SystemPromptSetting:
#     def __init__(self, text):
#         self.text = text
        
#     def promptSetting(self):
#         chat_prompt = ChatPromptTemplate.from_messages([
#                     ('system', '잘 대답해줘'),
#                     ('user', "{user_input}"),
#                 ])
        
#         messages = chat_prompt.format_messages(user_input=self.text)
         
#         return messages


# class DrinkRecommendationSystem:
#     def __init__(self, api_key):
#         self.chatbot = ChatGoogleGenerativeAI(model='gemini-1.5-pro-latest', api_key=api_key)

#     def generate_response(self, user_input):
#         # 사용자 입력을 이해하여 LLM으로 답변 생성
#         response = self.chatbot.invoke(input=user_input, system_prompt="음료 추천 시스템")
#         return response.content

#     def process_user_input(self):
#         # 사용자 입력 받기
#         user_input = input("사용자: ")
        
#         # 사용자 입력을 전처리하고 답변 생성
#         response = self.generate_response(user_input)

#         # Gemini API를 통해 답변이 제대로 생성되었는지 확인
#         if response.confidence > 0.5:
#             print("Gemini API를 통해 답변이 제대로 생성되었습니다.")
#         else:
#             print("Gemini API를 통해 답변이 생성되지 않았거나, 낮은 확신도를 갖고 있습니다.")
        
#         return response

# # API 키 설정
# api_key = "YOUR_GEMINI_API_KEY"

# DrinkRecommendationSystem 클래스의 인스턴스 생성
# recommendation_system = DrinkRecommendationSystem(api_key)

# # 사용자 입력에 대한 응답 생성
# response = recommendation_system.process_user_input()

# # 생성된 응답 출력
# print("음료 추천 시스템: ", response)



# 3
# 
# from langchain_google_genai import ChatGoogleGenerativeAI

# class DrinkRecommendationSystem:
#     def __init__(self, api_key):
#         self.chatbot = ChatGoogleGenerativeAI(model='gemini-1.5-pro-latest', api_key=api_key)

#     def generate_response(self, user_input):
#         # 사용자 입력을 이해하여 LLM으로 답변 생성
#         response = self.chatbot.invoke(input=user_input)
#         return response.content

#     def process_user_input(self):
#         # 사용자 입력 받기
#         user_input = input("사용자: ")
        
#         # 사용자 입력을 전처리하고 답변 생성
#         response = self.generate_response(user_input)
#         return response

# # API 키 설정
# api_key = "YOUR_GEMINI_API_KEY"

# # DrinkRecommendationSystem 클래스의 인스턴스 생성
# recommendation_system = DrinkRecommendationSystem(api_key)

# # 사용자 입력에 대한 응답 생성
# response = recommendation_system.process_user_input()

# # 생성된 응답 출력
# print("음료 추천 시스템: ", response)

#1. class 함수로 음료추천시스템 input

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

class DrinkRecommendationSystem:
    def __init__(self):
        self.chatbot = ChatGoogleGenerativeAI(model='gemini-1.5-pro-latest')

    def generate_response(self, user_input):
        # 사용자 입력을 이해하여 LLM으로 답변 생성
        response = self.chatbot.invoke(input=user_input)
        return response.content

    def process_user_input(self, user_input):
        # 사용자 입력을 전처리하고 답변 생성
        response = self.generate_response(user_input)
        return response

# DrinkRecommendationSystem 클래스의 인스턴스 생성
recommendation_system = DrinkRecommendationSystem()


# 사용자 입력 받기
user_input = input("사용자: ")

# 사용자 입력에 대한 응답 생성
response = recommendation_system.process_user_input(user_input)

# 생성된 응답 출력
print("음료 추천 시스템: ", response)


#2.class함수로 정해진 값 출력해보기
# 
# import os
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.messages import HumanMessage, SystemMessage
# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# class StarbucksDrinkAnalyzer:
#     def __init__(self, api_key):
#         if os.getenv("GOOGLE_API_KEY") is None:
#             os.environ["GOOGLE_API_KEY"] = api_key
#         self.fatsecret_url = "https://www.fatsecret.kr/%EC%B9%BC%EB%A1%9C%EB%A6%AC-%EC%98%81%EC%96%91%EC%86%8C/search?q=%EC%8A%A4%ED%83%80%EB%B2%85%EC%8A%A4+(Starbucks)+%EC%BB%A4%ED%94%BC"
#         self.chat = ChatGoogleGenerativeAI(model='gemini-pro')

#     def get_today_drink_info(self):
#         kcal_response = self.chat.invoke(input=f"오늘 먹은 음료의 칼로리를 알려줘")
#         kcal = kcal_response.content

#         sugar_response = self.chat.invoke(input=f"오늘 먹은 음료의 설탕 함량을 알려줘")
#         sugar = sugar_response.content

#         return f"오늘 먹은 음료의 칼로리: {kcal}, 설탕 함량: {sugar}"

#     def get_lowest_calorie_drink(self):
#         low_kcal_response = self.chat.invoke(input=f"스타벅스에서 가장 칼로리가 낮은 음료를 알려줘")
#         return low_kcal_response.content

#     def get_lowest_sugar_drink(self):
#         low_sugar_response = self.chat.invoke(input=f"스타벅스에서 가장 설탕 함량이 낮은 음료를 알려줘")
#         return low_sugar_response.content

#     def compare_drinks(self):
#         low_kcal_drink = self.get_lowest_calorie_drink()
#         low_sugar_drink = self.get_lowest_sugar_drink()
#         print(f"스타벅스에서 가장 칼로리가 낮은 음료: {low_kcal_drink}")
#         print(f"스타벅스에서 가장 설탕 함량이 낮은 음료: {low_sugar_drink}")

#         prompt = ChatPromptTemplate.from_messages(
#             [
#                 ('system', 'andswer by fatsecret_url'),
#                 MessagesPlaceholder(variable_name='message')
#             ]
#         )

#         chain = prompt | self.chat
#         response = chain.invoke({'message': [HumanMessage('user saying:')]})

# # StarbucksDrinkAnalyzer 클래스의 인스턴스 생성
# analyzer = StarbucksDrinkAnalyzer(api_key='AIzaSyAq2lz53uw_YhBfJJ6P4DGnmXLMZyJCD2U')

# # 오늘 먹은 음료 정보 출력
# print(analyzer.get_today_drink_info())

# # 스타벅스에서 가장 칼로리가 낮은 음료와 설탕 함량이 낮은 음료 비교
# analyzer.compare_drinks()





# # Fat Secret API 주소 (한국어 검색 불가능)
# fatsecret_url = "https://www.fatsecret.kr/%EC%B9%BC%EB%A1%9C%EB%A6%AC-%EC%98%81%EC%96%91%EC%86%8C/search?q=%EC%8A%A4%ED%83%80%EB%B2%85%EC%8A%A4+(Starbucks)+%EC%BB%A4%ED%94%BC"

# # Fat Secret API 주소 (영문 검색)
# fatsecret_url = "https://www.fatsecret.com/search?q=Starbucks"

# import os
# from langchain_community.document_loaders import WebBaseLoader
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
# from langchain_core.messages import HumanMessage, SystemMessage
# from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
# from langchain_text_splitters import RecursiveCharacterTextSplitter

# if os.getenv("GOOGLE_API_KEY") is None:
#     os.environ["GOOGLE_API_KEY"] = "YOUR_GEMINI_API_KEY"

# # Fat Secret API 주소 (영문 검색)
# fatsecret_url = "https://www.fatsecret.com/search?q=Starbucks"

# chat = ChatGoogleGenerativeAI(model='gemini-pro')

# # 오늘 먹은 음료의 칼로리
# kcal_response = chat.invoke(input=f"오늘 먹은 음료의 칼로리를 알려줘")
# kcal = kcal_response.content

# # 오늘 먹은 음료의 설탕 함량
# sugar_response = chat.invoke(input=f"오늘 먹은 음료의 설탕 함량을 알려줘")
# sugar = sugar_response.content

# # 스타벅스에서 가장 칼로리가 낮은 음료
# low_kcal_response = chat.invoke(input=f"스타벅스에서 가장 칼로리가 낮은 음료를 알려줘")
# low_kcal_drink = low_kcal_response.content

# # 스타벅스에서 가장 설탕 함량이 낮은 음료
# low_sugar_response = chat.invoke(input=f"스타벅스에서 가장 설탕 함량이 낮은 음료를 알려줘")
# low_sugar_drink = low_sugar_response.content

# print(f"오늘 먹은 음료의 칼로리: {kcal}")
# print(f"오늘 먹은 음료의 설탕 함량: {sugar}")
# print(f"스타벅스에서 가장 칼로리가 낮은 음료: {low_kcal_drink}")
# print(f"스타벅스에서 가장 설탕 함량이 낮은 음료{low_sugar_drink}")


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


