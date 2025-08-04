import os
import requests
from bs4 import BeautifulSoup

# Nome de usuário (sempre minúsculo)
username = "fernandafregulha"
url = f"https://github.com/{username}"

# Cabeçalho com User-Agent para evitar bloqueios
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Faz requisição para o perfil do GitHub
response = requests.get(url, headers=headers)

# Faz o parsing do HTML
soup = BeautifulSoup(response.text, "html.parser")

# Busca o SVG do gráfico de contribuições
svg = soup.find("svg", {"class": "js-calendar-graph-svg"})

# Verifica se encontrou o SVG
if not svg:
    raise Exception("Gráfico de contribuições não encontrado!")

# Cria a pasta de destino se não existir
os.makedirs("assets", exist_ok=True)

# Salva o SVG em arquivo
output_path = "assets/lumos_contributions.svg"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(str(svg))

print(f"✅ SVG salvo em: {output_path}")
