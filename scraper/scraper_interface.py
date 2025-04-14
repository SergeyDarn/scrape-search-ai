class ScraperInterface:
    def scrape_single_page(
        self,
        url: str,
        auth_cookie_name: str = "",
        auth_cookie_value: str = ""
    ) -> str:
        pass