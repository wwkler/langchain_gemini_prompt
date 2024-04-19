from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.vectorstores import Chroma
import os

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = "AIzaSyA0TiBpYfLhr8GY6zSZAtEKdkiw31wE4HU"  # API키 값을 value로 저장

text = input("질문 : ")

params = {  # 환경 설정, 다양한 파라미터중에 필요한 것을 선택.
    "temperature": 0.7,   # 해당 온도를 가지고 추론해준다.
    "max_output_tokens": 100,  # 토큰의 최대개수 설정, 0보다 커야하고 설정되지 않았으면 64로 디폴트.
}

llm = ChatGoogleGenerativeAI(model="gemini-pro", **params)  # model을 제미니 프로로 설정하고, 설정한 파라미터들을 넣는다.

#Load the models
llm = ChatGoogleGenerativeAI(model="gemini-pro")

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")  # 모델을 사용하여 임베딩
#Load the PDF and create chunks

loader = PyPDFLoader("youye.pdf")  # PDF를 불러온다. loader 변수로 저장
text_splitter = CharacterTextSplitter(  # 텍스트를 자를 도구를 설정
    separator=" ",
    chunk_size=30,
    chunk_overlap=0,
    length_function=len,
    is_separator_regex=False,
)
pages = loader.load_and_split(text_splitter)  # PDF를 불러오고 스플리터로 자른다.
#Turn the chunks into embeddings and store them in Chroma
vectordb=Chroma.from_documents(pages,embeddings)  # chromadb 파이썬 패키지가 설치되어있어야 한다.
#Configure Chroma as a retriever with top_k=5
retriever = vectordb.as_retriever(search_kwargs={"k": 5})
#Create the retrieval chain
template = """
You are a helpful AI assistant.
Answer based on the context provided.
context: {context}
input: {input}
answer:
"""
prompt = PromptTemplate.from_template(template)  # 저희 팀이 문제있는 부분
combine_docs_chain = create_stuff_documents_chain(llm, prompt)
retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)


#Invoke the retrieval chain
response=retrieval_chain.invoke({"input": text})

#Print the answer to the question
print('대답 : ')
print(response["answer"])