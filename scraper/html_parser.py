from bs4 import BeautifulSoup
from typing import List
from scraper.string_utils import StringUtils

class HtmlParser:
    def parse(self, html: str) -> str:
        body = self.get_body(html)

        return self.clean_html(body)
    

    def get_links(self, html: str, main_link: str, url_to_include: str) -> str:
        html_soup = BeautifulSoup(html, "html.parser")
        links = []

        for link_tag in html_soup.find_all('a'):
            href = link_tag.get('href')

            if (not url_to_include or (href.find(url_to_include) != -1)):
                links.append(href)
                
        links = self._process_links(main_link, links)

        return links
        

    # Todo: add return type
    def get_body(self, html: str):
        soup = BeautifulSoup(html, "html.parser")
        body = str(soup.body) if soup.body else ""
        
        return body


    def clean_html(self, html: str) -> str:
        html = self._remove_scripts_and_styles(html)
        
        return self._remove_empty_lines(html)


    def _remove_scripts_and_styles(self, html: str) -> str:
        html_soup = BeautifulSoup(html, "html.parser")
        
        for script_or_style in html_soup([ "script", "style" ]):
            script_or_style.extract()
            
        return html_soup.get_text(separator="\n")


    def _remove_empty_lines(self, html: str) -> str:
        # todo: figure out how this works
        return "\n".join(
            line.strip() for line in html.splitlines() if line.strip()
        )
        
    def _process_links(self, main_url: str, urls: List[str]) -> List[str]:
        mapped_urls = []
        main_base_url = StringUtils.get_base_url(main_url)

        print('main_base_url', main_base_url)

        for url in urls:
            url = main_base_url + StringUtils.get_relative_url(url)
            
            try:
                mapped_urls.index(url)
            except:
                mapped_urls.append(url)
                pass

        return mapped_urls
            
        
    
        
    