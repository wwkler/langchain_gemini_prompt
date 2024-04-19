import csv
import os
from datetime import datetime, timezone, timedelta

class Logger:
    # 현재 시간을 구하는 함수  2023-04-1623:59
    def get_day_time(self):
        KST = timezone(timedelta(hours=9))
        time_record = datetime.now(KST)
        day = str(time_record)[:10]
        time = str(time_record.time())[:5]
        return (day, time)
    
    # 질문, 대답, 로그 찍힌 시간을 텍스트 파일로 확장하는 함수 
    def save_data(self, text, answer): 
        day, time = self.get_day_time() # 현재 시각을 구한다.
        
        with open(file='./logger.txt', mode='a') as file: # 질문, 대답, 시각을 구해서 한줄에 추가한다.
            file.write(f"질문 : {text}\n")
            file.write("=" * 50 + "\n")

            file.write(f"대답 : {answer}")
            file.write("=" * 50 + "\n")

            file.write(f"시각 : {day}\t{time}\n")
            file.write("=" * 50 + "\n")

            file.write("\n")
        
# class Logger:
#     def save_data(self, data: list):
#         current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         with open('./data_log.csv', 'a', newline='') as f:
#             writer = csv.writer(f)
#             if os.stat('data_log.csv').st_size == 0:
#                 writer.writerow(['No.', 'Question', 'Answer', 'Timestamp'])
#             for idx, line in enumerate(data, start=1):
#                 Answer = response.content   # gemini에서 받은 response를 Answer로 받음.
#                 text, Answer = line.split(', ') # main에서 user input을 text로 받음. 
#                 writer.writerow([idx, text, Answer, current_time])

# # Logger 클래스 인스턴스 생성
# logger = Logger()

# # 예시 데이터 수정
# example_data = [
#     "What is the capital of France?, Paris",
#     "Who wrote 'Romeo and Juliet'?, William Shakespeare",
#     "What is the chemical symbol for water?, H2O",
#     "How many continents are there on Earth?, 7",
#     "What is the freezing point of water in Celsius?, 0"
# ]

# # 데이터 저장
# logger.save_data(example_data)