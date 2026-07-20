---
title: "SEO technique : un site rapide et lisible par Google"
date: 2024-07-23
excerpt: "Vitesse, mobile, indexation : les bases techniques qui aident (ou freinent) ta visibilite."
type: article
tags: [SEO, technique, Core Web Vitals, audit, performance]
series: seo-serie
series_order: 2
og_image: seo-technique-1200x630.jpg
---

# SEO technique : un site rapide et lisible par Google

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/seo-technique.svg" alt="Schema SEO technique" class="schema-inline" width="640" />
  <figcaption>Crawl, index, vitesse, mobile, HTTPS.</figcaption>
</figure>

Le SEO technique pose les fondations : sans indexation correcte et sans performance, le meilleur contenu ne sera pas bien classé. Ce guide couvre l'audit technique, les Core Web Vitals et les leviers d'optimisation.

## Indexabilité : être visible avant d'être classé

Google ne peut pas classer une page qu'il n'a pas explorée et indexée. L'indexabilité, c'est la première étape.

### robots.txt

Ce fichier indique aux robots ce qu'ils peuvent explorer. Vérifie qu'aucune règle `Disallow` ne bloque tes pages stratégiques. Un `Disallow: /` ou un `Disallow: /blog/` par erreur peut couper tout ton trafic organique.

### Sitemap XML

Le sitemap liste tes URLs importantes et aide Google à les découvrir. Soumets-le dans Search Console, mets-le à jour à chaque publication et exclu les pages sans valeur (filtres, pages de recherche interne).

### Pages orphelines et profondeur de crawl

Une page sans lien interne pointant vers elle risque de ne jamais être découverte. Assure une navigation cohérente, un maillage interne logique et des liens depuis ta page d'accueil vers tes contenus clés. Idéalement, toute page importante est accessible en trois clics depuis l'accueil.

### Balise canonical

Si la même page est accessible via plusieurs URLs (avec/sans www, paramètres UTM, pagination), la balise `<link rel="canonical">` indique la version de référence. Sans elle, Google peut diluer le signal entre des duplicates.

## Core Web Vitals : la vitesse perçue compte

Depuis 2021, Google intègre l'expérience utilisateur dans son algorithme via trois métriques mesurables.

### LCP (Largest Contentful Paint)

Temps de chargement du plus grand élément visible (souvent une image hero ou un titre). **Cible : inférieur à 2,5 secondes.**

Leviers : compresser les images (WebP, AVIF), lazy loading, CDN, réduire le CSS/JS bloquant le rendu, hébergement performant.

### INP (Interaction to Next Paint)

Remplace progressivement le FID. Mesure la réactivité aux clics et interactions. **Cible : inférieur à 200 ms** (100 ms pour l'ancien FID).

Leviers : réduire le JavaScript long, découper les bundles, déferrer les scripts non critiques, éviter les tâches lourdes sur le thread principal.

### CLS (Cumulative Layout Shift)

Stabilité visuelle : les éléments ne doivent pas bouger pendant le chargement. **Cible : inférieur à 0,1.**

Leviers : définir width/height sur images et vidéos, réserver l'espace pour les bannières publicitaires, éviter d'injecter du contenu au-dessus du contenu existant.

Mesure avec PageSpeed Insights, Lighthouse et le rapport Core Web Vitals dans Search Console. Privilégie les données « terrain » (utilisateurs réels) aux tests labo seuls.

## Mobile-first et HTTPS

Google indexe en priorité la version mobile de ton site. Teste sur un vrai smartphone : lisibilité, boutons cliquables, menus fonctionnels. Le responsive design n'est plus une option.

HTTPS est obligatoire. Un site en HTTP affiche « Non sécurisé » dans Chrome et perd en confiance. Redirige tout le trafic HTTP vers HTTPS avec une redirection 301.

## Structure HTML et balisage sémantique

- Un seul **H1** par page, des **H2/H3** hiérarchisés sans sauter de niveau
- Balises sémantiques : `<article>`, `<section>`, `<nav>`, `<header>`
- Attributs `alt` descriptifs sur les images
- Données structurées JSON-LD (Schema.org) pour compléter le HTML

Un code propre aide Google à comprendre la structure, mais aussi les lecteurs utilisant des lecteurs d'écran.

## Audit technique : par où commencer

1. Search Console → Couverture et Core Web Vitals
2. PageSpeed Insights sur tes 5 pages les plus visitées
3. Crawl avec Screaming Frog ou Sitebulb (URLs cassées, redirects en chaîne, titles dupliqués)
4. Vérification manuelle du robots.txt et du sitemap

Priorise les corrections par impact : une page d'accueil lente pèse plus qu'un article de blog secondaire à 4 secondes de LCP.

## Conclusion

Le SEO technique est la base : indexation, performance et structure. Un audit régulier avec Search Console et PageSpeed Insights permet d'identifier les problèmes et de prioriser les corrections. Une fois les fondations solides, complète avec des [données structurées Schema.org](/blog/articles/seo-schema-org-donnees-structurees.html) pour aider Google à interpréter ton contenu.
