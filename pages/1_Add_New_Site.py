import streamlit as st

from scraper.scrape import scrape
from ai.ask_ai import ask_ai
from web_ui.add_new_site import add_new_site


st.set_page_config(
    page_title="Добавить сайт",
    page_icon="🕸️",
)

add_new_site(scrape, ask_ai)

