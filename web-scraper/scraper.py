import requests
from bs4 import BeautifulSoup
import os

def scrape_website(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Erro ao acessar o site")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Exemplo: Coletar todos os títulos de artigos (h2)
    titles = soup.find_all("h2")
    
    # Salvar os dados coletados
    data_path = "web-scraper/data/resultados.txt"
    with open(data_path, "w", encoding="utf-8") as file:
        file.write("Títulos encontrados:\n")
        for title in titles:
            file.write(f"- {title.get_text()}\n")
    
    print("Dados salvos em", data_path)

if __name__ == "__main__":
    url = input("Digite a URL do site para coletar dados: ")
    scrape_website(url)
