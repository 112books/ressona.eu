---
title: "Distribuir la teva música sense plataformes: sobirania total"
description: "Web propi, descàrregues directes, RSS, Faircamp, Funkwhale. Com publicar música sense donar ni un cèntim a les grans plataformes i conservant el control de tot."
translationKey: "blog-diy-music-distribution"
type: recursos
date: 2026-06-30
draft: true
author: "Ressona"
tags: ["eines-digitals", "musics", "distribucio"]
---

Hi ha artistes que no volen donar ni un cèntim a Spotify, Apple ni Amazon. Ni per principi ni per estratègia. Volen que els seus fans puguin accedir a la música directament, sense intermediaris, sense algorismes, sense rastres de dades que van a parar a una corporació.

És possible. Requereix una mica més d'esforç inicial, però el control que guanyes és total.

## El principi base: el teu web com a punt de distribució

Si tens un web propi amb el teu domini, ja tens el 90% de la infraestructura que necessites per distribuir música de forma autònoma. Un fitxer MP3 o FLAC penjat al teu servidor és, tècnicament, distribució directa.

El que cal afegir per sobre d'això és:

- **Una pàgina per a cada llançament** amb informació, portada i el botó de descàrrega o reproducció
- **Un sistema de pagament optatiu** si vols cobrar (Stripe, Ko-fi, o simplement un número de compte)
- **Una llista de correu** per avisar els fans quan surt música nova

Amb aquests tres elements tens una infraestructura de distribució independent completa.

## Faircamp: el Bandcamp lliure

