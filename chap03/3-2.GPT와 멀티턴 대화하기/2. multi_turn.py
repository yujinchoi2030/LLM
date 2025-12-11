# GPT가 사용자와 대화한 내용을 기억해서 맥락에 맞게 적절히 대답하도록
# 턴 = 대화
# 멀티턴 = 여러 번 턴 할 때 이전 대화를 기억하고 적절하게 반응하는 것
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) 

# 답변을 받아오는 부분을 함수로 구성
def get_ai_response(messages):
    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.9,
        messages=messages,  # 대화 기록을 입력으로 전달
    )
    return response.choices[0].message.content  # 생성된 응답의 내용 반환

# 초기 시스템 메시지
messages = [
    {"role": "system", "content": "너는 사용자를 도와주는 상담사야."},
]

while True:
    user_input = input("사용자: ")

    if user_input == "exit":
        break
    
    messages.append({"role": "user", "content": user_input})  # 사용자 메시지를 대화 기록에 추가 
    ai_response = get_ai_response(messages)  # 대화 기록을 기반으로 AI 응답 가져오기
    messages.append({"role": "assistant", "content": ai_response})  # AI 응답 대화 기록에 추가하기

    print("AI: " + ai_response)  # AI 응답 출력
