# p.150
# function calling 를 사용한다면 GPT에게 함수와 그에 관한 설명을 제공하고 상황에 맞는 특정 함수를 호출하도록 할 수 있다.
from datetime import datetime

# 현재 시간 파악 함수
def get_current_time():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(now)
    return now 

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "현재 날짜와 시간을 반환합니다.",
        }
    },
]

if __name__ == '__main__':
    get_current_time()  