import os
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader


class Save_Vector_DB:
    def __init__(self):
        pass
        
    # PDF 파일을 바탕으로 텍스트를 읽고 그것을 embedding해서 VectorDB에 저장하는 매서드
    def save_db(self):
        if "GOOGLE_API_KEY" not in os.environ:
            os.environ["GOOGLE_API_KEY"] = "AIzaSyA0TiBpYfLhr8GY6zSZAtEKdkiw31wE4HU"

        # PDF 파일 세팅
        loader = PyPDFLoader("youye.pdf")  # PDF를 불러온다. loader 변수로 저장
        
        # 스플리터로 자른다.
        pages = loader.load() 
        
        # embedding(벡터화) 해서 Vector DB를 생성하고 return 한다.
        vectordb = Chroma.from_documents(documents=pages,
                                         embedding=GoogleGenerativeAIEmbeddings(model="models/embedding-001"))
        
        return vectordb

