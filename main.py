from web_ui.run_web_app import run_web_app
from scraper.scrape import scrape
from ai.ask_ai import ask_ai

run_web_app(scrape, ask_ai)
