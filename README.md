# Web Scraper

Este é um simples Web Scraper desenvolvido em Python que coleta títulos de artigos (tags `<h2>`) de uma página da web e os salva em um arquivo de texto.

## 📌 Funcionalidades
- Acessa uma URL fornecida pelo usuário
- Extrai todos os títulos (h2) da página
- Salva os dados no arquivo `data/resultados.txt`

## 📂 Estrutura do Projeto
```
web-scraper/
│-- scraper.py           # Código principal do scraper
│-- requirements.txt     # Dependências do projeto
│-- data/                # Pasta para armazenar os dados extraídos
│   │-- resultados.txt   # Arquivo com os dados coletados
│-- README.md            # Explicação do projeto
```

## 🚀 Como Usar
### 1️⃣ Instalar as dependências
No terminal, dentro da pasta do projeto, execute:
```sh
pip install -r requirements.txt
```
Ou instale manualmente:
```sh
pip install requests beautifulsoup4
```

### 2️⃣ Executar o Web Scraper
```sh
python scraper.py
```
Digite a URL do site desejado e pressione **Enter**.

### 3️⃣ Ver os dados coletados
Os títulos extraídos serão salvos em:
```
data/resultados.txt
```
Abra o arquivo para visualizar os resultados.

## 🔧 Personalização
Caso queira extrair outras informações, edite o código dentro de `scraper.py`, alterando a linha:
```python
titles = soup.find_all("h2")
```
Para, por exemplo, coletar links:
```python
links = soup.find_all("a")
```

## 📜 Licença
Este projeto é de código aberto e pode ser modificado livremente.

---
Criado por Sabrina Cristina Ilha Silva 🚀
