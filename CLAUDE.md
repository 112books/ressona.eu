# Ressona — Identitat digital per a artistes

## Concepte
Ressona és una marca d'assessoria i acompanyament en identitat digital per a artistes. Neix de la combinació de **Pocallum** (fotografia, identitat visual) i **LinuxBCN** (tecnologia, infraestructura, automatització).

El nom prové de *ressonar*: fer eco, vibrar. La identitat digital d'un artista ha de ressonar amb el seu públic.

## Públic
Músics, bandes, actors/actrius, circ, arts escèniques, ballarins/coreògrafs, artistes plàstics, creadors emergents.

## To misteriós i intrigant
- No ho expliquem tot. Deixem espais perquè l'usuari descobreixi.
- Els textos suggereixen més que no diuen. Poetry, no prosa.
- Cada secció revela una mica més, però mai del tot.
- El que no es veu és tan important com el que es veu (espai negatiu, silencis).
- El disseny convida a scrollejar per descobrir, no explica res a la primera.
- La pàgina és com un disc de jazz: cada visitant hi troba alguna cosa diferent.

## ADN de disseny
Tres influències que es fonen:

### Escola Suïssa (International Typographic Style)
- Graelles asimètriques com a base estructural
- Jerarquia tipogràfica clara i dramàtica
- Composició amb espais negatius generosos
- Sense decoració innecessària — cada element té una funció
- Asimetria controlada, mai centrat simètric excepte l'hero

### Bauhaus
- Blocs de color sòlid com a elements estructurals de pàgina
- Formes geomètriques bàsiques (quadrat, cercle, línia, triangle)
- Colors primaris amb intenció: roig, or, blau
- "La forma segueix la funció" — cada bloc de color defineix una zona
- Tensions visuals entre elements: gran vs petit, ple vs buit

### Jazz modern i contemporani
- Calidesa en la paleta (negre no pur, blanc trencat)
- Ritme visual alternat (seccions que respiren)
- Sofisticació sense pretensió — estètica ECM Records
- Contrastos suaus, mai agressius
- L'espai entre elements és tan important com els elements mateixos

## Paleta de colors (curta amb caràcter)

| Color | Hex | Ús | Influència |
|-------|-----|-----|------------|
| Negre càlid | `#0c0b09` | Fons principal | Jazz: negre no pur |
| Ivori | `#ece4d9` | Text i fons alternatiu | Suïssa: llegibilitat |
| Roig Bauhaus | `#c1121f` | Accent principal, CTAs, blocs | Bauhaus: primari |
| Or càlid | `#d49a2a` | Accent secundari, subtileses | Jazz: calidesa |
| Blau profund | `#1e5084` | Accent fred, equilibri | Bauhaus: primari |

## Tipografia
- **Syne** (700, 800): titulacions, marca, números enormes. Variable font weight.
- **Inter** (300, 400, 500): cos de text, navegació, labels.
- Mida base: 18px. Títols: clamp(2.2rem, 4vw, 3.8rem).
- Marca a l'hero: clamp(6rem, 18vw, 14rem) amb gradient càlid.
- Molt pes visual de la lletra — la tipografia és la decoració principal.

## Navegació
- 4 ítems al header: icona SVG + micro-label textual
- Icones inline, minimalistes, stroke 1.5px
- Smooth scroll a seccions
- No hi ha "Inici" — la marca fa de home
- Switcher d'idioma: text sol (`CA` / `EN`), mai banderetes
- A mòbil: nav es condensa o passa a bottom tab

## Iconografia (SVG inline)
Totes les icones són SVG inline, traç simple, sense llibreries externes:
- **Estrella**: Què fem
- **Persones**: Per a qui
- **Rellotge/ones**: Com treballem
- **Sobre**: Contacte
- **Serveis**: ull (identitat), càmera (foto), globus (web), xarxa (socials), cervell (IA), carpeta (press kit)
- **Públic**: nota musical, màscara, tenda circ, ballarí, paleta, planter

## Estructura del site (single page)

### Hero
- Fons negre càlid amb ona jazz subtilíssima (opacity 0.03)
- Marca "Ressona" massiva amb gradient (blanc → or → roig)
- Tagline en letter-spacing ampli
- Descripció curta
- No CTA — la pàgina convida a scrollejar

### Què fem (6 serveis)
- Graella asimètrica 4+2 o 3+3 amb pesos diferents
- Cada servei: icona SVG + títol Syne + descripció Inter
- Blocs de color alternats: fons negre, alguns ítems tenen fons de color sòlid
- Línies de separació horitzontals fines

### Per a qui (6 perfils)
- Graella asimètrica a l'estil Swiss
- Mides de cel·la variables (algunes dobles)
- Cada perfil: icona SVG + nom + descripció curta
- Fons de color massís per blocs (roig, or, blau alternats)

### Com treballem (4 passos)
- Números enormes (Syne 800, opacity baixa)
- Disposició vertical o 2x2
- Text a la dreta del número
- Línia fina separant passos

### Contacte
- Bloc massís de color roig Bauhaus
- Text en blanc
- Email destacat + enllaç Instagram
- Sense formulari — l'email és el canal

