from langchain_core.messages import HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain


class Gemini:
    def __init__(self, text, prompt, retriever, chat_history):
        self.text = text   # main.py에서 입력 받은 텍스트
        self.prompt = prompt # 시스템 프롬프트 설정에 접근할 수 있는 변수
        self.retriever = retriever # vector DB로부터 얻는 가장 근접한 대답을 받는 설정
        self.chat_history = chat_history # main.py에 class Storage에 있는 chat_history 변수

    def call_gemini(self):
        #  1. Gemini 모델을 만든다.
        model = ChatGoogleGenerativeAI(model='gemini-1.5-pro-latest', temperature=1.0)

        # 2. 시스템 프롬프트 설정을 Gemini 모델에 반영한다.
        combine_docs_chain = create_stuff_documents_chain(model, self.prompt)
        retrieval_chain = create_retrieval_chain(self.retriever, combine_docs_chain)
            
        # 3. Gemini 모델에게 대답을 얻는다.
        response = retrieval_chain.invoke({"input": self.text, 
                                           "chat_history" : self.chat_history})
        
        print(response['chat_history'])
        
        # 4. Gemini한테 얻은 최종 대답을 활용해서 채팅 이력을 main.py에 있는 Storage 클래스의 chat_history 변수에 확장한다.
        self.chat_history.extend([HumanMessage(content=self.text),
                                  AIMessage(content=response['answer'])])

        # 5. Gemini한테 얻은 최종 대답을 main.py로 보낸다.
        return response['answer']


    
    
# chat_history = []
# question = "What is Task Decomposition?"
# ai_msg_1 = rag_chain.invoke({"input": question, 
#                              "chat_history": chat_history})
# chat_history.extend([HumanMessage(content=question), ai_msg_1["answer"]])
# second_question = "What are common ways of doing it?"
# ai_msg_2 = rag_chain.invoke({"input": second_question, "chat_history": chat_history})
# print(ai_msg_2["answer"])