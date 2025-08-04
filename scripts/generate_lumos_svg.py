from bs4 import BeautifulSoup
import requests

username = "FernandaFregulha"
url = f"https://github-contributions-api.deno.dev/{username}.svg"

response = requests.get(url)
svg = BeautifulSoup(response.text, "html.parser").find("svg")

if not svg:
    raise Exception("Gráfico de contribuições não encontrado!")

for rect in svg.find_all("rect"):
    fill = rect.get("fill", "").lower()
    if fill in ("#ebedf0", "#ffffff", "#000000"):
        continue
    rect["fill"] = "#00ff99"  # Altere a cor conforme desejado

with open("output.svg", "w", encoding="utf-8") as f:
    f.write(str(svg))
