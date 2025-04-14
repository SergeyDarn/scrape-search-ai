import re

class StringUtils:
    @staticmethod
    def get_base_url(url: str) -> str:
        if (not url):
            return ""
        
        matches = re.findall("https?\:\/\/[^/]*\/", url)
        
        return matches[0] if (len(matches) > 0) else ""
    
    @staticmethod
    def get_relative_url(url: str) -> str:
        if (not url):
            return ""

        base_url = StringUtils.get_base_url(url)
        
        url = url.replace(base_url, '').lstrip('/')
        url = StringUtils.remove_get_parameters_and_hash(url)
        
        return url

    @staticmethod
    def remove_get_parameters_and_hash(url: str) -> str:
        if (not url):
            return ""

        return re.sub("[?#][^\/]*$", "", url)
    
    @staticmethod
    def get_domain(url: str) -> str:
        if (not url):
            return ""

        base_url = StringUtils.get_base_url(url)
        domain = re.sub("https?:\/\/", "", base_url)

        return domain.rstrip('/')