[Faircamp](https://codeberg.org/simonrepp/faircamp) és un generador de llocs estàtics per a músics — en essència, el que hauria de ser Bandcamp si fos programari lliure. L'has d'allotjar tu (o algú que t'ho configuri), però un cop en marxa funciona sol.

**Què fa Faircamp:**
- Genera automàticament una web per als teus llançaments a partir d'una estructura de carpetes
- Suporta descàrregues en múltiples formats (MP3, FLAC, OGG, OPUS)
- Permet venda amb codis de cupó i control d'accés per contrasenya
- Funciona sense base de dades ni PHP — és HTML pur
- Suporta múltiples artistes o labels

**Qui el finança:** el programa NGI0 Entrust de la Comissió Europea, a través de NLnet. No hi ha empresa amb accionistes darrere. La versió 1.0 es va publicar el 2024.

**Requeriment:** un allotjament web (qualsevol servidor bàsic serveix) i algú que et configuri el sistema inicialment. Després, afegir música és tan senzill com copiar carpetes.

## Funkwhale: la ràdio federada

[Funkwhale](https://funkwhale.audio/) és una plataforma de streaming federada i codi obert, part del Fediverse (el mateix ecosistema que Mastodon i Pixelfed). Funciona com Spotify però sense empresa, sense algorismes i sense dades que van a parar a ningú.

**Opcions d'ús:**
- **Instància pròpia**: tu allotges la teva Funkwhale, tu controles tot. Requereix un servidor i coneixements tècnics (o algú que t'ho faci).
- **Instàncies de comunitat**: pots unir-te a una instància existent gestionada per una comunitat sense necessitat d'allotjar res. Les instàncies es federin entre elles.

**Per a qui:** labels independents, col·lectius musicals, artistes amb vocació de comunitat. No és una plataforma de descoberta massiva — és una eina per a una audiència que ja t'estima i que prefereix alternatives federades.

## RSS: la distribució invisible

El protocol RSS és el sistema de subscripció més antic i robust d'internet. L'usen els podcasts. I la música és, tècnicament, àudio — que és exactament el que pot distribuir RSS.

Si publiques la teva música amb un feed RSS (qualsevol web pot generar-ne un), els teus fans poden subscriure's amb qualsevol aplicació de podcasts (Pocket Casts, AntennaPod, Overcast) i rebre cada nou llançament automàticament, sense cap plataforma intermediària.

Algunes aplicacions de podcasts permeten fins i tot descarregar els episodis automàticament. Fet: és exactament el que fan molts artistes de música experimental i netlabel.

**Com implementar-ho:** qualsevol web Hugo, WordPress o similar genera feeds RSS automàticament. Si publiques les teves cançons com a entrades de blog amb el fitxer d'àudio adjunt, tens un feed de música funcional.

## Descàrrega directa amb pagament voluntari

El model "paga el que vulguis" que va popularitzar Bandcamp no és propietat de Bandcamp. Pots implementar-lo al teu web amb eines senzilles:

- **Ko-fi**: plataforma de suport directe. Permet "comprar" un àlbum i rebre el fitxer com a descàrrega. Ko-fi cobra el 0% si uses Stripe directament (Stripe cobra la seva comissió estàndard ~1,4% + 0,25€).
- **Stripe Payment Links**: genera un enllaç de pagament per a un producte (el teu àlbum) i envia el fitxer per email un cop completada la transacció.
- **Gumroad**: plataforma de venda de productes digitals. Cobra el 10% per transacció però és molt senzilla d'usar.
- **Descàrrega gratuïta directa**: simplement un enllaç a un fitxer ZIP al teu servidor. Sense barrera, sense intermediari, sense comissió.

## La llista de correu com a canal de distribució

La llista de correu és el canal de distribució directa més infravalorat que existeix. Un email als teus subscriptors amb un enllaç de descàrrega és distribució. Sense algorisme que decideixi si el reben. Sense plataforma que es quedi un percentatge. Sense dades que vagin a parar a cap tercer.

Eines ètiques per a llistes de correu:
- **Brevo** (abans Sendinblue): pla gratuït fins a 300 emails/dia. Empresa francesa.
- **Mailchimp**: el més conegut, americà, fins a 500 contactes gratuït.
- **Listmonk**: programari lliure i auto-allotjable. Zero comissions, zero dades a tercers.

## Peertube per als vídeos musicals

Si vols publicar videoclips o enregistraments en directe sense YouTube, [Peertube](https://joinpeertube.org/) és l'alternativa federada i lliure. Com Funkwhale, pots unir-te a una instància de comunitat o allotjar la teva pròpia.

Els vídeos de Peertube es fedieren — algú d'una instància diferent pot seguir i veure els teus vídeos sense compte propi.

## Resum pràctic

| Necessitat | Eina lliure | Dificultat |
|---|---|---|
| Publicar música amb descàrrega | Faircamp (auto-allotjat) | Mitjana |
| Streaming propi federat | Funkwhale (instància pròpia o comunitat) | Mitjana-alta |
| Distribució per subscripció | Feed RSS del teu web | Baixa |
| Venda directa de música | Ko-fi + fitxer ZIP | Baixa |
| Avisar fans de nous llançaments | Llista de correu | Baixa |
| Vídeos sense YouTube | Peertube | Mitjana |

## La veritat sobre el "sense plataformes"

Distribuir música de forma completament independent et dona control total i zero comissions. El que no et dona és descoberta passiva: ningú et trobarà per algorismes perquè no n'hi ha. La teva música arribarà exactament a qui tu hi arribes activament — ni un fan més, ni un fan menys.

Per als artistes que ja tenen un públic consolidat i un canal de comunicació directa (llista de correu, xarxes amb abast orgànic real), la distribució independent és perfectament viable. Per als artistes que estan construint el seu públic, les plataformes continuen sent útils com a canals de descoberta, encara que sigui de manera selectiva.

La solució no és una o l'altra: és saber quina plataforma uses per descoberta i quina infraestructura pròpia uses per a la relació directa amb el teu públic.

A Ressona ajudem artistes a construir aquesta infraestructura pròpia: web, domini, llista de correu i eines de distribució que no depenen de cap empresa aliena. [Parla amb nosaltres](/#contacte).
