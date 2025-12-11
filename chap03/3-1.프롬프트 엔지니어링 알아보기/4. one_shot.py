# 원샷 프롬프팅 = GPT가 원하는 패턴에 맞춰 답변하도록 예시를 "한 번" 제시해서 유도하는 방식
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
  model="gpt-4o",
  temperature=0.9,
  messages=[
    {"role": "system", "content": "너는 유치원 학생이야. 유치원생처럼 답변해줘."}, # system : AI가 어떤 톤·성격·규칙으로 대화해야 하는지를 알려주는 최상위 지침
    {"role": "user", "content": "참새"}, # user : 사람이 AI에게 하는 질문/명령
    {"role": "assistant", "content": "짹짹"}, # assistant : 과거에 했던 응답을 저장해 대화의 흐름을 유지
    {"role": "user", "content": "오리"},
  ]
)

print(response)

print('----')
print(response.choices[0].message.content) 
