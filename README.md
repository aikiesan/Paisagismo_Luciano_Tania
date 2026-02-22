# Projeto Luciano e Tania — Paisagismo

Projeto de paisagismo residencial desenvolvido por **Tanus Saab** e **Gustavo Valencio**.

## Sobre

Website de apresentação do projeto com:
- **Espécies Selecionadas** — galeria de plantas (a ser adicionada)
- **Planta Baixa 2D** — layout técnico do projeto
- **Visualizações 3D** — 46 renders fotorrealísticos

## Tecnologias

- HTML5, CSS3, JavaScript puro (sem frameworks)
- Design responsivo mobile-first
- WebP image optimization com lazy loading
- Lightbox modal para visualização ampliada
- Animações suaves e parallax scrolling

## Visualizações 3D

Renders 3D desenvolvidos por **Lucas Nakamura Cerejo**.

## Estrutura do Projeto

```
/
├── index.html                    # Website principal (single-page)
├── logo_tanus_saab.png          # Logo Tanus Saab
├── .gitignore                   # Configuração Git
├── README.md                    # Este arquivo
└── public/
    └── images/
        ├── species/             # Espécies (a adicionar)
        │   └── thumbs/
        ├── plans/               # Planta baixa
        │   ├── PLANTA_2D_LUCIANO.webp
        │   └── thumbs/
        └── renders/             # 46 visualizações 3D
            ├── scene-01.webp ... scene-46.webp
            └── thumbs/
```

## Como Visualizar Localmente

1. Abra o arquivo `index.html` diretamente em seu navegador
2. Ou use um servidor local simples:
   ```bash
   # Python 3
   python -m http.server 8000

   # Node.js
   npx serve
   ```
3. Acesse `http://localhost:8000`

## Deployment GitHub Pages

Este projeto está configurado para GitHub Pages:

1. **URL:** `https://[username].github.io/[repo-name]/`
2. **Branch:** `main`
3. **Pasta:** `/ (root)`

### Deploy Automático

Qualquer push para a branch `main` atualiza automaticamente o site em 1-3 minutos.

## Adicionando Espécies de Plantas

Para adicionar a galeria de espécies:

1. **Prepare as imagens:**
   - Formato WebP (otimizado)
   - Full-size: 800-1200px largura → `public/images/species/`
   - Thumbnails: 400px largura → `public/images/species/thumbs/`

2. **Edite `index.html`:**
   - Localize a seção "PAGE 2 — ESPÉCIES" (linha ~891)
   - Substitua o `.species-placeholder` por `.species-grid`
   - Adicione cards de espécies seguindo o padrão:
   ```html
   <div class="species-grid">
       <div class="species-card" onclick="openLightbox(this)">
           <img src="public/images/species/thumbs/nome-da-planta.webp"
                data-full="public/images/species/nome-da-planta.webp"
                alt="Nome Comum" class="species-image" loading="lazy" decoding="async">
           <div class="species-info">
               <div class="species-name">Nome Comum</div>
               <div class="species-scientific">Nome científico</div>
               <div class="species-description">Descrição da planta...</div>
           </div>
       </div>
       <!-- Repita para cada espécie -->
   </div>
   ```

3. **Commit e push:**
   ```bash
   git add public/images/species/ index.html
   git commit -m "Add plant species gallery"
   git push origin main
   ```

## Características do Design

- **Paleta de Cores:** Tons de concreto quente (#F3F2F0, #EAEAE6)
- **Tipografia:** Cormorant Garamond (serifada) + Lato (sans-serif)
- **Responsividade:**
  - Mobile (≤768px): navegação inferior, uma seção por vez
  - Tablet (769-1023px): menu hamburger
  - Desktop (≥1024px): navegação completa, scroll entre seções
- **Animações:** Fade-in ao scroll, parallax no hero, hover effects

## Créditos

- **Projeto de Paisagismo:** Tanus Saab e Gustavo Valencio
- **Visualizações 3D:** Lucas Nakamura Cerejo
- **Website:** Baseado na arquitetura do projeto Casa EVA

---

© 2026 Tanus Saab Paisagismo — Todos os direitos reservados.
