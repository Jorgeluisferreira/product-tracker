from factory.scraper_factory import ScraperFactory
import asyncio

urls = [
    "https://relvaco.com.br/produto/camiseta-oversized-inferno-basica",
]

async def main():
    for url in urls:
        try:
            scraper = ScraperFactory.get_scraper(url)
            info = await scraper.extrair_info(url)
            print(info)
        except Exception as e:
            print(f"Erro ao processar {url}: {e}")

if __name__ == "__main__":
    asyncio.run(main())