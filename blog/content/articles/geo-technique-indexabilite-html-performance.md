---
title: "GEO technique : un HTML que les IA peuvent lire"
date: 2024-09-17
excerpt: "Pages rapides, textes visibles, structure claire : la base technique du GEO."
type: article
tags: [GEO, technique, indexabilité, HTML, performance, SSR, Core Web Vitals]
series: geo-serie
series_order: 4
og_image: geo-technique-1200x630.jpg
---

# GEO technique : un HTML que les IA peuvent lire

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/geo-technique.svg" alt="Schema GEO technique" class="schema-inline" width="640" />
  <figcaption>HTML propre, performance, indexable, structure.</figcaption>
</figure>

Les moteurs génératifs parcourent le web comme les crawlers classiques. Pour être cité, ton contenu doit être **accessible**, **lisible** et **rapide**. Ce guide détaille les leviers techniques : robots.txt, structure HTML, contenu initial, et performance.

Le GEO (Generative Engine Optimization) ne remplace pas le [SEO classique](/blog/articles/seo-fondamentaux-referencement-naturel.html) : il s’appuie sur les mêmes bases techniques, avec une exigence encore plus forte sur le texte réellement présent dans la page. Pour le cadre global, vois aussi [GEO vs SEO](/blog/articles/geo-vs-seo-differences-complementarite.html) et le [guide GEO](/blog/articles/geo-nouveau-seo-ia-guide-complet.html).

---

## 1. Indexabilité : robots.txt et sitemap

### Ne pas bloquer les crawlers

Un `Disallow: /blog/` ou `Disallow: /` dans ton robots.txt empêche les moteurs (et les bots génératifs) d’accéder à ces pages. Vérifie que les sections stratégiques sont **autorisées** :

```
User-agent: *
Allow: /
Allow: /blog/
Sitemap: https://tondomaine.fr/sitemap.xml
Sitemap: https://tondomaine.fr/blog/sitemap-blog.xml
```

### Sitemap à jour

Un sitemap XML liste tes URLs et aide à la découverte. Inclus pages clés, articles, collections. Les IA s’appuient souvent sur les mêmes mécanismes de crawl que Google : si la page n’est pas trouvable, elle ne sera pas citée.

### Checklist indexabilité

- [ ] Pas de `noindex` accidentel sur les pages importantes
- [ ] Sitemap régénéré après chaque publication
- [ ] URLs du sitemap répondent en 200 (pas de 404 / 500)

---

## 2. Contenu dans le HTML initial

### Problème des SPA et du chargement JS

Les apps monopages (React, Vue, Angular) chargent souvent le contenu **après** le JavaScript. Le HTML initial ne contient qu’un `<div id="root"></div>` vide. Un crawler qui n’exécute pas (ou mal) le JS ne voit rien.

**Impact GEO** : si ton texte n’est pas dans le HTML initial, les moteurs génératifs peuvent l’ignorer — même si un humain voit la page « correctement » dans le navigateur.

### Solutions

- **SSR** (Server-Side Rendering) : Next.js, Nuxt, SvelteKit génèrent le HTML côté serveur.
- **SSG** (Static Site Generation) : pages HTML au build — idéal pour un blog.
- **Prérendering** : snapshots HTML pour les crawlers (ex. Prerender.io).

Pour un blog, SSG ou HTML statique reste la solution la plus simple et la plus fiable.

### Vérification

Ouvre le code source (Ctrl+U / Cmd+U). Le titre, l’intro et les sections principales doivent apparaître en clair dans le HTML, pas seulement dans des `<script>` ou des divs vides.

---

## 3. Balisage sémantique

### Structure HTML

Utilise une hiérarchie claire :

- une seule `<h1>` par page ;
- des `<h2>` pour les sections ;
- des `<h3>` pour les sous-parties ;
- balises sémantiques : `<article>`, `<section>`, `<header>`, `<main>`.

Exemple concret : un article « comment choisir un hébergement » avec H2 « Critères », « Budget », « Checklist ». Un modèle d’IA qui résume la page retrouve facilement les blocs — comme un lecteur humain. Pour les formats qui aident au résumé, vois le [contenu GEO et sa structure](/blog/articles/geo-contenu-structure-formats-checklist.html).

### Schema.org JSON-LD

Ajoute des données structurées :

- **BlogPosting** / **Article** : titre, auteur, date, description ;
- **FAQPage** : questions-réponses ;
- **HowTo** : tutoriels étape par étape ;
- **BreadcrumbList** : fil d’Ariane.

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "Titre",
  "author": {"@type": "Person", "name": "Ton nom"},
  "datePublished": "2026-02-21"
}
```

Le détail des schemas utiles côté Google est aussi dans [données structurées Schema.org](/blog/articles/seo-schema-org-donnees-structurees.html).

---

## 4. Performance et Core Web Vitals

Les crawlers ont des budgets de temps et de ressources. Un site lent est moins bien exploré — et une page lente se partage / se cite moins bien.

Cibles utiles :

- **LCP** < 2,5 s
- **INP** < 200 ms (ordre de grandeur « bon »)
- **CLS** < 0,1

### Bonnes pratiques

- compression Gzip / Brotli ;
- lazy loading des images non critiques ;
- CSS/JS minifiés ;
- cache des pages statiques ;
- images au bon format (WebP) et à la bonne taille.

Pour un audit plus large, le guide [SEO technique et Core Web Vitals](/blog/articles/seo-technique-audit-core-web-vitals.html) complète ce chapitre.

### Pièges fréquents

- Hero image de 4 Mo non compressée → LCP catastrophique.
- Polices web bloquantes sans `font-display`.
- Widgets tiers (chat, pubs) qui décalent le layout (CLS).

---

## 5. URLs et canoniques

- **URLs propres** : slugs lisibles, peu de paramètres inutiles.
- **Canonical** : une seule URL « officielle » via `<link rel="canonical">`.
- **HTTPS** : obligatoire pour la confiance et le référencement.

Exemple : `/blog/articles/geo-technique-indexabilite-html-performance.html` plutôt que `/page?id=42&ref=utm`.

---

## 6. Mini-checklist avant de publier

- [ ] robots.txt n’bloque pas la page
- [ ] Contenu visible dans le code source
- [ ] H1 unique + H2 cohérents
- [ ] JSON-LD Article / FAQ si pertinent
- [ ] LCP / CLS acceptables sur mobile
- [ ] Canonical + HTTPS OK

---

## Conclusion

La base technique du GEO : indexabilité, contenu dans le HTML initial, balisage sémantique et performance. Sans ces fondations, peaufiner le style ou les prompts ne suffira pas. Vérifie robots.txt, sitemap et code source **avant** d’affiner ta stratégie de contenu ou tes [optimisations pour ChatGPT / Perplexity](/blog/articles/geo-optimiser-chatgpt-perplexity-sge.html).
