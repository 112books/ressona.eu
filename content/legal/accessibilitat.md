---
translationKey: "accessibility"
title: "Declaració d'accessibilitat"
slug: "accessibilitat"
description: "Declaració d'accessibilitat de ressona.eu: nivell de conformitat WCAG, tecnologies compatibles i procediment de contacte."
---

## Declaració d'accessibilitat

Ressona s'ha compromès a fer el seu lloc web accessible, de conformitat amb les pautes d'accessibilitat de continguts web WCAG 2.1, nivell AA.

Aquesta declaració s'aplica a **ressona.eu**.

---

## Estat de conformitat

El lloc web ressona.eu **és parcialment conforme** amb WCAG 2.1, nivell AA. Parcialment conforme significa que algunes parts del contingut no compleixen plenament la norma d'accessibilitat.

---

## Mesures tècniques implementades

**Navegació i estructura**
- Un únic enllaç "Salta al contingut" al principi de cada pàgina
- Títols jerarquitzats (`h1` → `h2` → `h3`) sense salts
- Navegació principal marcada amb `<nav aria-label="Navegació principal">`
- Punt d'ancoratge `id="main-content"` a totes les pàgines

**Imatges i icones**
- Totes les imatges amb atribut `alt` descriptiu o `alt=""` si són decoratives
- Icones SVG inline amb `aria-hidden="true"` quan són decoratives
- El logotip i les icones funcionals tenen `aria-label` explícit

**Formularis**
- Tots els camps amb `<label>` associat o `aria-label`
- Atributs `autocomplete` per facilitar el compliment automàtic
- Missatges d'error i confirmació llegibles per lectors de pantalla

**Color i contrast**
- Relació de contrast del text principal: ≥ 7:1 (supera WCAG AA)
- Accent daurat (`#fdbf68`) sobre fons fosc (`#34454c`): 7.3:1
- No s'utilitza el color com a única via per transmetre informació

**Animacions i moviment**
- Totes les animacions respecten `prefers-reduced-motion`
- Cap contingut parpelleja més de 3 vegades per segon

**Teclat**
- Tota la navegació és accessible per teclat
- L'ordre de focus és lògic i visible
- Els elements interactius mostren focus visible (`outline`)

**Idioma**
- Atribut `lang` correcte a l'element `<html>` en cada idioma (CA / EN)
- Les pàgines amb canvi d'idioma inline marquen el fragment amb `lang`

**Documents alternatius**
- `sitemap.xml` públic per facilitar la indexació
- `robots.txt` configurat
- `humans.txt` disponible a `/humans.txt`

---

## Contingut no accessible

- Alguns **mapes interactius** en iframe (Leaflet) no són plenament navegables per teclat ni per lectors de pantalla. Es recomana consultar la informació de cada lloc als llistats de text que acompanyen cada mapa.
- Els **vídeos externs** incrustats de tercers (si n'hi ha) podrien no tenir subtítols complets.

---

## Preparació d'aquesta declaració

Aquesta declaració es va preparar el **2 de juliol de 2026** mitjançant una avaluació interna del lloc web.

---

## Contacte i reclamacions

Si trobes una barrera d'accessibilitat en aquest lloc web, posa't en contacte amb nosaltres:

- **Correu:** [hola@ressona.eu](mailto:hola@ressona.eu)
- **Assumpte recomanat:** `Accessibilitat — [descripció del problema]`

Intentem respondre en un termini de 5 dies hàbils.
