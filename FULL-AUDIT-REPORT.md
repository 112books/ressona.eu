# Full SEO Audit — ressona.eu
**Data:** 2026-06-15
**Model:** Claude Sonnet 4.6 · 6 agents paral·lels
**Cobertura:** Technical · Content · Schema · Performance · GEO/AI · SXO

---

## Puntuació Global de Salut SEO: 49 / 100

| Categoria | Pes | Puntuació | Weighted |
|---|---|---|---|
| Technical SEO | 22% | 61/100 | 13.4 |
| Content Quality | 23% | 41/100 | 9.4 |
| On-Page SEO | 20% | 45/100 | 9.0 |
| Schema / Structured Data | 10% | 35/100 | 3.5 |
| Performance (CWV) | 10% | 70/100 | 7.0 |
| AI Search Readiness | 10% | 38/100 | 3.8 |
| Imatges | 5% | 60/100 | 3.0 |
| **TOTAL** | | | **49.1 / 100** |

---

## Resum Executiu

### Negoci detectat
Consultoria d'identitat digital per a artistes escènics i creadors. Mercat local (Barcelona / Catalunya) + abast remot. Bilingüe CA/EN. Marca nova (<2 anys). Presència social mínima (Instagram únic canal extern).

### Top 5 Problemes Crítics

1. **"Barcelona" no existeix al lloc** — cap menció a la pàgina principal, títol, meta description, schema, ni body text. Per a tota cerca local, el site és invisible.
2. **Contingut extremadament prim** — ~240 paraules visibles. Descripcions de servei de 8-12 paraules. Per sota de qualsevol llindar de citació per IA o de cobertura temàtica per a Google.
3. **`llms.txt` inexistent** — el fitxer més directe per a visibilitat en IA (ChatGPT, Perplexity, Claude) no existeix.
4. **Meta description = slogan** — "Identitat digital per a artistes" (34 chars). Google ho reescriurà automàticament de forma descontrolada.
5. **Schema JSON-LD desconnectat** — `WebSite` i `Organization` no estan vinculats per `@id`. El logo apunta a un SVG (Google requereix PNG/JPG). Manca `ProfessionalService`.

### Top 5 Quick Wins (< 30 min cadascun)

1. Afegir "Barcelona" al hero_desc + meta description
2. Reescriure la meta description (150 chars) a `content/_index.md`
3. Canviar logo a PNG en el schema (`ressona-eu-rounded-192.png`)
4. Afegir `public/` al `.gitignore`
5. Crear `static/llms.txt` (plantilla a la secció GEO)

---

## 1. Technical SEO — 61/100

### Problemes Crítics

**CRIT-1 — `public/` commitejat amb URLs localhost**
El directori `public/` al repo conté un build de `hugo server` (dev), no producció. Tots els canonicals, hreflang, OG tags i JSON-LD usen `http://localhost:60818/`. Si mai es deploya manualment, el site desapareix de Google en dies.
- Fix: `echo "public/" >> .gitignore`
- Risc: el deploy via GitHub Actions és correcte, però el fitxer commitejat és un artefacte perillós.

**CRIT-2 — Verificar `sitemap.xml` en producció**
El `robots.txt` apunta a `https://ressona.eu/sitemap.xml`. El `hugo.toml` té `baseURL = "https://ressona.eu/"`. Verificar: `curl -s https://ressona.eu/sitemap.xml | head -5` → ha de mostrar `https://ressona.eu/`, no `http://localhost`.

### Problemes Alts

**HIGH-1 — Google Fonts bloqueja el render (LCP)**
La stylesheet de Google Fonts (`fonts.googleapis.com`) es carrega com a recurs bloquejant. El `<h1 class="hero-brand">` en Syne 800 és l'element LCP, i depèn d'aquesta font externa. Estimació: +400-900ms de LCP en mobile.

