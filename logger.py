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
        