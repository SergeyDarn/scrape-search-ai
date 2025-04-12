import streamlit as st
from web_ui.ui_interface import UiInterface

class StreamlitUi(UiInterface):
    def add_title(self, title: str) -> str:
        return st.title(title)
        
    # todo: add return type
    def add_button(self, text: str):
        return st.button(text)
    
    def add_text(self, text: str) -> str:
        return st.write(text)
    
    def add_input(self, title: str) -> str:
        return st.text_input(title)
    
    # todo: add return type
    def add_accordion(self, text: str):
        return st.expander(text)
    
    # todo: add return type
    def add_textarea(self, title: str, content: str = "", height: int = 300):
        return st.text_area(title, content, height=height)
    

    def set_session_var(self, name, value):
        st.session_state[name] = value
    
    def get_session_var(self, name):
        return st.session_state[name]
    
    def has_session_var(self, name):
        return name in st.session_state
