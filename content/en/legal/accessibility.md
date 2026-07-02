---
translationKey: "accessibility"
title: "Accessibility statement"
slug: "accessibility"
description: "Accessibility statement for ressona.eu: WCAG conformance level, supported technologies, and contact procedure."
---

## Accessibility statement

Ressona is committed to making its website accessible, in accordance with the Web Content Accessibility Guidelines WCAG 2.1, level AA.

This statement applies to **ressona.eu**.

---

## Conformance status

ressona.eu is **partially conformant** with WCAG 2.1, level AA. Partially conformant means that some parts of the content do not fully conform to the accessibility standard.

---

## Technical measures implemented

**Navigation and structure**
- A single "Skip to content" link at the top of every page
- Hierarchical headings (`h1` → `h2` → `h3`) without gaps
- Main navigation marked with `<nav aria-label="Main navigation">`
- `id="main-content"` anchor on all pages

**Images and icons**
- All images with descriptive `alt` attribute or `alt=""` if decorative
- Inline SVG icons with `aria-hidden="true"` when decorative
- Logo and functional icons have explicit `aria-label`

**Forms**
- All fields with associated `<label>` or `aria-label`
- `autocomplete` attributes to facilitate auto-completion
- Error and confirmation messages readable by screen readers

**Colour and contrast**
- Main text contrast ratio: ≥ 7:1 (exceeds WCAG AA)
- Gold accent (`#fdbf68`) on dark background (`#34454c`): 7.3:1
- Colour is not the sole means of conveying information

**Animations and motion**
- All animations respect `prefers-reduced-motion`
- No content flashes more than 3 times per second

**Keyboard**
- All navigation is keyboard accessible
- Focus order is logical and visible
- Interactive elements show visible focus (`outline`)

**Language**
- Correct `lang` attribute on `<html>` in each language (CA / EN)
- Pages with inline language changes mark the fragment with `lang`

**Alternative documents**
- Public `sitemap.xml` to facilitate indexing
- `robots.txt` configured
- `humans.txt` available at `/humans.txt`

---

## Non-accessible content

- Some **interactive maps** in iframe (Leaflet) are not fully navigable by keyboard or screen readers. We recommend consulting the text listings that accompany each map.
- **Embedded third-party videos** (if any) may not have complete captions.

---

## Preparation of this statement

This statement was prepared on **2 July 2026** through an internal evaluation of the website.

---

## Contact and complaints

If you encounter an accessibility barrier on this website, please contact us:

- **Email:** [hola@ressona.eu](mailto:hola@ressona.eu)
- **Suggested subject:** `Accessibility — [description of the problem]`

We aim to respond within 5 business days.
