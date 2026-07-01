# Spec: EPK Hub — Contingut educatiu + actualització de servei

**Data:** 2026-06-26  
**Estat:** Aprovat

---

## Objectiu

Crear contingut que posicioni Ressona orgànicament per a búsquedes com "que és un EPK", "epk músics", "press kit digital" — tant a cercadors com a IAs — amb l'objectiu final que l'usuari contacti Ressona per crear el seu EPK.

---

## Lliurables

### 1. Article hub: `content/recursos/que-es-un-epk.md`

**URL:** `ressona.eu/recursos/que-es-un-epk/`  
**Versió EN:** `content/en/resources/what-is-an-epk.md`  
**translationKey:** `blog-what-is-epk`

**Metadades:**
- `title`: "Que és un EPK (i per a que el necessites si ets artista)"
- `description`: ~155 caràcters, inclou "EPK", "press kit digital", "artistes"
- `date`: 2026-06-26
- `author`: "Ressona"
- `type`: recursos

**Estructura de l'article (Catalan):**

1. **Obertura** — escena real: programador busca un artista, no troba informació clara, passa al següent. Una frase, directa.
2. **Tres noms, un concepte** — EPK / press kit digital / dossier de premsa: el mateix. Sense condescendència. Aclarir que EPK és el terme anglès habitual al sector musical internacional.
3. **L'evolució en 30 anys** — carpeta física (anys 90) → PDF per email (2000s) → pàgina web viva (avui). Breu, cronològic.
4. **Per a que serveix exactament** — qui l'obre i per quin motiu: programadors de festivals, periodistes, càstings, sales de concert. Concret.
5. **Els 5 elements imprescindibles** — llista curta, genèrica per a tots els perfils artístics:
   - Fotografies en alta resolució
   - Bio en dos formats (curta i llarga)
   - Vídeo o àudio recent en streaming
   - Contacte directe (email, no formulari genèric)
   - URL pròpia fàcil de recordar i compartir
6. **L'error més comú** — tenir-lo desactualitzat (o no tenir-lo). Una frase contundent.
7. **CTA** — "Si vols que te'l construïm o revisem el que ja tens, [explica'ns el teu projecte](/#contacte)."
   - Link intern als articles de perfil: actors (`/recursos/press-kit-digital-actors/`) i futurs (músics, dansa)

**To:** mateix registre que els articles existents — directe, professional, sense floritures. Segona persona singular. Frases curtes.

**Longitud aproximada:** 500-650 paraules. No és una guia exhaustiva; és la porta d'entrada.

---

### 2. Actualització: `content/serveis/press-kit-digital.md`

**Canvis al frontmatter:**

Afegir camp `intro` amb el text:

> EPK, press kit digital, dossier de premsa: tres noms per al mateix document. El que ha canviat és el format: ja no és una carpeta, ni un PDF. És una pàgina web que sempre mostra la versió actual.

**Canvis a les FAQs:**

Afegir una nova FAQ (primera de la llista, per prioritat):

```yaml
- q: "He sentit parlar d'\"EPK\". És diferent d'un press kit digital?"
  a: "No. EPK (Electronic Press Kit) és el terme anglès, habitual al sector musical internacional. Press kit digital és com s'usa en català i castellà. El concepte és idèntic: un espai web amb tota la informació professional de l'artista, accessible en un sol clic. [Llegeix la guia completa sobre EPK →](/recursos/que-es-un-epk/)"
```

**Versió EN:** `content/en/services/digital-press-kit.md` — canvis equivalents en anglès.

---

## Layout

Cal verificar que el layout `layouts/serveis/single.html` renderitza el camp `intro` del frontmatter. Si no existeix, afegir-lo com a primer bloc de contingut, abans de `.Params.challenge`.

---

## Fora d'abast

- Articles de perfil específics per a músics, dansa, circ — vindran en iteracions posteriors
- Versió imprimible o PDF de l'article
- Canvis al layout de recursos (`layouts/recursos/single.html`)

---

## Criteri d'èxit

- L'article apareix indexat a Google per "que és un EPK" i termes relacionats
- La pàgina de servei té la FAQ "EPK vs press kit digital" visible
- El CTA de l'article apunta a `/#contacte`
- Internal linking bidireccional: article hub ↔ pàgina de servei ↔ articles de perfil
