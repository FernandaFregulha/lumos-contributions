
from bs4 import BeautifulSoup
import requests

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
        rect["fill"] = "#111111"
        rect["data-lit"] = "no"
    else:
        rect["fill"] = "#FFD700"
        rect["data-lit"] = "yes"

width = svg.get("width", "720")
height = svg.get("height", "110")

sparkles = "\n".join([
    f'<circle cx="{50 + i * 20}" cy="{int(height)-10 - (i%5)*10}" r="2" fill="#FFD700">'
    f'<animate attributeName="opacity" values="0;1;0" dur="2s" begin="{i * 0.3}s" repeatCount="indefinite" /></circle>'
    for i in range(10)
])

lumos_text = f'<text x="{int(int(width)/2)}" y="30" text-anchor="middle" font-size="24" fill="#FFD700" font-family="serif">LUMOS<animate attributeName="opacity" values="1;0.6;1" dur="1.8s" repeatCount="indefinite" /></text>'

wand = f'<rect x="{int(width)//2 - 2}" y="{int(height)-10}" width="4" height="40" fill="#FFD700" rx="1" transform="rotate(-45 {int(width)//2} {int(height)-10})" />'

svg_wrapper = f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{int(height)+50}" viewBox="0 0 {width} {int(height)+50}"><rect width="100%" height="100%" fill="#000000"/>{str(svg)}{wand}{lumos_text}{sparkles}</svg>'

with open("lumos_contributions.svg", "w") as f:
    f.write(svg_wrapper)
