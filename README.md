# langchain_gemini_prompt
langchain_gemini_prompt 프로젝트 입니다.

## 팀원 소개(오프라인 4조)
    - 최승현(Logger), 주현범(Retriever), 민유진(SystemSetting), 조현지(Gemini), 김영우(main)

## 프로젝트 전반적인 내용

    위 프로젝트는 Langchain을 이용해서 Vector DB을 바탕으로 LLM을 불러와서 QA Engine이 진행되는 프로젝트 이다.
    사용자가 질문을 계속 하면서 과거 이력을 반영하여 대답이 나오도록 구현했다.

    주제 :  문학 작품의 다양한 시각을 넓혀 주는 나만의 독후감 대리 QA BOT

    프로그램은 2단계 과정을 거친다.

    1. 사전 세팅
        PyPDFLoader를 이용하여 pdf 파일을 읽고 페이지 별로 텍스트를 split하고 임베딩 한 후 Vector DB에 저장
    
    2. 사용자가 QA BOT 사용
        사용자가 질문을 하면 Vector DB를 참고하여 대답을 출력받는다.

    프로그램이 진행되기 위한 모듈은 다음과 같다.

    1. main : 프로그램의 출발점이며, 사전 세팅에 대한 모듈과 QA BOT 출력을 도출하기 위한 모듈로 구성된다.
    2. retreiver : save_Vector_DB class 를 만들어서 raw데이터를 불러오고 의미 단위로 스플릿을 하였습니다.
                   로드는PDF 로더를 사용했습니다.
                   스플릿한 데이터를 GoogleGenerativeAIEmbeddings 을 사용하여 vectorDB를 리턴합니다.
    5. systemSetting(input) :  시스템 프롬프트를 설정해 언어 모델(LLM)이 의도한 맥락에 맞는 응답을 생성하는 것입니다.
                                시스템 프롬프트는 일관된 맥락과 관련된 응답을 생성하기 위해 언어 모델을 가이드하는 역할
                                input을 text로 받아 gemini에 전달해줄 return값 message를 output으로 출력합니다.
    6. gemini :  gemini 모델을 만들어 호출한다. 
                 system prompt 설정과 retriever 설정을 gemini 모델에 반영한다.
                 gemini모델에게 질문한 input값인 HumanMessage와 답변인 AIMessage을 invoke한다.
                 gemini가 참고할 수 있게 HumanMessage, AIMessage를 chat_history에 넣어 저장한다.
                 gemini에게 얻은 최종 응답을 return 하도록 하여 main.py로 보낸다.
                 
    7. Logger : user input 질문과 gemini의 최종답변을 받아 input의 입력 현재시간과 같이 출력하여 logger.txt파일로      
                저장되도록 구현했습니다.


## 프로그램 사용 방법 
사용자가 PDF 파일을 선택해서 설정한 다음, 질문을 하면 사용자 의도에 맞게 분석하여 답변을 받아볼 수 있는 서비스

이전 질문과 이어지는 답변으로 사용자가 추가 질문을 한다. 

감사합니다.
