from web_ui.streamlit_ui import StreamlitUi
from web_ui.ui_interface import UiInterface

ui: UiInterface = StreamlitUi()

WEBSITE_CONTENT_KEY = "WEBSITE_CONTENT"

# todo: add typing to function
def run_web_app(scraper_fn, ask_ai_fn):
    ui.add_title("Ai web scrapper")
    # todo: url validation
    website = ui.add_input("Enter website url: ")
    
    if (ui.add_button("Scrape site")):
        ui.add_text("Scrapping site")

        website_content = scraper_fn(website)
        ui.set_session_var(WEBSITE_CONTENT_KEY, website_content)
        
        with ui.add_accordion("View DOM Content"):
            ui.add_textarea("DOM Content", website_content, 300)
            
            
    if (ui.has_session_var(WEBSITE_CONTENT_KEY)):           
        question = ui.add_textarea("What do you want to ask?")
            
        if (ui.add_button("Ask") and question):
            print(f"Your question is: {question}")
            ui.add_text("Ai is thinking...")

            result = ask_ai_fn(question, ui.get_session_var(WEBSITE_CONTENT_KEY))
            ui.add_text(f"Result: {result}")
        
            
    