## 가상환경 활성화하기 : .\venv\Scripts\activate
# 사용자가 입력한 텍스트에 대화 형식으로 응답을 생성하는 기능 = Chat Completion을 사용해서 GPT 에게 2022년  월드컵 우승 팀을 물어보고 답변을 받아옴
from openai import OpenAI # 오픈AI 라이브러리를 가져오기
# pip install python-dotenv 설치 후 .env .gitignore 파일을 이용해 API KEY 노출 관리 
from dotenv import load_dotenv # dotenv 라이브러리를 가져오기
import os

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY') # 환경 변수에서 API 키 가져오기
client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
  model="gpt-4o", # 어떤 모델 사용 설정
  temperature=0.1, # 정확한 답변 = 0에 가깝게, 창의적인 답변 = 1에 가깝게
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "2022년 월드컵 우승팀은 어디야?"},
  ]	
)

print(response)

print('----')
print(response.choices[0].message.content) 
