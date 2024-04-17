#1. class 함수로 음료추천시스템 input

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

class DrinkRecommendationSystem:
    def __init__(self):
        self.chatbot = ChatGoogleGenerativeAI(model='gemini-pro')

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
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

class StarbucksDrinkAnalyzer:
    def __init__(self, api_key):
        if os.getenv("GOOGLE_API_KEY") is None:
            os.environ["GOOGLE_API_KEY"] = api_key
        self.fatsecret_url = "https://www.fatsecret.kr/%EC%B9%BC%EB%A1%9C%EB%A6%AC-%EC%98%81%EC%96%91%EC%86%8C/search?q=%EC%8A%A4%ED%83%80%EB%B2%85%EC%8A%A4+(Starbucks)+%EC%BB%A4%ED%94%BC"
        self.chat = ChatGoogleGenerativeAI(model='gemini-pro')

    def get_today_drink_info(self):
        kcal_response = self.chat.invoke(input=f"오늘 먹은 음료의 칼로리를 알려줘")
        kcal = kcal_response.content

        sugar_response = self.chat.invoke(input=f"오늘 먹은 음료의 설탕 함량을 알려줘")
        sugar = sugar_response.content

        return f"오늘 먹은 음료의 칼로리: {kcal}, 설탕 함량: {sugar}"

    def get_lowest_calorie_drink(self):
        low_kcal_response = self.chat.invoke(input=f"스타벅스에서 가장 칼로리가 낮은 음료를 알려줘")
        return low_kcal_response.content

    def get_lowest_sugar_drink(self):
        low_sugar_response = self.chat.invoke(input=f"스타벅스에서 가장 설탕 함량이 낮은 음료를 알려줘")
        return low_sugar_response.content

    def compare_drinks(self):
        low_kcal_drink = self.get_lowest_calorie_drink()
        low_sugar_drink = self.get_lowest_sugar_drink()
        print(f"스타벅스에서 가장 칼로리가 낮은 음료: {low_kcal_drink}")
        print(f"스타벅스에서 가장 설탕 함량이 낮은 음료: {low_sugar_drink}")

        prompt = ChatPromptTemplate.from_messages(
            [
                ('system', 'andswer by fatsecret_url'),
                MessagesPlaceholder(variable_name='message')
            ]
        )

        chain = prompt | self.chat
        response = chain.invoke({'message': [HumanMessage('user saying:')]})

# StarbucksDrinkAnalyzer 클래스의 인스턴스 생성
analyzer = StarbucksDrinkAnalyzer(api_key='AIzaSyAq2lz53uw_YhBfJJ6P4DGnmXLMZyJCD2U')

# 오늘 먹은 음료 정보 출력
print(analyzer.get_today_drink_info())

# 스타벅스에서 가장 칼로리가 낮은 음료와 설탕 함량이 낮은 음료 비교
analyzer.compare_drinks()






