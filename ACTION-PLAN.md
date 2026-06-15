# Pla d'Acció SEO — ressona.eu
**Data:** 2026-06-15 · Puntuació actual: 49/100 · Objectiu 3 mesos: 72/100

---

## CRÍTIC — Implementar immediatament

### C1 — `public/` al `.gitignore` [2 min]
```bash
echo "public/" >> .gitignore
git rm -r --cached public/
git commit -m "chore: remove dev build artifact from repo"
```
**Per què:** El `public/` commitejat conté localhost URLs. Si mai es deploya manualment, el site desapareix de Google.

### C2 — Meta description expandida [20 min]
Editar `content/_index.md` — afegir o modificar camp `description`:
```yaml
description: "Ressona acompanya músics, actors, balladors i artistes a construir la seva identitat digital a Barcelona: web, identitat visual, press kit i xarxes socials."
```
Equivalent EN a `content/en/_index.md`:
```yaml
description: "Ressona helps musicians, actors, dancers and artists build their digital identity in Barcelona: website, visual branding, digital press kit and social strategy."
```
**Per què:** Actual = 34 chars (tagline). Google la reescriu de forma descontrolada.

### C3 — "Barcelona" al contingut visible [10 min]
Editar `i18n/ca.yaml` — modificar `hero_desc`:
```yaml
hero_desc: "Acompanyem creadors de Barcelona a construir la seva presència digital"
```
O afegir-la al hero section en `layouts/index.html`.
**Per què:** "Barcelona" no existeix al site. Invisible per a tota cerca local.

### C4 — Logo PNG al schema [5 min]
Editar `layouts/_default/baseof.html` — canviar:
```json
"logo": "https://ressona.eu/img/ressona-logo.svg"
```
Per:
```json
"logo": {
  "@type": "ImageObject",
  "url": "https://ressona.eu/img/ressona-eu-rounded.png",
  "width": 874,
  "height": 874
}
```
**Per què:** Google Knowledge Panel requereix PNG/JPG per al logo d'Organization.

### C5 — Crear `static/llms.txt` [30 min]
Veure plantilla a FULL-AUDIT-REPORT.md §5.
**Per què:** Gap d'impacte més alt per a visibilitat en ChatGPT, Perplexity i Claude.

---

## ALT — Implementar aquesta setmana

### A1 — Google Fonts non-blocking [15 min]
Editar `layouts/_default/baseof.html` — substituir la línia de `<link rel="stylesheet" href="fonts.googleapis.com...">` per:
```html
<link rel="preload" as="style"
  href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500&family=Syne:wght@700;800&display=swap"
  onload="this.onload=null;this.rel='stylesheet'">
<noscript>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500&family=Syne:wght@700;800&display=swap">
</noscript>
```
**Per què:** Principal causa del LCP lent en mobile. Estalvi estimat 400-900ms.

### A2 — Actualitzar JSON-LD complet [45 min]
Substituir els dos blocs JSON-LD a `layouts/_default/baseof.html` amb els blocs millorats de FULL-AUDIT-REPORT.md §3. Canvis clau:
- Afegir `@id` als dos blocs (els vincula)
- Afegir `ProfessionalService` al type d'Organization
- Afegir `address` (Barcelona), `areaServed`, `knowsLanguage`
- Afegir `hasOfferCatalog` amb els 9 serveis
- Canviar `contactType` a `"sales"`
- Guardar `WebSite` schema únicament per a `{{ if and .IsHome (eq .Language.Lang "ca") }}`

### A3 — Actualitzar `static/robots.txt` [15 min]
Veure robots.txt recomanat a FULL-AUDIT-REPORT.md §5. Afegir regles named-agent per a GPTBot, ClaudeBot, PerplexityBot, etc.

### A4 — Expandir descripcions de servei [2h]
Editar `i18n/ca.yaml` i `i18n/en.yaml`. Cada servei: de 8-12 paraules → 50-80 paraules. Incloure: què és, quin és el lliurament, per a qui és específicament.
Afegir la paraula "assessoria" com a mínim 2-3 vegades al body copy.

