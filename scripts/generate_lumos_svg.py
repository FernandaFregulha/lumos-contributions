from bs4 import BeautifulSoup
import requests
import os

username = "FernandaFregulha"
url = f"https://github.com/{username}"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
svg = soup.find("svg", {"class": "js-calendar-graph-svg"})

if not svg:
    raise Exception("Gráfico de contribuições não encontrado!")

for rect in svg.find_all("rect"):
    fill = rect.get("fill", "").lower()
    if fill in ("#ebedf0", "#ffffff", "#000000"):
        rect["fill"] = "#202020"  # cor dos blocos "apagados"

# Garante que a pasta "assets" existe
os.makedirs("assets", exist_ok=True)

# Salva o SVG 
with open("assets/lumos_contributions.svg", "w", encoding="utf-8") as f:
    f.write(str(svg))
