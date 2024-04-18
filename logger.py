import csv
import os
from datetime import datetime

class Logger:
    def save_data(self, data: list):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('./data_log.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            if os.stat('data_log.csv').st_size == 0:
                writer.writerow(['No.', 'Question', 'Answer', 'Timestamp'])
            for idx, line in enumerate(data, start=1):
                Answer = response.content   # gemini에서 받은 response를 Answer로 받음.
                text, Answer = line.split(', ') # main에서 user input을 text로 받음. 
                writer.writerow([idx, text, Answer, current_time])

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