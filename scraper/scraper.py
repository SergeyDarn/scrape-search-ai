from scraper.selenium_scraper import SeleniumScraper
from scraper.html_parser import HtmlParser
from scraper.array_utils import ArrayUtils

from typing import List
import math
import time


class Scraper:
    def __init__(self):
        self.scrapper = SeleniumScraper()
        self.html_parser = HtmlParser()
        
    def set_main_url(self, main_url: str):
        self.main_url = main_url
        return self
        
    def set_url_to_include(self, url_to_include: str):
        self.url_to_include = url_to_include
        return self
        
    def set_auth_cookie_name(self, auth_cookie_name: str):
        self.auth_cookie_name = auth_cookie_name
        return self
        
    def set_auth_cookie_value(self, auth_cookie_value: str):
        self.auth_cookie_value = auth_cookie_value
        return self
        

    # todo: сделать асинхронный скрейп сразу нескольких страниц, чтобы это происходило быстрее
    def scrape_website(self, url_limit: int = math.inf) -> List[str]:
        time1 = time.perf_counter()
        
        scrape_res = self.scrape_single_page(self.main_url, True)

        page_links = scrape_res["links"]
        scrapped_urls = [self.main_url]
        scrapped_content = [scrape_res["content"]]
        url_counter = 1
        
        while ((len(page_links) > 0) and (url_counter < url_limit)):
            link = page_links[-1]
            
            try:
                scrapped_urls.index(link)
            except:
                res = self.scrape_single_page(link, True)
                scrapped_content.extend(res["content"])
                page_links = ArrayUtils.combine_arrays(page_links, res["links"])

            page_links.pop(-1)
            url_counter += 1
        
        #print('website_content', website_content)
        print("-----------------------------")
        print("-----------------------------")
        print(f"Scrapping for website: {self.main_url} took {time.perf_counter() - time1}s")
        print("-----------------------------")
        print("-----------------------------")

        return scrapped_content
            

    # todo: add correct return type
    def scrape_single_page(self, url: str, get_page_links = False):
        time1 = time.perf_counter()
        
        website_html = self.scrapper.scrape_single_page(url)
        website_content = self.html_parser.parse(website_html)
        
        page_links = []
        
        if get_page_links:
            page_links = self.html_parser.get_links(website_html, url, self.url_to_include)
            
        print("-----------------------------")
        print(f"Scrapping for page: {url} took {time.perf_counter() - time1}s")
        print("-----------------------------")
        
        return {
            "content": website_content,
            "links": page_links
        }
