from bs4 import BeautifulSoup
import requests
from .base import ScraperStrategy
import asyncio
from playwright.async_api import async_playwright

async def verificar_disponibilidade():
    async with async_playwright() as p:
        print("entrou")
        browser = await p.chromium.launch(headless=True)  # headless=True significa sem abrir janela para debugar setar como FALSE
        page = await browser.new_page()
        await page.goto('https://relvaco.com.br/produto/camiseta-oversized-inferno-basica')
        await page.wait_for_selector('.js-product-variants-group')
   
        #Nesse site tem um overlay então tem que fechar
        close_layer = page.locator(".p-close")
        if await close_layer.is_visible():
            await close_layer.click()
            await page.wait_for_timeout(1000)

        # Espera o botão do tamanho ficar disponível
        await page.locator("#product_form a[title='G']").first.wait_for(state="visible") #fazer entrada do tamanho por parametro depois
        # Clica no botão G
        await page.locator("#product_form a[title='G']").first.click()
        
        # Espera o botão atualizar após selecionar o tamanho
        await page.wait_for_selector("input.js-addtocart", state="attached")

        botao = await page.query_selector("input.js-addtocart")
        value = await botao.get_attribute("value")
        await browser.close()


        disponibilidade = value.strip().lower()
        if "comprar" in disponibilidade:
            return("Produto disponível!")
        else:
            return(f"Indisponível: '{value}'")

class RelvaScraper(ScraperStrategy):
    async def extrair_info(self, url: str) -> dict:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extração do nome do produto
        nome = soup.find('h1').text.strip()

        # Extração do preço
        preco_element = soup.find('div', class_='js-price-display')  # Substitua pela classe correta do preço
        preco_original = soup.find('div', class_='js-compare-price-display')  # Substitua pela classe correta do preço
        preco = preco_element.text.strip() if preco_element else 'Preço não encontrado'
        preco_original = preco_original.text.strip() if preco_original else preco

        estoque = await verificar_disponibilidade()

        return {"nome": nome, "preco": preco, "preco original": preco_original,"estoque": estoque, "url": url}