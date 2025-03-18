import os

# Estrutura de pastas e arquivos
folders = ["web-scraper", "web-scraper/data"]
files = ["web-scraper/scraper.py", "web-scraper/requirements.txt", "web-scraper/README.md", "web-scraper/data/resultados.txt"]

# Criar pastas
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Criar arquivos vazios
for file in files:
    with open(file, "w") as f:
        pass

print("Estrutura do Web Scraper criada com sucesso! 🚀")
