import streamlit as st
from fastapi_app.chatbot.assistant import get_answer

st.title('Привет, мир!')
st.write('Это мой умный корпоративный ассистент.')

# Создаем форму для ввода данных пользователем
with st.form(key='my_form'):
    text_input = st.text_input(label='Введите текст')
    submit_button = st.form_submit_button(label='Отправить')

# Выводим данные, введенные пользователем
#if text_input:
#    st.write(f'Вы ввели: {text_input}')
#    answer = get_answer(document = text_input)
#    st.write(f'Ваш ответ: {answer}')

# Выводим данные, введенные пользователем
if text_input:
    st.write(f'Вы ввели: {text_input}')
    answer = get_answer_with_sources(document = text_input)
    st.write(f'Ваш ответ: {answer}')
    st.write(f'Источники: {sources}')