Fix immediat (baseof.html, ~15 min):
```html
<!-- Reemplaçar la línia del link stylesheet per: -->
<link rel="preload" as="style"
  href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500&family=Syne:wght@700;800&display=swap"
  onload="this.onload=null;this.rel='stylesheet'">
<noscript>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500&family=Syne:wght@700;800&display=swap">
</noscript>
```
Nota: també elimina Inter 600 i Syne 600 (no s'utilitzen al CSS).

**HIGH-2 — Hero tagline JS-dependent**
`.hero-tagline` té `visibility: hidden` per defecte i s'omple via JS (800ms delay). Crawlers que llegeixen HTML inicial veuen un element buit. El `<noscript>` mitiga parcialment però és fràgil.

Fix: eliminar `visibility: hidden` del CSS per defecte. Fer que el JS sigui additiu (aplica l'efecte de cursor, no buida el text).

**HIGH-3 — Cap header de seguretat**
GitHub Pages no permet configurar headers. El site serveix sense `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy`, ni `HSTS`. Impacta Lighthouse Security score.

Fix: posar Cloudflare davant (free tier) i afegir headers via Transform Rules o un `_headers` file si es migra a Cloudflare Pages.

### Problemes Mitjans

| # | Problema | Fix ràpid |
|---|---|---|
| MED-1 | Pàgines legals sense `translationKey` (no apareixen hreflang al sitemap) | Afegir `translationKey` al front matter de cada legal |
| MED-2 | `/legal/` section index genera URL prima | Afegir `_build: { render: never }` a `content/legal/_index.md` |
| MED-3 | `WebSite` JSON-LD apareix a CA i EN (duplicat) | Wrappar amb `{{ if and .IsHome (eq .Language.Lang "ca") }}` |
| MED-4 | `Organization.logo` és SVG (Google requereix PNG) | Canviar a `/img/ressona-eu-rounded-192.png` |
| MED-5 | Sense `www` → apex redirect confirmat | Configurar a Cloudflare (301 `www.ressona.eu` → `ressona.eu`) |
| MED-6 | Sense IndexNow | Afegir step a `deploy.yml` + clau a `static/` |

### Problemes Baixos

| # | Problema | Fix |
|---|---|---|
| LOW-1 | Sense `apple-touch-icon` | Afegir `<link rel="apple-touch-icon" href="/img/ressona-eu-rounded-192.png">` |
| LOW-2 | GoatCounter carrega via `//gc.zgo.at` (protocol-relative) | Canviar a `https://gc.zgo.at` |
| LOW-3 | SVG decorativa (ull) té `aria-label="Ressona"` | Canviar a `aria-hidden="true"`, eliminar `role="img"` |
| LOW-4 | `humans.txt` menciona Twitter: @linuxbcn | Actualitzar o eliminar camp Twitter |

### Comprovacions que passen ✓
- `robots.txt` sintaxi correcta, `/admin/` bloquejat
- Viewport meta present
- HTTPS baseURL al hugo.toml
- Pàgina 404 personalitzada
- hreflang CA/EN/x-default (template correcte)
- `hugo --minify --baseURL` al deploy workflow
- Anchor IDs coincideixen amb nav links
- CSS `scroll-behavior: smooth`
- OG image, Twitter card configurats
- GoatCounter `async`, scroll listener `{ passive: true }`
- ARIA labels a les 22 icones SVG
- Checkbox GDPR al formulari

---

## 2. Content Quality — 41/100

### Recompte de paraules visibles
**~240 paraules en CA.** El mínim per a una pàgina principal amb pretensions SEO és 500. La bretxa és de ~260 paraules.

### E-E-A-T Breakdown

| Dimensió | Score | Principals mancances |
|---|---|---|
| Experience (20%) | 30/100 | Zero casos d'estudi, zero exemples de feina, zero resultats quantificats |
| Expertise (25%) | 42/100 | La llista de serveis és coherent i actual (IA search inclosa). Però cap descripció arriba a demostrar mètode |
| Authoritativeness (25%) | 25/100 | Únic canal extern: Instagram. Sense LinkedIn, sense premsa, sense vincle amb institucions culturals |
| Trustworthiness (30%) | 55/100 | Email, GDPR, pàgines legals, HTTPS. Falta adreça física, telèfon, equip nomenat |

### Problemes Crítics de Contingut

**La meta description és el tagline (34 chars)**
Google la reescriurà. Recomanació:
```
Ressona acompanya músics, actors, balladors i artistes a construir
la seva identitat digital a Barcelona: web, press kit, xarxes i 
estratègia. Parlem.
```
(~150 chars) — editar a `content/_index.md` camp `description:`

**"Assessoria" no existeix al site**
El mot que els artistes utilitzen per buscar serveis de consultoria digital no apareix ni una sola vegada al site. Ni al títol, ni al body, ni al schema, ni a les metadades.

**Descripcions de servei de 8-12 paraules**
Exemples actuals:
- "La mirada que et distingeix. Logotip, paleta, to. La base." (10 p)
- "Aparador. Eina. Agenda. Tot connectat, tot al seu lloc." (9 p)

Funcionen com a microcòpia d'UI. No funcionen com a contingut per a crawlers. Target: 50-80 paraules per servei.

**Sense senyal geogràfica**
"Barcelona" o "Catalunya" no apareixen en cap lloc. Per a cerca local i per a citació per IA de serveis locals, és una omissió estructural.

**Sense prova social**
Zero testimonis, zero clients nomenats (ni anonimitzats), zero resultats quantificats. Per a la persona B (músic professional en fase de consideració), és el principal bloqueig a la conversió.

### Problemes Mitjans

| Problema | Fitxer | Fix |
|---|---|---|
| OG description = tagline (34 chars) | `content/_index.md` | Afegir camp `description:` (el template l'hereda automàticament) |
| Sense `dateModified` al schema | `baseof.html` | Afegir `"dateModified": "{{ now.Format "2006-01-02" }}"` |
| Versió EN idèntica a CA | `content/en/_index.md` + `i18n/en.yaml` | Afegir paràgraf diferenciador per a artistes internacionals |
| `contactType: "customer support"` incorrecte | `baseof.html` | Canviar a `"sales"` |

---

## 3. Schema / Structured Data

### Validació del que existeix

**WebSite** ✓ estructura vàlida, però:
- Cap `@id` — no pot vincular-se a Organization
- `inLanguage: "ca"` — hauria de ser `["ca", "en"]`
- `publisher` absent — Google no sap a qui pertany el site

**Organization** ✓ estructura vàlida, però:
- `logo` apunta a SVG → Google Knowledge Panel requereix PNG/JPG
- Cap `@id` — desconnectat de WebSite
- Sense `description`, `address`, `areaServed`, `knowsLanguage`
- Sense `foundingDate`, `founder` (opcionals però valuosos)
- `sameAs` conté únicament Instagram

**BreadcrumbList** ✓ lògica correcta per a pàgines no-home. Risc menor: possible trailing comma quan `Kind == "section"`.

### JSON-LD millorat (llest per implementar)

**Bloc 1 — WebSite** (substituir existent a `baseof.html`):
```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "@id": "https://ressona.eu/#website",
  "name": "Ressona",
  "alternateName": "Ressona — Identitat digital per a artistes",
  "url": "https://ressona.eu/",
  "description": "Assessoria i acompanyament en identitat digital per a artistes. Web, identitat visual, press kit, xarxes i alta a cercadors.",
  "inLanguage": ["ca", "en"],
  "publisher": { "@id": "https://ressona.eu/#organization" }
}
```

**Bloc 2 — Organization** (substituir existent):
```json
{
  "@context": "https://schema.org",
  "@type": ["Organization", "ProfessionalService"],
  "@id": "https://ressona.eu/#organization",
  "name": "Ressona",
  "description": "Assessoria i acompanyament en identitat digital per a artistes. Combina fotografia, identitat visual, tecnologia i automatització.",
  "url": "https://ressona.eu/",
  "logo": {
    "@type": "ImageObject",
    "url": "https://ressona.eu/img/ressona-eu-rounded.png",
    "width": 874,
    "height": 874
  },
  "image": "https://ressona.eu/img/ressona-eu-rounded.png",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Barcelona",
    "addressRegion": "Catalunya",
    "addressCountry": "ES"
  },
  "areaServed": { "@type": "Country", "name": "Spain" },
  "knowsLanguage": ["ca", "es", "en"],
  "email": "hola@ressona.eu",
  "contactPoint": {
    "@type": "ContactPoint",
    "email": "hola@ressona.eu",
    "contactType": "sales",
    "availableLanguage": ["Catalan", "Spanish", "English"]
  },
  "sameAs": ["https://www.instagram.com/ressona_identitat_digital/"],
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Serveis Ressona",
    "itemListElement": [
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Identitat visual", "description": "Logotip, paleta de color i to de comunicació. La base visual de la marca artística." } },
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Fotografia i vídeo", "description": "Sessions fotogràfiques i de vídeo pensades per al press kit de l'artista." } },
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Web sincronitzada", "description": "Lloc web com a aparador, eina i agenda. Tot connectat." } },
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Press kit digital", "description": "Bio, fotos, vídeos i contacte en un sol lloc accessible per a programadors i mitjans." } },
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Alta a cercadors i IA", "description": "Posicionament a Google, Bing, Perplexity i ChatGPT per a artistes." } },
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Xarxes automàtiques", "description": "Gestió i automatització de xarxes socials per a artistes." } },
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Estratègia de xarxes", "description": "Calendari editorial, formats i veu per a xarxes socials d'artistes." } },
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "IA amb criteri", "description": "Integració d'eines d'intel·ligència artificial en el flux creatiu i de comunicació." } },
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Cartelleria i materials", "description": "Pòsters, flyers i targetes de visita. El disseny que passa a paper." } }
    ]
  }
}
```

---

## 4. Performance

### Estimació de puntuació PSI (sense API key)

| Estratègia | Estimació | Confiança |
|---|---|---|
| Mobile | 65–75 | Mitjana |
| Desktop | 88–94 | Mitjana |

### Core Web Vitals

**LCP — Risc MITJÀ-ALT**
Element candidat: `<h1 class="hero-brand">` en Syne 800 a `clamp(6rem, 18vw, 14rem)`. Depèn de font externa via Google Fonts. Sense `<link rel="preload">` per al .woff2. Estimació: +400-900ms en mobile 4G.

**INP — Risc BAIX**
JS mínim, scroll listener `passive`, analytics `async`. Cap framework JS. INP probablement en rang "Good" (<200ms).

**CLS — Risc BAIX-MITJÀ**
Risc principal: font swap amb `display=swap` sense `size-adjust` pot causar reflow visible al hero brand (font size ~14rem). No hi ha `<img>` sense dimensions. El progress bar no causa shift.

### Pes total estimat: ~150KB ✓
(sense rasters inline, tot SVG, JS inline mínim)

### Oportunitats d'optimització

| Prioritat | Acció | Estalvi estimat |
|---|---|---|
| Alta | Google Fonts no-blocking (preload/onload trick) | 400-900ms LCP |
| Alta | Eliminar Inter 600 + Syne 600 del URL de Fonts | ~60KB |
| Mitjana | `will-change: transform` al `.hero-brand` | Compositor GPU layer |
| Baixa | Autohostejar fonts (eliminar dependència CDN) | ~150ms cold connection |

**Artefacte de dev:** `public/index.html` conté `livereload.js` script. Confirmar que NO apareix en producció (`curl -s https://ressona.eu/ | grep livereload`).

---

## 5. GEO / AI Search Readiness — 38/100

| Dimensió | Pes | Score |
|---|---|---|
| Citabilitat | 25% | 28/100 |
| Llegibilitat estructural | 20% | 45/100 |
| Senyals d'autoritat | 20% | 35/100 |
| Accessibilitat tècnica | 20% | 52/100 |
| Contingut multimodal | 15% | 30/100 |

### Accessibilitat per crawlers IA

| Crawler | Estat |
|---|---|
| GPTBot | Permès (implícit via `*`) |
| OAI-SearchBot | Permès (implícit) |
| ClaudeBot | Permès (implícit) |
| PerplexityBot | Permès (implícit) |
| CCBot (training) | Permès (implícit — potser no desitjat) |

**Falta:** regles named-agent explícites al `robots.txt`.

### `llms.txt` — No existeix

És el gap d'impacte més alt. Plantilla mínima per a `static/llms.txt`:

```
# Ressona

> Ressona és una consultoria d'identitat digital per a artistes 
> amb seu a Barcelona. Ajudem músics, actors, ballarins, companyies 
> de circ i artistes visuals a construir una presència digital 
> coherent: identitat visual, fotografia, web, press kit, xarxes 
> socials i alta a cercadors i IA.

Contacte: hola@ressona.eu
Instagram: https://www.instagram.com/ressona_identitat_digital/

## Serveis

- Identitat visual (logotip, paleta, to)
- Fotografia i vídeo per a press kit
- Web sincronitzada (aparador, eina, agenda)
- Xarxes automàtiques i estratègia de xarxes
- Press kit digital
- IA amb criteri
- Alta a cercadors i IA (Google, Bing, Perplexity, ChatGPT)
- Cartelleria i materials impresos

## Per a qui

Músics, actors, ballarins, circ i escena, arts plàstiques, 
creadors emergents.

## Com treballem

5 passos: escoltem, dissenyem, construïm, acompanyem, monitoritzem.
Auditem l'estat inicial i mesurem l'impacte al final.
```

### Puntuació per plataforma IA

| Plataforma | Score | Principal gap |
|---|---|---|
| Google AI Overviews | 35/100 | Sense FAQPage schema, passatges massa curts |
| ChatGPT (GPT-4o search) | 22/100 | Sense YouTube, sense Wikipedia, sense llms.txt |
| Perplexity | 42/100 | SSR correcte, bots permesos, però contingut no citable |
| Bing Copilot | 38/100 | OG + JSON-LD presents, contingut prim |

### Robots.txt recomanat

```
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Googlebot-Extended
Allow: /

User-agent: CCBot
Disallow: /

User-agent: *
Allow: /
Disallow: /admin/

Sitemap: https://ressona.eu/sitemap.xml
```

---

## 6. SXO — Search Experience Optimization — 41/100

### FINDING CRÍTIC: Page-Type Mismatch en 3 de 5 keywords objectiu

| Keyword | Intent | Match pàgina actual | Severitat |
|---|---|---|---|
| "identitat digital artistes" | Informacional | Pàgina comercial | CRÍTIC |
| "assessoria digital artistes" | Comercial investigació | Landing page ✓ | MITJÀ |
| "digital identity for artists" (EN) | Informacional global | Pàgina CA/EN sense blog | CRÍTIC |
| "presència digital músics" | Informacional | Pàgina comercial | CRÍTIC |
| "web per a artistes Barcelona" | Local comercial | Sense "Barcelona", sense GBP | CRÍTIC |

### Scoring per Persona

| Persona | Query | Score |
|---|---|---|
| Artista emergent (awareness) | "com tenir presència digital com a artista" | 43/100 |
| Músic professional (consideration) | "agència identitat digital músics Barcelona" | 59/100 |
| Actor de teatre (consideration) | "press kit digital actor" | 40/100 |
| Professora de dansa (decision) | "web per a escola de dansa" | 31/100 |

### Arquitectura recomanada (SOLL)

```
ressona.eu/
├── /                              ← CA homepage (revisar + Barcelona + trust)
├── /en/
├── /serveis/
│   ├── press-kit-digital/         ← "press kit digital actor/músic"
│   ├── web-artistes-barcelona/    ← "web per a artistes Barcelona"
│   ├── identitat-visual-artistes/ ← "identitat visual artista"
│   └── estrategia-xarxes/
├── /recursos/ (blog)
│   ├── identitat-digital-artista-emergent-barcelona/
│   ├── press-kit-digital-actor-que-ha-de-tenir/
│   └── web-escola-dansa-que-necessita/
├── /qui-som/                      ← E-E-A-T + fundadors nomenats
└── /legal/* (sense canvis)
```

---

## Resum de Fitxers Afectats

| Fitxer | Canvis necessaris |
|---|---|
| `static/robots.txt` | Named AI agent rules |
| `static/llms.txt` | Crear (nou) |
| `static/humans.txt` | Actualitzar camp Twitter |
| `layouts/_default/baseof.html` | JSON-LD, Google Fonts non-blocking, apple-touch-icon, WebSite guard per idioma |
| `layouts/index.html` | Camp "interès" al formulari de contacte |
| `content/_index.md` | Meta description expandida (150 chars) + "Barcelona" |
| `content/en/_index.md` | Meta description EN + contingut diferenciador |
| `i18n/ca.yaml` | Afegir "Barcelona", "assessoria", descripcions servei 50-80p |
| `i18n/en.yaml` | Equivalent EN |
| `content/legal/_index.md` | `_build: { render: never }` |
| `.gitignore` | Afegir `public/` |
| `.github/workflows/deploy.yml` | Step IndexNow al final |
