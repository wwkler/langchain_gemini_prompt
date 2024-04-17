# chat_history와 vector db의 상태를 유지하기 위한 클래스 
class Storage:
    def __init__(self):
        self.chat_history = []
        
        # self.urls = 30개 URL를 읽어서 (URL1, URL2, .... URL30) 이렇게 튜플로 변환해주는 기능을 호출한다.

        # self.vectordb = 웹 페이지에서 텍스트를 추출해서 embedding하고 vector db에 저장하는 기능을 호출한다.
   
# 사전 세팅 -> chat_history를 만들고 vector db를 세팅한다.
st = Storage() 

# 사용자가 입력해서 chat Bot을 사용한다.
while True:
    pass

    # chat - User Input과 LLM Answer를 어떻게 시스템 설정을 하는가에 대한 부분 (기능 맡으신 분이 구현 해야 합니다!)
    
    # User Input을 판별하여 상황에 따라 while문을 종료한다. (if문 사용)
    
    # User Input을 바탕으로 Vector DB에서 가장 근접한 대답을 찾는 코드
    
    # gemini - User Input과 가장 근접한 대답을 을 바탕으로 Gemini한테 call 하는 부분  (기능 맡으신 분이 구현 해야 합니다!)
    
    # 최종 대답을 print 한다.
    
    # logger  - User Input과 gemini에서 반환한 최종 답변을 바탕으로 로그를 찍는 부분 (기능 맡으신 분이 구현 해야 합니다!)
    
    # chat_history에 채팅 이력을 추가한다.