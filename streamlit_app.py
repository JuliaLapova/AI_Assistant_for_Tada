import streamlit as st
from fastapi_app.chatbot.assistant import get_answer

openai_api_key = "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"

st.title('Привет, мир!')
st.write('Это мой умный корпоративный ассистент.')

# Создаем форму для ввода данных пользователем
with st.form(key='my_form'):
    text_input = st.text_input(label='Введите текст')
    submit_button = st.form_submit_button(label='Отправить')

# Выводим данные, введенные пользователем
if text_input:
    st.write(f'Вы ввели: {text_input}')
    answer = get_answer(document = text_input)
    st.write(f'Ваш ответ: {answer}')
