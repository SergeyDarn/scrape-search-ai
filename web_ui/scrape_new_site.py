import streamlit as st

WEBSITE_CONTENT_KEY = "WEBSITE_CONTENT"

from scraper.scraper import Scraper
from ai.ask_ai import ask_ai

scraper = Scraper()

# todo: add typing to functions, and give function a better name
def scrape_new_site():
    st.title("Добавить сайт")
    # todo: url validation, make sure that logic works both with http url and without it
    main_url = st.text_input("Введите урл сайта для скрепинга: ")
    url_substr = st.text_input("Введите доп фильтрацию для урлов сайта (опционально): ")
    auth_cookie_name = st.text_input("Введите имя куки для авторизации (опционально): ")
    auth_cookie_value = st.text_input("Введите значение куки для авторизации (опционально): ")
    
    if (st.button("Scrape site")):
        st.write("Scrapping site")
        
        (scraper
            .set_main_url(main_url)
            .set_url_to_include(url_substr)
            .set_auth_cookie_name(auth_cookie_name)
            .set_auth_cookie_value(auth_cookie_value)
        )
            
        res = scraper.scrape_website(5)
        # st.session_state[WEBSITE_CONTENT_KEY] = website_content
        
        #with st.expander("View DOM Content"):
         #   st.text_area("DOM Content", website_content, 300)
            
            
    #if (WEBSITE_CONTENT_KEY in st.session_state):           
    #    question = st.text_area("What do you want to ask?")
            
    #    if (st.button("Ask") and question):
    #        print(f"Your question is: {question}")
    #        st.write("Ai is thinking...")

    #        result = ask_ai_fn(question, st.session_state[WEBSITE_CONTENT_KEY])
    #        st.write(f"Result: {result}")
        
        
        
        