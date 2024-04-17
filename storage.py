# 사전에 채팅 히스토리를 기록
# 여러 데이터를 수집해서 embedding(벡터화) 하고 Vector DB에 저장한다.
def storage():
    chat_history = [] # 채팅 히스토리, 프롬프트 시스템 설정할 떄 사용할 수 있다.
    
    # get_url 함수 : URL에 있는 30개를 모으는 txt 파일을 읽어서 모은 Url들을 반환 하는 함수 
    
    # save_vecotor_db 함수 : URl들에 있는 웹 페이지 글들을 읽어서 embedding(벡터화) 하고 Vector DB에 저장하는 함수 

if __name__ == '__main__':
    storage()