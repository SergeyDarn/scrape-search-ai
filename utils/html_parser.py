from bs4 import BeautifulSoup
from typing import List
from utils.string_utils import StringUtils

class HtmlParser:
    def parse(self, html: str) -> str:
        body = self.get_body(html)

        return self.clean_html(body)
    
    def get_title(self, html: str) -> str:
        html_soup = self._parse_html(html)
        
        return html_soup.title.name if html_soup.itlte else ""
        

    def get_links(self, html: str, main_link: str, url_to_include: str) -> str:
        html_soup = self._parse_html(html)
        links = []

        for link_tag in html_soup.find_all('a'):
            href = link_tag.get('href')
            
            if (not url_to_include or (href and href.find(url_to_include) != -1)):
                links.append(href)
                
        links = self._process_links(main_link, links)

        return links
        

    def get_body(self, html: str) -> str:
        soup = self._parse_html(html)
        body = str(soup.body) if soup.body else ""
        
        return body


    def clean_html(self, html: str) -> str:
        html = self._remove_scripts_and_styles(html)
        
        return self._remove_empty_lines(html)


    def _remove_scripts_and_styles(self, html: str) -> str:
        html_soup = self._parse_html(html)
        
        for script_or_style in html_soup([ "script", "style" ]):
            script_or_style.extract()

        return html_soup.get_text()


    def _remove_empty_lines(self, html: str) -> str:
        return "\n".join(
            line.strip() for line in html.splitlines() if line.strip()
        )
        
    def _process_links(self, main_url: str, urls: List[str]) -> List[str]:
        mapped_urls = []
        main_base_url = StringUtils.get_base_url(main_url)

        for url in urls:
            url = main_base_url + StringUtils.get_relative_url(url)
            url = url.strip()
            
            try:
                mapped_urls.index(url)
            except:
                mapped_urls.append(url)
                pass

        return mapped_urls
    
    def _parse_html(self, html: str) -> BeautifulSoup:
        return BeautifulSoup(html, "html.parser")
            
        
    
        
    