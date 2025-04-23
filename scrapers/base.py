from abc import ABC, abstractmethod

class ScraperStrategy(ABC):
    @abstractmethod
    def extrair_info(self, url: str) -> dict:
        pass