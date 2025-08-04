import os
import requests

# Nome de usuário (sempre minúsculo)
username = "fernandafregulha"

# URL direta para o SVG do gráfico de contribuições
svg_url = f"https://github.com/{username}/{username}/raw/main/lumos_only_contributions.svg"

# Cabeçalho com User-Agent para evitar bloqueios
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Faz requisição para o SVG
response = requests.get(svg_url, headers=headers)

# Verifica se a requisição foi bem-sucedida
response.raise_for_status() # Levanta um erro para códigos de status HTTP ruins (4xx ou 5xx)

# Cria a pasta de destino se não existir
os.makedirs("assets", exist_ok=True)

# Salva o SVG em arquivo
output_path = "assets/lumos_contributions.svg"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(response.text)

print(f"✅ SVG salvo em: {output_path}")


