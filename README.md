# Ressona

Identitat digital per a artistes.

## Requisits

- [Hugo](https://gohugo.io/) v0.159+ (extended edition)

## Clonar i executar

```bash
git clone git@github.com:112books/ressona.eu.git
cd ressona.eu
hugo server --buildDrafts -p 1313
```

Obre `http://localhost:1313/` al navegador.

## Estructura

```
ressona.eu/
├── assets/css/        — estils (Swiss + Bauhaus + Jazz)
├── content/           — pàgines (ca/ per defecte, en/)
├── i18n/              — textos traduïts (ca.yaml, en.yaml)
├── layouts/           — plantilles Hugo
│   ├── _default/      — baseof.html
│   ├── partials/      — header.html, footer.html
│   └── index.html     — pàgina principal
├── static/img/        — SVGs del logotip
├── hugo.toml          — configuració
└── CLAUDE.md          — especificacions del projecte
```

## Build per producció

```bash
hugo --minify
```

El site es genera a `public/`.

## Desplegament

Automatitzat amb GitHub Actions. En pushing a `main` es desplega a GitHub Pages.
