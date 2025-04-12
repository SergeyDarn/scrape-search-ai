from scraper.selenium_scraper import SeleniumScraper
from scraper.html_parser import HtmlParser

scrapper = SeleniumScraper()
html_parser = HtmlParser()

def scrape(website: str):
    website_html = scrapper.scrape(website)
    website_content = html_parser.parse(website_html)
    
    print("Scrapped website content", website_content)
    print("------------------------------------")
    print("------------------------------------")
    
    return website_content;