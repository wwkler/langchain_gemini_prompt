import os
from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader,OnlinePDFLoader
from langchain_community.document_loaders import UnstructuredPDFLoader


class Save_Vector_DB:
    def __init__(self):
        pass
        
    # 30개의 url를 받아서 데이터를 수집하고 embedding해서 VectorDB에 저장하는 매서드
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

