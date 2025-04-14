import streamlit as st
from ai.ask_ai import ask_ai
from ai.ai_db import AiDb

st.set_page_config(
    page_title="Задай вопрос",
    page_icon="❓",
)

# ToDo: учесть пустой кейс, разобраться как получить список колекций
# collection = st.selectbox("Выберите таблицу")
# todo: сделать ui для удаления коллекций
st.title("Задай свой вопрос")
collection = st.text_input("Имя коллекции")

# todo: move this inside if
question = st.text_input("Вопрос")
ai_db = AiDb()

if (st.button("Спросить")):
    query_res = ai_db.query_collection(collection, question, 5)
    # todo: handle empty documents
    res = ask_ai(question, query_res["documents"][0])
    
    # todo later: pass url metadata to ai too
    
    st.write(res)