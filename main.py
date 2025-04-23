from factory.scraper_factory import ScraperFactory

urls = [
    "https://relvaco.com.br/produto/camiseta-oversized-inferno-basica",
]

for url in urls:
    try:
        scraper = ScraperFactory.get_scraper(url)
        info = scraper.extrair_info(url)
        print(info)
    except Exception as e:
        print(f"Erro ao processar {url}: {e}")
