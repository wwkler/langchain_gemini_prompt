import os
from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma



class SaveDB:
    def __init__(self, urls):
        self.loader = WebBaseLoader(web_paths=urls)
        self.text_spliter=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)

    def save_db(self):
        if "GOOGLE_API_KEY" not in os.environ:
            os.environ["GOOGLE_API_KEY"] = "AIzaSyAXHubEUXcfTJV3nPCt7N3n4jn0LwNV83k"

        # 데이터를 수집한다.
        text = self.loader.load()

    
        # 500글자씩 자르는데, 안겹치게 자름
        splits = self.text_spliter.split_documents(text)



        # embedding(벡터화) 해서 Vector DB를 생성하고 return 한다.
        vectordb = Chroma.from_documents(documents=splits,
                                        embedding=GoogleGenerativeAIEmbeddings(model="models/embedding-001"))
        
        return vectordb




savedb = SaveDB(urls=["https://docs.smith.langchain.com/overview", 
                      "https://docs.smith.langchain.com/overview"])
savedb.save_db()

        
        

    

