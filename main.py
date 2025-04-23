from factory.scraper_factory import ScraperFactory
import asyncio
import json

urls = [
    "https://relvaco.com.br/produto/camiseta-oversized-inferno-basica",
    "https://www.relvaco.com.br/produtos/camiseta-oversized-abelha/"
]

def salva_registro(dados):
    with open("Resultado.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
        print("Dados salvos com sucesso!")

async def main():
    dados = []
    for url in urls:
        try:
            scraper = ScraperFactory.get_scraper(url)
            produto = await scraper.extrair_info(url)
            dados.append(produto)
        except Exception as e:
            print(f"Erro ao processar {url}: {e}")
    salva_registro(dados)
if __name__ == "__main__":
    asyncio.run(main())