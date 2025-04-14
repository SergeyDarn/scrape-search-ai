import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service

from scraper.scraper_interface import ScraperInterface
from utils.string_utils import StringUtils


class SeleniumScraper(ScraperInterface):
    def scrape_single_page(
        self,
        url: str,
        auth_cookie_name: str = "",
        auth_cookie_value: str = ""
    ) -> str:
        # todo: как-то универсализировать установку драйвера
        # todo: добавить инструкцию для мака по разрешению на то, чтобы запустить этот скрипт в security (или если это будет запускать в докере - таких проблем не должно быть)
        # drivers download: https://googlechromelabs.github.io/chrome-for-testing/#stable
        chrome_driver_path = "./chromedriver"
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")

        driver = webdriver.Chrome(
            service=Service(chrome_driver_path),
            options=options
        )
        
        try:
            driver.get(url)
            
            if (auth_cookie_name and auth_cookie_value):
                if (driver.get_cookie(auth_cookie_name)):
                    driver.delete_cookie(auth_cookie_name)

                driver.add_cookie({
                    "name": auth_cookie_name,
                    "value": auth_cookie_value,
                    "domain": "." + StringUtils.get_domain(url),
                    "path": "/admin"
                })
                
                driver.get(url)
            
            html = driver.page_source
            
            return html
        finally:
            driver.quit()