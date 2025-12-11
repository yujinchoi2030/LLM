# p.151
# get_current_time 함수를 이용해 시간 알아내기
from gpt_functions.gpt_functions_0 import get_current_time, tools 
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) 

def get_ai_response(messages, tools=None):
    response = client.chat.completions.create(
        model="gpt-4o",   
        messages=messages,
        tools=tools,  # 사용 가능한 도구 목록 전달
    )
    return response 

messages = [
    {"role": "system", "content": "너는 사용자를 도와주는 상담사야."},  # 초기 시스템 메시지
]

while True:
    user_input = input("사용자 : ")  # 사용자 : 입력 받기

    if user_input == "exit":
        break
    
    messages.append({"role": "user", "content": user_input})  # 사용자 메시지 대화 기록에 추가
    
    ai_response = get_ai_response(messages, tools=tools)
    ai_message = ai_response.choices[0].message
    print(ai_message)  # gpt에서 반환되는 값을 파악하기 위해 임시로 추가

    tool_calls = ai_message.tool_calls  # AI 응답에 포함된 tool_calls를 가져옴
    if tool_calls:  # tool_calls가 있는 경우
        tool_name = tool_calls[0].function.name # 실행해야한다고 판단한 함수명 받기
        tool_call_id = tool_calls[0].id         # tool_call 아이디 받기    
        
        if tool_name == "get_current_time":  # 만약 tool_name이 "get_current_time"이라면
            messages.append({
                "role": "function",  # role을 "function"으로 설정
                "tool_call_id": tool_call_id,
                "name": tool_name,
                "content": get_current_time(),  # get_current_time 함수를 실행한 결과를 content로 설정
            })

        ai_response = get_ai_response(messages, tools=tools) # 다시 GPT 응답 받기
        ai_message = ai_response.choices[0].message

    messages.append(ai_message)  # AI 응답을 대화 기록에 추가하기

    print("AI\t: " + ai_message.content)  # AI 응답 출력
