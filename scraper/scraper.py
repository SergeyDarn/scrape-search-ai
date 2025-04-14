from scraper.selenium_scraper import SeleniumScraper
from utils.html_parser import HtmlParser
from utils.array_utils import ArrayUtils

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
        
        scraped_main_page = self.scrape_single_page(self.main_url, True)
        main_page_object = self._build_content_object(self.main_url, scraped_main_page["title"], scraped_main_page["content"])

        scraped_pages = self._scrape_website_pages(scraped_main_page["urls"], url_limit)
        
        #print('website_content', website_content)
        print("-----------------------------")
        print("-----------------------------")
        print(f"Scraping of website: {self.main_url} took {time.perf_counter() - time1}s")
        print("-----------------------------")
        print("-----------------------------")

        return [main_page_object] + scraped_pages


    # todo: add correct return type
    def scrape_single_page(self, url: str, get_page_links = False):
        time1 = time.perf_counter()
        
        website_html = self.scrapper.scrape_single_page(url)
        website_content = self.html_parser.parse(website_html)
        website_title = self.html_parser.get_title(website_html)
        
        page_links = []
        
        if get_page_links:
            page_links = self.html_parser.get_links(website_html, url, self.url_to_include)
            
        print("-----------------------------")
        print(f"Scraping of url: {url} took {time.perf_counter() - time1}s")
        print("-----------------------------")
        
        return {
            "title": website_title,
            "content": website_content,
            "urls": page_links
        }


    def _scrape_website_pages(
        self,
        page_links: List[str],
        url_limit: int = math.inf
    ):
        page_urls = page_links.copy()
        scraped_urls = [self.main_url]
        scraped_content = []
        url_counter = 1
        
        while ((len(page_urls) > 0) and (url_counter < url_limit)):
            page_url = page_urls[-1].strip()
            
            try:
                scraped_urls.index(page_url)
            except:
                scraped_urls.append(page_url)

                scraped_page = self.scrape_single_page(page_url, True)
                filtered_res_urls = ArrayUtils.filter_array(scraped_page["urls"], scraped_urls)
                page_urls = ArrayUtils.combine_arrays(page_urls, filtered_res_urls)
                
                if scraped_page["content"]:
                    content_object = self._build_content_object(page_url, scraped_page["title"], scraped_page["content"])
                    scraped_content.append(content_object)

            page_urls.pop(-1)
            url_counter += 1
            
        return scraped_content
        

    # todo: type properly
    def _build_content_object(self, url: str, title: str, content: str): 
        return {
            "title": title,
            "url": url,
            "content": content
        }
