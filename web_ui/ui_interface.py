 # todo: figure out how to properly do interfaces in python and handle incorrect inheretance
class UiInterface:
    def add_title(self, title: str) -> str:
        pass
    
    # todo: add return type
    def add_button(self, text: str):
        pass
    
    def add_text(self, text: str) -> str:
        pass
    
    def add_input(self, title: str) -> str:
        pass
    
     # todo: add return type
    def add_accordion(self, text: str):
        pass
    
    # todo: add return type
    def add_textarea(self, title: str, content: str, height: int) -> str:
        pass
    

    def set_session_var(self, name, value):
        pass
    
    def get_session_var(self, name):
        pass
    
    def has_session_var(self, name):
        pass