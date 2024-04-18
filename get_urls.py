# 30개의 URL를 찾아서 반환해주는 클래스 
class Url_Loader:
    def __init__(self):
        pass

    def read_text_files(self):  # 30개의 url 주소를 읽어서 리스트로 저장하는 함수 
        urls = []
        
        # urls.txt 파일을 읽는다.
        with open(file='./urls.txt', mode='r') as file: 
            for url in (file.readlines()):
                urls.append(url.rstrip("\n"))
        
        return urls

    def get_urls(self): # 30개 url 주소를 읽고 튜플로 반환하는 함수 
        urls = self.read_text_files()  
        
        return tuple(urls)