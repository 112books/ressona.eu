# Ressona — Identitat digital per a artistes

## Concepte
Ressona és una marca d'assessoria i acompanyament en identitat digital per a artistes. Neix de la combinació de **Pocallum** (fotografia, identitat visual) i **LinuxBCN** (tecnologia, infraestructura, automatització).

El nom prové de *ressonar*: fer eco, vibrar.

## Públic
Músics, actors, circ, dansa, arts plàstiques, creadors emergents.

## Paleta real (web)
| Color | Hex | Ús |
|-------|-----|-----|
| Fons | `#34454c` | fons principal |
| Text | `#d9d0d5` | cos, llegibilitat |
| Gold | `#fdbf68` | accent principal |
| Red | `#501345` | accent secundari, blocs |
| Blue | `#c0a9b3` | accent fred |

## Tipografia
- **Syne** (700, 800): titulacions, marca
- **Inter** (300, 400, 500): cos

## Navegació
- 4 ítems: icona SVG inline + label (només desktop), smooth scroll
- Switcher d'idioma: `CA` / `EN` text, mai banderetes

## Estructura (single page)
1. **Hero**: marca massiva gradient + tagline typing + desc fade-in
2. **Què fem** (10 serveis): icona visible, text apareix on hover (desktop) / sempre visible (mobile)
3. **Per a qui** (6 perfils): float-in aleatori, color invert on hover
4. **Com ho fem** (5 passos): eix central, desc apareix on hover (desktop) / sempre visible (mobile)
5. **Contacte**: form fetch + inline feedback
6. **Footer**: links, powered by LinuxBCN

## SEO/Accesibilitat (2026-06-12)
- canonical, hreflang (CA, EN, x-default), sitemap.xml, robots.txt
- OG + Twitter cards (imatge `ressona-eu-rounded.png`)
- JSON-LD: WebSite + Organization + BreadcrumbList
- `<title>` i meta description dinàmics per pàgina
- `role="img"` + `aria-label` a tots els SVGs (22 icones)
- Títols dinàmics (p. ex. "Avís legal · Ressona")
- humans.txt

## Logotip (wordmark «Яessona»)
Markup idèntic al hero, header i footer:

```html
<span class="flip-r">R</span><span class="brand-grad">e<span class="shift-up">s</span><span class="shift-down">s</span><span class="shift-down">o</span>na</span>
```

- **La «R» invertida (`.flip-r`) és text pla en `--gold`**: `color` + `-webkit-text-fill-color` daurats i `background: none` explícit; el mirall es fa amb `transform: scaleX(-1)`. **No ha de dependre mai d'una capa `background-clip: text`**: si aquesta capa falla o es repinta en un pla separat (s'ha vist en algunes compilacions de Chromium/Brave), queda a la vista el crema `#ece4d9` del degradat de sota i el glif apareix **blanc**. Incident: 2026-10-18, commit `cab24e7`.
- **El degradat viu a `.brand-grad`**, que només embolcalla «essona»: `linear-gradient(135deg, #ece4d9 0%, #ece4d9 8%, var(--gold) 48%, var(--red) 100%)` retallat a text. Els stops 8/48 reprodueixen el degradat original (20/55/100) descomptant l'amplada de la R.
- **Prohibit**: `background-clip: text` o `-webkit-text-fill-color: transparent` sobre l'element que conté la R; `transform: translateZ(0)` al `.hero-brand` (forçava capa GPU i afavoria el repintat fantasma).
- `@supports not ((-webkit-background-clip: text) or (background-clip: text))` → el wordmark es pinta daurat sòlid, mai invisible.
- Artwork canònic (SVG, mateixa R invertida): portada de la guia de marca `static/admin/brand/index.html` i `static/img/ressona-logo*.svg`.

## Animacions
- **Hero brand**: ressonància (`heroResonance`, CSS, 1.4s)
- **Tagline**: typing efecte amb cursor gold (JS, 35-60ms per char, 800ms delay)
- **Hero desc**: fade-in 2.5s (CSS)
- **Serveis**: icona visible per defecte, hover → icona s'esvaeix + text apareix
- **Audience**: float-in aleatori (JS, `--drift-x/y`), hover → color invert
- **Process steps**: eix vertical central, desc hidden, reveal on hover
- **Progress bar**: 2px gradient bar + percentage + scroll-to-top button

## Analytics
- **GoatCounter**: `ressona.goatcounter.com`, privacy-friendly (sense cookies)
- **Dashboard**: `ressona.eu/admin/` — Chart.js, SHA-256 auth (sessionStorage)
- **Workflow**: `.github/workflows/fetch-analytics.yml` (cada hora)
- **Scripts**: `scripts/build-analytics-json.py` + `scripts/process-analytics.py`
- **Secret**: `GOATCOUNTER_TOKEN`

