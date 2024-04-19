from get_urls import Url_Loader
from retriever import Save_Vector_DB
from input import SystemPromptSetting
from gemini import Gemini
from logger import Logger

# chat_history와 vector db의 상태를 유지하기 위한 클래스 
class Storage:
    def __init__(self):
        self.chat_history = [] # 현지님이 LLM(Gemini)를 호출할 떄 추가적으로 넣어주는 chat history 입니다.

        self.vector_db = Save_Vector_DB().save_db()  # PDF 에서 텍스트를 추출해서 embedding하고 vector db에 저장하는 기능을 호출한다.
        
# 사전 세팅 -> chat_history를 만들고 vector db를 세팅한다.
st = Storage() 

# 사용자가 입력해서 chat Bot을 사용한다.
print("=========챗봇을 시작합니다!!!=========")
while True:
    # Question Input을 받아서 상황에 따라 while문을 종료한다. (if문 사용)
    text = input('질문 : ')
    
    if text in ['q', 'quit']: #  text가 q, quit이면 프로그램을 종료한다.
        print("=========챗봇을 종료합니다!!!=========")
        break

    # chat - Question Input과 LLM Answer를 어떻게 시스템 설정을 한다.
    spt = SystemPromptSetting(text)
    prompt = spt.promptSetting()

    # User Input을 바탕으로 Vector DB에서 가장 근접한 대답을 어떻게 찾을지 설정한다.
    retriever = st.vector_db.as_retriever(search_kwargs={"k": 1})
    
    # gemini - User Input과 가장 근접한 대답을 을 바탕으로 Gemini한테 call 한다.
    gemini = Gemini(text, prompt, retriever, st.chat_history)
    answer = gemini.call_gemini()
    
    # Gemini 한테 최종 대답을 받아서 print 한다.
    print(f'Gemini 대답 : {answer}')

    # # logger  - User Input과 gemini에서 반환한 최종 답변을 바탕으로 로그를 찍는다.
    logger = Logger()
    logger.save_data(text, answer)

    # 한줄 띄워준다.
    print()