### A5 — Hero tagline visible per defecte [30 min]
Editar `assets/css/main.css` — eliminar `visibility: hidden` del `.hero-tagline` per defecte. Fer que el JS de l'efecte typing sigui additiu (aplica cursor i animació, però no buida el text). Mantenir el `<noscript>` com a capa addicional.

### A6 — `apple-touch-icon` + GoatCounter HTTPS [5 min]
A `layouts/_default/baseof.html`:
```html
<link rel="apple-touch-icon" href="/img/ressona-eu-rounded-192.png">
```
I canviar `//gc.zgo.at/count.js` → `https://gc.zgo.at/count.js`.

---

## MITJÀ — Implementar aquest mes

### M1 — Secció "Qui som" a la homepage [2h]
Afegir entre la secció de processos i el formulari de contacte. Contingut mínim:
- Noms dels fundadors / l'equip (Joan + Pocallum + LinuxBCN)
- Localització: Barcelona
- 80-100 paraules sobre l'origen del projecte
**Per què:** Impacte directe sobre E-E-A-T Experience + Authoritativeness. Google QRG (set. 2025) exigeix identificabilitat.

### M2 — Un element de prova social [1h]
Afegir a la homepage:
- Un testimoni real (amb permís) o parafrasejat ("Artista emergent, Barcelona, 2025")
- O una frase de volum: "Hem acompanyat X artistes"
**Per què:** Persona B (músic professional) no converteix sense prova social. És el principal bloqueig de conversió.

### M3 — Camp "interès" al formulari [15 min]
Editar `layouts/index.html` — afegir `<select>` al formulari:
```html
<select name="servei">
  <option value="">Quin servei t'interessa?</option>
  <option>Identitat visual</option>
  <option>Web</option>
  <option>Press kit digital</option>
  <option>Xarxes socials</option>
  <option>Paquet complet</option>
  <option>No ho sé encara</option>
</select>
```
**Per què:** Segmentació de leads des del primer contacte.

### M4 — Suprimir `/legal/` section index [15 min]
Crear `content/legal/_index.md` amb:
```yaml
---
_build:
  render: never
---
```
**Per què:** Genera una URL prima que pot ser flagada com a thin content.

### M5 — IndexNow al deploy workflow [30 min]
Afegir a `.github/workflows/deploy.yml` un step final que pinga `api.indexnow.org` amb les URLs principals. Genera clau: `openssl rand -hex 16`. Guarda com a secret `INDEXNOW_KEY`.
**Per què:** Bing indexa els canvis en minuts en lloc de dies.

### M6 — Verificar sitemap en producció [5 min]
```bash
curl -s https://ressona.eu/sitemap.xml | head -20
```
Confirmar que les `<loc>` mostren `https://ressona.eu/` i no `http://localhost`.

