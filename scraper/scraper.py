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

        page_links = scrape_res["urls"]
        scraped_urls = [self.main_url]
        scraped_content = [
            self._build_content_object(self.main_url, scrape_res["title"], scrape_res["content"])
        ]
        url_counter = 1

        # todo: move to another function
        while ((len(page_links) > 0) and (url_counter < url_limit)):
            link = page_links[-1].strip()
            
            try:
                scraped_urls.index(link)
            except:
                res = self.scrape_single_page(link, True)
                scraped_urls.append(link)
                filtered_res_urls = ArrayUtils.filter_array(res["urls"], scraped_urls)
                page_links = ArrayUtils.combine_arrays(page_links, filtered_res_urls)
                
                if res["content"]:
                    scraped_content.append(
                        self._build_content_object(link, res["title"], res["content"])
                    )

            page_links.pop(-1)
            url_counter += 1
        
        #print('website_content', website_content)
        print("-----------------------------")
        print("-----------------------------")
        print(f"Scraping of website: {self.main_url} took {time.perf_counter() - time1}s")
        print("-----------------------------")
        print("-----------------------------")

        return scraped_content


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

    # todo: type properly
    def _build_content_object(self, url: str, title: str, content: str): 
        return {
            "title": title,
            "url": url,
            "content": content
        }
