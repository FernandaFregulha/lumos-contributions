# 🔮 GitHub LUMOS Contribution Grid

Este projeto usa GitHub Actions para gerar um gráfico de contribuições estilo **"LUMOS"** (com efeitos mágicos), baseado nos blocos reais do seu perfil GitHub.

### 💡 Como funciona

- Usa BeautifulSoup para pegar o gráfico SVG do seu perfil
- Aplica animações:
  - ✨ Blocos iluminados
  - 🌟 Faíscas subindo
  - 🪄 Varinha mágica e título animado
- Atualiza o SVG automaticamente todos os dias via GitHub Actions

---

### 📦 Como usar

1. Fork este repositório
2. Altere o nome de usuário no script Python (`scripts/generate_lumos_svg.py`)
3. Ative o GitHub Pages se quiser servir o SVG por URL

---

### 🧙 Resultado

No seu `README.md`:

```html
<img src="assets/lumos_contributions.svg" alt="LUMOS Contribution Grid" />
```
