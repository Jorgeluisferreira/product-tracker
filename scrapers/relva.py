from bs4 import BeautifulSoup
import requests
from .base import ScraperStrategy

class RelvaScraper(ScraperStrategy):
    def extrair_info(self, url: str) -> dict:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extração do nome do produto
        nome = soup.find('h1').text.strip()

        # Extração do preço
        preco_element = soup.find('div', class_='js-price-display')  # Substitua pela classe correta do preço
        preco_original = soup.find('div', class_='js-compare-price-display')  # Substitua pela classe correta do preço
        preco = preco_element.text.strip() if preco_element else 'Preço não encontrado'
        preco_original = preco_original.text.strip() if preco_original else 'Preço não encontrado'

        estoque = 'ainda n funciona' if 'Esgotado' not in soup.text else 'Esgotado'

        return {"nome": nome, "preco": preco, "preco original": preco_original,"estoque": estoque}