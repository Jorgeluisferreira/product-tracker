# Product tracker

Product tracker é um serviço que criei para uso pessoal e estudo de programação, onde o sistema poderia informar diariamente se algum produto que ele tem interesse está em promoção.

## Como funciona ?

O sistema faz uma especie de webscrap no site da loja, utilizando o url do produto que o usuario quer que seja monitorado.
Como cada site possui layouts diferentes, é necessario criar um "scraper" utilizando como base a classe abstrata no arquivo "scrapers/base.py"

## Sites suportados até o momento

relvaco - https://www.relvaco.com.br
