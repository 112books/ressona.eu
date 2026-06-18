# Pla d'Acció SEO — ressona.eu
**Creat:** 2026-06-15 · **Actualitzat:** 2026-06-18 · Puntuació inicial: 49/100 · Objectiu 3 mesos: 72/100

---

## ✅ COMPLETAT

| # | Acció | Data |
|---|-------|------|
| C1 | `public/` fora del repo git | 2026-06-18 |
| C2 | Meta description 150 chars (CA+EN) | 2026-06-15 |
| C3 | "Barcelona" al `hero_desc` i18n | 2026-06-15 |
| C4 | Logo PNG 874×874 al schema Organization | 2026-06-18 |
| C5 | `static/llms.txt` creat | 2026-06-15 |
| A1 | Google Fonts non-blocking (preload/onload) | 2026-06-15 |
| A2 | JSON-LD complet: `@id`, address, areaServed, hasOfferCatalog | 2026-06-15 |
| A3 | `robots.txt` amb GPTBot, ClaudeBot, PerplexityBot, OAI-SearchBot | 2026-06-15 |
| A4 | Descripcions de servei expandides (CA+EN) | 2026-06-15 |
| A5 | Hero tagline: `visibility:hidden` eliminat del CSS, ocultació JS-driven | 2026-06-18 |
| A6 | `apple-touch-icon` + GoatCounter HTTPS | 2026-06-15 |
| M1 | Secció "Qui som": Joan Mz, Barcelona, Pocallum, LinuxBCN, 112books | 2026-06-18 |
| M3 | Camp `<select>` interès al formulari de contacte | 2026-06-15 |
| M4 | `/legal/` index: `_build: render: never` | 2026-06-18 |
| M5 | IndexNow ping a deploy workflow (Bing) | 2026-06-15 |
| M6 | Sitemap producció: URLs `https://ressona.eu/` ✓ | 2026-06-18 |
| M7 | SVGs decoratives: `aria-hidden="true"` | 2026-06-15 |
| E1 | Pàgines de servei: 5 pàgines CA+EN (identitat visual, foto, web, press kit, cercadors) | 2026-06-18 |

---

## ⏳ PENDENT — Esperar primer client

### M2 — Prova social [1h]
Afegir un testimoni real o frase de volum a la homepage.
**Bloqueig:** Ressona és nova. Activar quan es tanqui el primer client (Ladies First?).
Opcions:
- Testimoni real amb permís
- "Hem acompanyat X artistes a Barcelona"

---

## 📋 BAIX — Backlog (quan toqui)

### B1 — `translationKey` a pàgines legals
Afegir `translationKey: avis-legal` (i equivalents) al front matter de cada pàgina legal per generar hreflang correcte al sitemap.
**Fitxers:** `content/legal/*.md` i `content/en/legal/*.md`

### B2 — Cloudflare davant de GitHub Pages
Mou DNS a Cloudflare (gratuït). Guanys: security headers, CDN, www→apex redirect, analytics Lighthouse.

### B3 — `humans.txt` actualitzar
Eliminar o actualitzar camp `Twitter: @linuxbcn` → handle Ressona quan existeixi.

### B4 — `_headers` file (si es migra a Cloudflare Pages)
```
/*
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=()
```

---

## 🎯 ESTRATÈGIC — Horitzó 3-6 mesos

### E2 — Blog `/recursos/` (3 articles inicials)
1. "Com construir la identitat digital com a artista emergent a Barcelona"
2. "Què ha de tenir un press kit digital d'actor el 2026"
3. "Les 7 coses que necessita el web d'una escola de dansa"

Cada article: 1.000-1.500 paraules, link intern a la pàgina de servei.

### E3 — Perfil Google Business ⚠️ alta prioritat local
Crear i verificar Google Business Profile per a Ressona.
Condició per aparèixer al "3-pack" local: "web per a artistes Barcelona", "assessoria digital artistes".

### E4 — Canal YouTube
3-5 vídeos de 60-90 segons sobre identitat digital per a artistes.
Afegir URL del canal a `sameAs` del schema Organization.
**Per què:** Correlació 0.737 amb citació a ChatGPT.

### E5 — Wikidata entity
Crear entrada Wikidata per a Ressona (organització, sector: consultoria identitat digital, Barcelona).
Afegir URL a `sameAs`. Millora la resolució d'entitat en grafs de coneixement IA.
