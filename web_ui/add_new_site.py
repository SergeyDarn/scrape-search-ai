import streamlit as st

WEBSITE_CONTENT_KEY = "WEBSITE_CONTENT"

# todo: add typing to functions
def add_new_site(scraper_fn, ask_ai_fn):
    st.title("Добавить сайт")
    # todo: url validation
    website = st.text_input("Введите урл сайта: ")
    
    if (st.button("Scrape site")):
        st.write("Scrapping site")

        website_content = scraper_fn(website)
        st.session_state[WEBSITE_CONTENT_KEY] = website_content
        
        with st.expander("View DOM Content"):
            st.text_area("DOM Content", website_content, 300)
            
            
    if (WEBSITE_CONTENT_KEY in st.session_state):           
        question = st.text_area("What do you want to ask?")
            
        if (st.button("Ask") and question):
            print(f"Your question is: {question}")
            st.write("Ai is thinking...")

            result = ask_ai_fn(question, st.session_state[WEBSITE_CONTENT_KEY])
            st.write(f"Result: {result}")
        