import os
import requests
from bs4 import BeautifulSoup

# Nome de usuário (sempre minúsculo)
username = "fernandafregulha"

# URL direta para o gráfico de contribuições do GitHub (retorna HTML)
url = f"https://github.com/users/{username}/contributions"

# Cabeçalho com User-Agent para evitar bloqueios
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Faz requisição para a página HTML
response = requests.get(url, headers=headers)

# Verifica se a requisição foi bem-sucedida
response.raise_for_status()

# Analisa o HTML com BeautifulSoup
soup = BeautifulSoup(response.text, 'lxml')

# O GitHub agora usa uma tabela HTML em vez de SVG para o gráfico de contribuições
# Vamos procurar pelos elementos <td> que representam os dias de contribuição
contribution_days = soup.find_all('td', class_='ContributionCalendar-day')

if contribution_days:
    print(f"Encontrados {len(contribution_days)} dias de contribuição")
    
    # Calcula as dimensões do SVG com base no número de dias
    # O GitHub exibe 53 semanas (colunas) e 7 dias (linhas)
    num_weeks = (len(contribution_days) + 6) // 7 # Arredonda para cima para garantir todas as semanas
    svg_width = num_weeks * 13  # 13px por quadrado (incluindo espaçamento)
    svg_height = 7 * 13  # 7 dias * 13px por quadrado
    
    # Criando o conteúdo SVG sem usar f-string para evitar problemas com caracteres especiais
    svg_content = f'<svg width="{svg_width}" height="{svg_height}" xmlns="http://www.w3.org/2000/svg">\n'
    svg_content += '''    <defs>
        <filter id="glow">
            <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
            <feMerge> 
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
    </defs>
    <style>
        .day-0 { fill: #ebedf0; }
        .day-1 { fill: #9be9a8; }
        .day-2 { fill: #40c463; }
        .day-3 { fill: #30a14e; }
        .day-4 { fill: #216e39; }

        @keyframes pulse-glow {
            0% { filter: url(#glow); opacity: 0.7; }
            50% { filter: url(#glow); opacity: 1; }
            100% { filter: url(#glow); opacity: 0.7; }
        }

        .glowing-rect {
            animation: pulse-glow 2s infinite alternate;
        }
    </style>
'''
    
    # Adiciona os retângulos para cada dia
    for i, day in enumerate(contribution_days):
        level = int(day.get('data-level', 0))
        
        # Calcula a posição x e y baseado no índice
        week = i // 7
        day_of_week = i % 7
        
        x = week * 13  # Ajustado para o novo tamanho do quadrado
        y = day_of_week * 13 # Ajustado para o novo tamanho do quadrado
        
        # Adiciona o retângulo para todos os dias
        # Aplica a classe 'glowing-rect' apenas se houver contribuições (level > 0)
        if level > 0:
            svg_content += f'    <rect x="{x}" y="{y}" width="10" height="10" class="day-{level} glowing-rect"/>\n'
        else:
            svg_content += f'    <rect x="{x}" y="{y}" width="10" height="10" class="day-{level}"/>\n'
    
    svg_content += '</svg>'
    
    # Salva o SVG modificado em arquivo
    output_path = "assets/lumos_contributions.svg"
    os.makedirs("assets", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    
    print(f"✅ SVG salvo em: {output_path}")
else:
    print("❌ Não foi possível encontrar os elementos de contribuição na página.")