### Footer
- Minimal
- Marca + tagline
- Instagram + email
- Crèdits: "Disseny gràfic: Pocallum · Tecnologia: LinuxBCN"

## Funcionalitats
- **Multi-idioma**: Català (defecte) + Anglès
- **URLs**: `ressona.eu/` (CA), `ressona.eu/en/` (EN)
- **Switcher d'idioma**: text sol, mai banderetes
- **JavaScript**: zero — site estàtic pur (excepte GoatCounter)
- **Analytics**: GoatCounter (`ressona.goatcounter.com`) + dashboard propi a `/admin/`
- **Responsive**: 27" desktop → tablet → mòbil
- **Hosting**: LinuxBCN (mateix stack que awpcp.org)

## Tecnologia
- **Framework**: Hugo (static site generator)
- **Idiomes**: gestió amb `i18n/` + `content/en/`
- **CSS**: pur, sense frameworks. Minificat amb Hugo pipelines.
- **Fonts**: Google Fonts (Syne + Inter), preconnect
- **Dashboard**: GoatCounter API v0 → scripts/build-analytics-json.py + process-analytics.py → static/admin/analytics.json → static/admin/index.html (Chart.js, SHA-256 auth)

## GoatCounter Analytics
- **Compte**: `ressona.goatcounter.com` (script de tracking a `baseof.html`)
- **Dashboard**: `ressona.eu/admin/` (protegit amb la mateixa contrasenya que el site)
- **Workflow**: `.github/workflows/fetch-analytics.yml` — cada hora, obté dades de l'API GoatCounter i genera `static/admin/analytics.json`
- **Scripts de processament**: `scripts/build-analytics-json.py` + `scripts/process-analytics.py`
- **Secret necessari**: `GOATCOUNTER_TOKEN` — token API amb permisos "Read stats" des de `ressona.goatcounter.com/settings/api`
- **Seccions del dashboard**: `inici` (home) + `legal` (pàgines legals)

## Estructura de fitxers
```
ressona.eu/
├── assets/
│   └── css/
│       └── main.css
├── content/
│   ├── _index.md
│   └── en/
│       └── _index.md
├── i18n/
│   ├── ca.yaml
│   └── en.yaml
├── layouts/
│   ├── _default/
│   │   └── baseof.html
│   ├── partials/
│   │   ├── header.html
│   │   └── footer.html
│   └── index.html
├── scripts/
│   ├── build-analytics-json.py
│   └── process-analytics.py
├── static/
│   ├── admin/
│   │   ├── index.html (dashboard)
│   │   └── analytics.json (generat)
│   ├── img/
│   │   ├── ressona-logo.svg (logotip complet: ꓤessona amb syncopation)
│   │   └── ressona-mark.svg (marca curta: ꓤ)
│   └── favicon.ico
├── .github/
│   └── workflows/
│       ├── deploy.yml
│       └── fetch-analytics.yml
├── hugo.toml
└── CLAUDE.md
```

## Riders online
- Cada artista pot tenir un rider tècnic online (fitxa de contractació)
- Configurable per formació: solo, duo, trio, banda
- Contingut: necessitats tècniques, so, llums, backline, hospitality
- Accés privat (enllaç compartible) o públic
- Part del press kit digital de l'artista

## Estratègia de promoció per perfils
- No revelar les cartes del tot. Mostrar resultats, mai la metodologia completa.
- Cada perfil d'artista (músic, actor, ballarí, circ, etc.) necessita una estratègia de promoció diferent.
- Exemples públics: mostrar el "abans i després" sense detallar el "com".
- Contingut de mostra: press kits, webs, fotos — però sempre amb aigua, mai el fitxer original.
- El site ha de generar curiositat i leads, no resoldre tots els dubtes.
- Estratègies per perfil:
  - **Músics**: presència a Spotify/YouTube + web + agenda sincronitzada + rider online
  - **Actors**: showreel + book digital + presència a càstings online
  - **Circ/escena**: dossier d'espectacle + galeria + calendari de gires
  - **Ballarins**: vídeo + bio + calendari de classes/tallers
  - **Arts plàstiques**: portfolio + galeria + presència a xarxes visuals
  - **Emergents**: paquet básic d'inici — foto + bio + web mínima

## Regles de desenvolupament
1. **Minimalisme radical**: cada element ha de justificar la seva existència
2. **Primer la tipografia**: abans que qualsevol decoració, que el text tingui pes
3. **SVG inline**: icons fetes a mà al HTML, sense llibreries, sense Font Awesome
4. **Idiomes**: mai barrejar CA i EN a la mateixa pàgina. Switcher net.
5. **Cap bandereta**: ni icons de país, ni flags. Només "CA / EN" en text.
6. **Blocs de color**: usar fons de color sòlid com a element de disseny estructural
7. **Zero JS**: tret de GoatCounter. No cal animació DOM, no cal interactivitat.
8. **Asimetria**: evitar simetries perfectes. Buscar tensió visual controlada.
9. **Contingut editorial**: cada text ha de sonar humà, no a template.
10. **Responsive**: pensar primer en 27" desktop, després adaptar.
