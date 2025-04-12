import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service

from scraper.scraper_interface import ScraperInterface


class SeleniumScraper(ScraperInterface):
    def scrape(self, website: str) -> str:
        print("Launching Chrome browser...")

        # todo: как-то универсализировать установку драйвера
        # todo: добавить инструкцию для мака по разрешению на то, чтобы запустить этот скрипт в security (или если это будет запускать в докере - таких проблем не должно быть)
        # drivers download: https://googlechromelabs.github.io/chrome-for-testing/#stable
        chrome_driver_path = "./chromedriver"
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(
            service=Service(chrome_driver_path),
            options=options
        )
        
        try:
            driver.get(website)
            print("Page Loaded")
            
            html = driver.page_source
            
            return html
        finally:
            driver.quit()