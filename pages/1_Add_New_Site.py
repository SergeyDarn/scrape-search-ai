import streamlit as st

from web_ui.scrape_new_site import scrape_new_site


st.set_page_config(
    page_title="Добавить сайт",
    page_icon="🕸️",
)

scrape_new_site()