## Admin dashboard (`/admin/`)
- Protegit amb SHA-256 (mateixa contrasenya que el site)
- Estil: fons `#34454c`, text `#d9d0d5`, accent gold `#fdbf68`
- KPIs, chart visites (Chart.js), idiomes, seccions, dispositius, pàgines
- `sessionStorage` per mantenir sessió
- NO staticrypt (el site públic és obert)

## Social media
- Estratègia: `ressona-docs/xarxes/ESTRATEGIA.md` — IG/FB/LI, 1 cop/setmana, 5 formats
- Generador: `/admin/plantilla.html` — 4 layouts (cita/servei/perfil/proces), 5 bgs, 6 icones, logo original, html2canvas → PNG download + clipboard, auth SHA-256

## Deploy
- GitHub Actions: `.github/workflows/deploy.yml`
- Trigger: push a `main`
- Hugo build → gh-pages branch
- `static/` es copia directament (admin, img, robots.txt, humans.txt)
- Sense Node.js / staticrypt (public site open, admin auth via JS)

## 404
- `layouts/404.html` — pàgina personalitzada amb enllaç "Tornar / Go back"

## Google Search Console
- Domini verificat via TXT record
- Sitemap: `https://ressona.eu/sitemap.xml` (automàtic, Hugo genera)

## Estructura de fitxers
```
ressona.eu/
├── assets/css/main.css (~1111 línies)
├── content/
│   ├── _index.md / en/_index.md
│   └── legal/ (avis-legal, privacitat, cookies) + en/
├── i18n/ (ca.yaml, en.yaml)
├── layouts/
│   ├── 404.html
│   ├── _default/baseof.html (SEO meta + JSON-LD + JS animacions)
│   ├── _default/single.html (pàgines legals)
│   ├── partials/ (header.html, footer.html, progress.html)
│   └── index.html (single page + form fetch)
├── scripts/ (build-analytics-json.py, process-analytics.py)
├── static/
│   ├── admin/ (index.html amb auth + dashboard, plantilla.html amb auth)
│   ├── img/ (logotips SVG, PNG 874×874 OG, PNG 192 favicon)
│   ├── CNAME, robots.txt, humans.txt
├── .github/workflows/ (deploy.yml, fetch-analytics.yml)
├── hugo.toml
└── CLAUDE.md
```

## Estratègia de continguts (recursos)
Els articles de recursos sempre són **contingut de captació**: informació útil i real, però amb l'objectiu final d'atraure clients per a les filials del grup:

- **Ressona**: assessoria identitat digital per a artistes (servei principal)
- **Pocallum** (pocallum.cat): fotografia professional, identitat visual, disseny gràfic, impressió (cartells, voladors, llibres via 112Books)
- **LinuxBCN** (linuxbcn.com): tecnologia, infraestructura, automatització, solucions a mida (newsletters, webs, etc.)
- **112Books**: projectes editorials impresos (llibres, cartells, voladors)

Regles per als articles:
- Aportar **informació genuïnament útil** — no vendre directament
- **No explicar-ho tot**: el contingut ha d'atraure, no substituir la consulta
- Quan sigui natural, **recomanar les filials sempre com "Ressona treballa amb…"** (p. ex. "Ressona treballa amb Pocallum per a fotografia i identitat visual", "Ressona treballa amb LinuxBCN per a la infraestructura digital"). **MAI** com "A Pocallum treballen…" o "Des de LinuxBCN ofereixen…" — les filials no parlen soles, Ressona les coordina.
- Mai en primera persona col·lectiva quan es parla de les filials ("fem", "treballem") — la veu és sempre "Ressona" com a marca integradora
- Les CTAs al final d'article redirigeixen al formulari de contacte (`/en/#contacte` o `/#contacte`)

## Regles
1. **SVG inline**: icons fetes a mà, sense llibreries
2. **Zero JS dependencies**: tret de GoatCounter i Chart.js (admin)
3. **Idiomes**: mai barrejar, switcher text «CA» / «EN», mai banderetes
4. **Contrast**: text sempre llegible sobre fons fosc
5. **Asimetria + espai negatiu**: trets de disseny fonamentals
6. **Blocs de color**: gold, red, blue com a fons de serveis i perfils
7. **Wordmark**: la «R» sempre en color pla (`--gold`), el degradat només a `.brand-grad` — mai `background-clip: text` sobre la R (vegeu § Logotip)

---

## Control horari

Skill actiu: `gestor-hores` — registra automàticament el temps de treball per sessió.

- Logs a `.taques/ressona.eu/YYYY-MM-DD.md` (creat automàticament)
- Comandes: `/time-log [tasca] [hores]`, `/time-report [periode]`, `/time-config [hores] [tarifa]`
- No modificar manualment els fitxers `.taques/` — són append-only
