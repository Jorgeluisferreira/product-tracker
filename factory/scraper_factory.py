from scrapers.relva import RelvaScraper

class ScraperFactory:
    @staticmethod
    def get_scraper(url: str):
        if "relvaco.com" in url:
            return RelvaScraper()
        else:
            raise ValueError("Loja não suportada")
