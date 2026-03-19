---
title: "GEO technique : indexabilité, HTML et performance"
date: 2024-09-17
excerpt: "robots.txt, balisage sémantique, contenu dans le HTML initial (JS/SSR), vitesse de chargement : ce que les moteurs génératifs doivent voir pour citer ton site."
type: article
tags: [GEO, technique, indexabilité, HTML, performance, SSR, Core Web Vitals]
series: geo-serie
series_order: 4
og_image: geo-technique-1200x630.jpg
---

# GEO technique : indexabilité, HTML et performance

Les moteurs génératifs parcourent le web comme les crawlers classiques. Pour être cité, ton contenu doit être **accessible**, **lisible** et **rapide**. Ce guide détaille les leviers techniques : robots.txt, structure HTML, contenu initial, et performance.

<figure>
<img src="../../assets/images/blog/html-technique.svg" alt="Structure HTML et balisage semantique pour le GEO" class="schema-inline" width="400" />
<figcaption>Le contenu doit etre present dans le HTML initial pour etre indexe.</figcaption>
</figure>

---

## 1. Indexabilité : robots.txt et sitemap

### Ne pas bloquer les crawlers

Un `Disallow: /blog/` ou `Disallow: /` dans ton robots.txt empêche les moteurs génératifs d'accéder à ces pages. Vérifie que les sections stratégiques sont **autorisées** :

```
User-agent: *
Allow: /
Allow: /blog/
Sitemap: https://tondomaine.fr/sitemap.xml
Sitemap: https://tondomaine.fr/blog/sitemap-blog.xml
```

### Sitemap à jour

Un sitemap XML liste tes URLs et aide les crawlers à découvrir ton contenu. Inclus les pages blog, articles, et collections. Les moteurs génératifs s'appuient sur les mêmes mécanismes de découverte que Google.

---

## 2. Contenu dans le HTML initial

### Problème des SPA et du chargement JS

Les applications monopages (React, Vue, Angular) chargent souvent le contenu **après** le JavaScript. Le HTML initial ne contient qu'un `<div id="root"></div>` vide. Les crawlers qui n'exécutent pas le JS ne voient rien.

**Impact GEO** : si ton contenu n'est pas dans le HTML initial, les moteurs génératifs peuvent ne pas le prendre en compte.

### Solutions

- **SSR (Server-Side Rendering)** : le serveur génère le HTML complet. Next.js, Nuxt, SvelteKit rendent le contenu côté serveur.
- **SSG (Static Site Generation)** : pré-génération des pages en HTML au build. Idéal pour un blog.
- **Prérendering** : outil qui génère des snapshots HTML pour les crawlers (ex. Prerender.io).

Pour un blog, le SSG ou le HTML statique est la solution la plus simple et la plus fiable.

### Vérification

Ouvre le code source de ta page (Ctrl+U). Le contenu principal doit apparaître dans le HTML, pas seulement dans des balises `<script>` ou des divs vides.

---

## 3. Balisage sémantique

### Structure HTML

Utilise une hiérarchie claire :

- Une seule `<h1>` par page
- Des `<h2>` pour les sections principales
- Des `<h3>` pour les sous-sections
- Balises sémantiques : `<article>`, `<section>`, `<header>`, `<main>`

### Schema.org JSON-LD

Les moteurs génératifs exploitent les données structurées. Ajoute du JSON-LD :

- **Article** / **BlogPosting** : titre, auteur, date, description
- **FAQPage** : pour les blocs question-réponse
- **HowTo** : pour les tutoriels étape par étape
- **BreadcrumbList** : fil d'Ariane

Exemple minimal :

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "Titre",
  "author": {"@type": "Person", "name": "Ton nom"},
  "datePublished": "2026-02-21"
}
```

---

## 4. Performance et Core Web Vitals

### Vitesse de chargement

Les crawlers ont des limites de ressources. Un site lent peut être moins bien exploré. Optimise :

- **LCP (Largest Contentful Paint)** : < 2,5 s
- **FID / INP (Interactivity)** : < 100 ms
- **CLS (Cumulative Layout Shift)** : < 0,1

### Bonnes pratiques

- Compresse les assets (Gzip, Brotli)
- Utilise le lazy loading pour les images non critiques
- Minifie CSS et JS
- Mets en cache les pages statiques

---

## 5. URLs et canoniques

- **URLs propres** : évite les paramètres inutiles, utilise des slugs lisibles
- **Canonical** : une seule URL par contenu, avec `<link rel="canonical">` pour éviter le duplicate
- **HTTPS** : obligatoire pour la confiance et le référencement

---

## Conclusion

La base technique du GEO : indexabilité, contenu dans le HTML initial, balisage sémantique et performance. Sans ces fondations, les optimisations de contenu ne suffiront pas. Vérifie ton robots.txt, ton sitemap et le code source de tes pages avant d'affiner ta stratégie.
