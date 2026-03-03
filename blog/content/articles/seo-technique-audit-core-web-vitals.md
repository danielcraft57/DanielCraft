---
title: "SEO technique : audit, Core Web Vitals et indexation"
date: 2025-09-26
excerpt: "Audit technique SEO : indexabilité, Core Web Vitals (LCP, FID, CLS), structure des URLs, balisage. Les fondations techniques pour un bon référencement."
type: article
tags: [SEO, technique, Core Web Vitals, audit, performance]
series: seo-serie
series_order: 2
og_image: seo-technique-1200x630.jpg
---

# SEO technique : audit, Core Web Vitals et indexation

Le SEO technique pose les fondations : sans indexation correcte et sans performance, le meilleur contenu ne sera pas bien classé. Ce guide couvre l'audit technique, les Core Web Vitals et les leviers d'optimisation.

<figure>
<img src="../../assets/images/blog/outils-audit.svg" alt="Audit technique SEO et Core Web Vitals" class="schema-inline" width="400" />
<figcaption>L'audit technique identifie les blocages d'indexation et les problemes de performance.</figcaption>
</figure>

---

## 1. Indexabilité

### robots.txt

Vérifie que tes pages stratégiques ne sont pas bloquées. Un `Disallow: /` ou `Disallow: /blog/` empêche Google d'accéder au contenu.

### Sitemap

Un sitemap XML liste tes URLs et aide Google à découvrir tes pages. Soumets-le dans Search Console et mets-le à jour régulièrement.

### Pages orphelines

Les pages sans lien interne ne sont pas toujours découvertes. Assure une navigation cohérente et des liens vers les pages importantes.

---

## 2. Core Web Vitals

Google utilise trois métriques pour évaluer l'expérience utilisateur :

### LCP (Largest Contentful Paint)

Temps de chargement du plus grand élément visible. **Cible : < 2,5 s.**

- Optimiser les images (format, taille, lazy loading)
- Réduire le blocage du rendu (CSS, JS)
- Utiliser un CDN

### FID / INP (Interactivity)

Temps de réponse aux interactions (clic, tap). **Cible : < 100 ms.**

- Réduire le JavaScript long
- Déferrer les scripts non critiques
- Utiliser le lazy loading

### CLS (Cumulative Layout Shift)

Stabilité visuelle : les éléments ne doivent pas bouger pendant le chargement. **Cible : < 0,1.**

- Définir dimensions pour images et vidéos
- Éviter les contenus injectés au-dessus du contenu existant
- Réserver l'espace pour les publicités

---

## 3. Structure des URLs

- **URLs propres** : courts, lisibles, avec des mots-clés pertinents
- **Canonical** : une seule URL par contenu pour éviter le duplicate
- **HTTPS** : obligatoire pour la confiance

---

## 4. Balisage et structure HTML

- Hiérarchie H1, H2, H3 cohérente
- Balises sémantiques (article, section, header)
- Schema.org JSON-LD pour les données structurées

---

## Conclusion

Le SEO technique est la base : indexation, performance et structure. Un audit régulier avec Search Console et PageSpeed Insights permet d'identifier les problèmes et de prioriser les corrections.
