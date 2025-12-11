# pip install streamlit
# streamlit = 파이썬 프로그램을 웹 기반 UI로 구현할 수 있게 해주는 프레임워크
# 실행문 : streamlit run "D:\LLMStudy\chap03\3-3.스트림릿으로 챗봇 완성하기\1. streamlit_basic.py"
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# (0) 사이드바에서 api_key 입력하는 부분 
with st.sidebar:
    openai_api_key = os.getenv('OPENAI_API_KEY') 
    "[Github](https://github.com/yujinchoi2030/LLM)"
    "[Naver](https://www.naver.com/)"

st.title("💬 Chatbot")

# (1) st.session_state에 "messages"가 없으면 초기값을 설정
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# (2) 대화 기록을 출력
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# (3) 사용자 입력을 받아 대화 기록에 추가하고 AI 응답을 생성
if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt}) 
    st.chat_message("user").write(prompt) 
    response = client.chat.completions.create(model="gpt-4o", messages=st.session_state.messages) 
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg}) 
    st.chat_message("assistant").write(msg)