### M7 — Suprimir SVG decorativa [5 min]
Al primer element `.service--icon-only` (la icona d'ull):
```html
aria-hidden="true"
```
Eliminar `role="img"` i `aria-label="Ressona"`.

---

## BAIX — Backlog

### B1 — `translationKey` a pàgines legals
Afegir `translationKey: avis-legal` (i equivalents) al front matter de cada pàgina legal per generar hreflang al sitemap.

### B2 — Cloudflare davant de GitHub Pages
Mou DNS a Cloudflare (gratuït). Guanys:
- Security headers (X-Frame-Options, X-Content-Type-Options, Referrer-Policy)
- Redirect www → apex automàtic
- CDN edge caching
- Analytics de seguretat Lighthouse

### B3 — `humans.txt` actualitzar
Eliminar o actualitzar camp `Twitter: @linuxbcn` (no és el handle de Ressona).

### B4 — `_headers` file si es migra a Cloudflare Pages
```
/*
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=()
```

---

## ESTRATÈGIC — Horitzó 3-6 mesos

### E1 — Crear pàgines de servei dedicades (màxim impacte SEO)
Prioritat per ordre de tràfic potencial:
1. `/serveis/press-kit-digital/` — "press kit digital actor", "press kit artista"
2. `/serveis/web-artistes-barcelona/` — "web per a artistes Barcelona", "disseny web músic"
3. `/serveis/identitat-visual-artistes/` — "identitat visual artista", "logo artista"

Format de cada pàgina: 600-900 paraules, exemple visual (mockup), rang de preus, 3-5 FAQs amb `FAQPage` schema, CTA.

### E2 — Blog `/recursos/` (3 articles inicials)
1. "Com construir la identitat digital com a artista emergent a Barcelona"
2. "Què ha de tenir un press kit digital d'actor el 2026"
3. "Les 7 coses que necessita el web d'una escola de dansa"

Cada article: 1.000-1.500 paraules, link intern a la pàgina de servei corresponent.

### E3 — Perfil Google Business
Crear i verificar Google Business Profile per a Ressona.
**Per què:** Condició necessària per aparèixer al "3-pack" local de Google per a cerques com "web per a artistes Barcelona" o "assessoria digital artistes".

### E4 — Canal YouTube (correlació 0.737 amb citació a ChatGPT)
3-5 vídeos de 60-90 segons:
- "Què és la identitat digital per a artistes?"
- "Quin hauria de tenir un press kit digital d'actor"
- "Com funciona l'alta a cercadors per a músics"

Afegir URL del canal a `sameAs` del schema Organization.

### E5 — Wikidata entity
Crear entrada Wikidata per a Ressona (organització, sector: consultoria identitat digital, lloc: Barcelona). Afegir URL de Wikidata a `sameAs`. Dóna resolució d'entitat de qualitat Wikipedia a tots els grafs de coneixement IA.

---

## Taula Resum de Prioritats

| # | Acció | Temps | Impacte | Arxiu |
|---|---|---|---|---|
| C1 | `public/` al .gitignore | 2 min | CRÍTIC | `.gitignore` |
| C2 | Meta description 150 chars | 20 min | CRÍTIC | `content/_index.md` |
| C3 | "Barcelona" al hero_desc | 10 min | CRÍTIC | `i18n/ca.yaml` |
| C4 | Logo PNG al schema | 5 min | CRÍTIC | `baseof.html` |
| C5 | Crear `llms.txt` | 30 min | CRÍTIC | `static/llms.txt` |
| A1 | Google Fonts non-blocking | 15 min | ALT (LCP) | `baseof.html` |
| A2 | JSON-LD complet millorat | 45 min | ALT | `baseof.html` |
| A3 | `robots.txt` named agents | 15 min | ALT | `static/robots.txt` |
| A4 | Descripcions servei 50-80p | 2h | ALT | `i18n/ca.yaml` |
| A5 | Hero tagline visible per defecte | 30 min | ALT | `main.css` + JS |
| A6 | apple-touch-icon + GoatCounter https | 5 min | ALT | `baseof.html` |
| M1 | Secció "Qui som" | 2h | MITJÀ | `layouts/index.html` |
| M2 | Prova social (testimoni) | 1h | MITJÀ | `i18n/ca.yaml` |
| M3 | Camp interès formulari | 15 min | MITJÀ | `layouts/index.html` |
| M4 | Suprimir `/legal/` index | 15 min | MITJÀ | `content/legal/_index.md` |
| M5 | IndexNow al workflow | 30 min | MITJÀ | `.github/workflows/deploy.yml` |
| M6 | Verificar sitemap prod | 5 min | MITJÀ | (verificació) |
| M7 | SVG decorativa aria-hidden | 5 min | BAIX | `layouts/index.html` |
| B1 | `translationKey` legals | 20 min | BAIX | legal front matter |
| B2 | Cloudflare DNS | 1-2h | BAIX-MITJÀ | Infraestructura |
| E1 | Pàgines de servei | 1-2 setmanes | ALT | Nous layouts |
| E2 | Blog 3 articles | 2-3 setmanes | ALT | Nous continguts |
| E3 | Google Business Profile | 30 min + verif | CRÍTIC (local) | Externa |
| E4 | Canal YouTube | 1-4 setmanes | ALT (IA) | Externa |
| E5 | Wikidata entity | 1h | MITJÀ (IA) | Externa |
