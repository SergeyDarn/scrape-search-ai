from bs4 import BeautifulSoup

class HtmlParser:
    def parse(self, html: str) -> str:
        soup = BeautifulSoup(html, "html.parser")
        # todo: test that this line will work
        body = str(soup.body) if soup.body else ""

        return self._clean_html(body)


    def _clean_html(self, html: str) -> str:
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
    