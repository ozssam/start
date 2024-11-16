import streamlit as st
import google.generativeai as genai
from langchain.prompts import PromptTemplate

st.title('6하원칙 작문기')

# Gemini API 키 입력 받기
api_key = st.text_input('Gemini API 키를 입력하세요:', type='password')

if api_key:
    # Gemini 모델 설정
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash-002')

    # 6하원칙 입력 받기
    who = st.text_input('누가: ')
    when = st.text_input('언제: ')
    where = st.text_input('어디서: ')
    what = st.text_input('무엇을: ')
    how = st.text_input('어떻게: ')
    why = st.text_input('왜: ')

    if st.button('작문하기'):
        try:
            # 6하원칙을 하나의 문장으로 조합
            principle = f"{who}이(가) {when}, {where}에서 {what}을(를) {how} 했다. 그 이유는 {why}이다."
            
            # Gemini를 사용하여 자연스러운 글 생성
            prompt = f"다음 6하원칙을 바탕으로 자연스러운 글을 작성해주세요: {principle}"
            response = model.generate_content(prompt)
            
            st.session_state.generated_result = response.text
            
        except Exception as e:
            st.error(f"에러가 발생했습니다: {e}")

    if 'generated_result' in st.session_state:
        st.subheader('생성된 결과:')
        st.write(st.session_state.generated_result)
