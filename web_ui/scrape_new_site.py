import streamlit as st

WEBSITE_CONTENT_KEY = "WEBSITE_CONTENT"

from scraper.scraper import Scraper
from ai.db.ai_db import AiDb

# todo: move classes init inside a function
scraper = Scraper()
aiDb = AiDb()

# todo: add typing to functions, and give function a better name
def scrape_new_site():
    st.title("Добавить сайт")
    # todo: url validation, make sure that logic works both with http url and without it
    site_name = st.text_input("Введите имя сайта (на английском, без пробелов): ")
    main_url = st.text_input("Введите урл сайта для скрепинга: ")
    # todo: расширить логику до урлов через запятую + добавить урлы исключения (для админки мадженты)
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
            
        scraped_content = scraper.scrape_website()
        aiDb.add_documents(site_name, scraped_content)
        # st.session_state[WEBSITE_CONTENT_KEY] = res["content"]
        
        #with st.expander("View DOM Content"):
        #   st.text_area("DOM Content", scraped_content[0]["content"], 300)

    #if (WEBSITE_CONTENT_KEY in st.session_state):           
    #    question = st.text_area("What do you want to ask?")
            
    #    if (st.button("Ask") and question):
    #        print(f"Your question is: {question}")
    #        st.write("Ai is thinking...")

    #        result = ask_ai_fn(question, st.session_state[WEBSITE_CONTENT_KEY])
    #        st.write(f"Result: {result}")
        
        
        
        