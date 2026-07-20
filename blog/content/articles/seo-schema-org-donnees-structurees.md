---
title: "Donnees structurees : aider Google a comprendre ta page"
date: 2024-07-18
excerpt: "Schema.org et rich results : des infos claires pour les machines, sans tricher."
type: article
tags: [SEO, Schema.org, JSON-LD, données structurées, Rich Snippets]
series: seo-serie
series_order: 7
og_image: seo-schema-1200x630.jpg
---

# Donnees structurees : aider Google a comprendre ta page

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/seo-schema-org.svg" alt="Schema donnees structurees Schema.org" class="schema-inline" width="640" />
  <figcaption>Page, balises, Schema.org, rich result, clic.</figcaption>
</figure>

Les données structurées (Schema.org) aident Google à comprendre ton contenu et à l'afficher sous forme de Rich Snippets : étoiles, FAQ, extraits enrichis. Ce guide présente les types essentiels et la mise en œuvre en JSON-LD.

## Pourquoi les données structurées comptent

Google lit ton HTML, mais sans contexte explicite, il doit deviner : s'agit-il d'un article, d'un produit, d'une recette ? Les données structurées répondent à cette question en langage machine. Elles ne garantissent pas un meilleur classement, mais elles améliorent souvent le taux de clic grâce à un affichage plus riche dans les résultats de recherche.

Les bénéfices concrets :

- **Compréhension** : Google identifie le type de contenu (article, entreprise, produit, etc.)
- **Rich Snippets** : affichage enrichi dans les résultats (étoiles, prix, FAQ)
- **Voice search** : les assistants vocaux s'appuient sur ces données pour formuler leurs réponses

L'important : décrire fidèlement ce qui est visible sur la page. Inventer des étoiles ou des prix fictifs, c'est une violation des consignes Google.

## Le format JSON-LD, recommandé par Google

Le format le plus simple à maintenir est JSON-LD : une balise `<script type="application/ld+json">` dans le `<head>` ou le `<body>`. Contrairement au microdata (balises HTML imbriquées), le JSON-LD reste séparé du contenu visuel et se met à jour facilement.

Exemple minimal pour un article de blog :

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Titre de l'article",
  "author": {"@type": "Person", "name": "Loïc DANIEL"},
  "datePublished": "2026-02-21",
  "image": "https://example.com/image.jpg"
}
```

Tu peux combiner plusieurs types dans un même bloc ou en empiler plusieurs scripts. Par exemple, un article avec une FAQ embarque un `@type: FAQPage` en plus de `Article`.

## Types Schema.org les plus utiles

### Article / BlogPosting

Pour les articles de blog : titre, auteur, date de publication, image principale. Indispensable pour les sites éditoriaux. Pense aussi à `dateModified` si tu mets à jour régulièrement tes contenus.

### LocalBusiness

Pour les fiches entreprise : nom, adresse, téléphone, horaires, avis. Couple ce type avec une fiche Google Business Profile cohérente. Les champs `geo`, `openingHoursSpecification` et `aggregateRating` renforcent ta présence locale.

### FAQPage

Pour les blocs FAQ : liste de questions/réponses. Google peut afficher un encadré déroulant directement dans la SERP. Chaque question doit avoir une réponse visible sur la page, pas seulement dans le JSON-LD.

### HowTo

Pour les tutoriels pas à pas : étapes numérotées, durée estimée, outils nécessaires. Particulièrement efficace pour les guides pratiques (« comment installer… », « comment configurer… »).

### Product

Pour les fiches produits e-commerce : nom, prix, disponibilité, avis. Le rich snippet peut afficher le prix et les étoiles. Vérifie que les données correspondent exactement à ce que voit l'utilisateur.

## Validation et suivi

Avant de publier, teste systématiquement :

- **Google Rich Results Test** : vérifie l'éligibilité aux rich results
- **Search Console** : onglet « Améliorations » pour repérer erreurs et avertissements
- **Schema.org Validator** : contrôle la syntaxe JSON-LD

En production, surveille le rapport « Données structurées » dans Search Console. Une erreur sur un champ obligatoire peut faire disparaître l'enrichissement pour des centaines de pages.

## Bonnes pratiques à retenir

Commence petit : implémente d'abord les types qui correspondent vraiment à ton site. Un blog = `Article`. Un commerce local = `LocalBusiness`. Un site avec FAQ = `FAQPage`. Automatise la génération du JSON-LD dans ton CMS ou ton générateur de site pour éviter les oublis page par page.

Ne duplique pas le contenu : le JSON-LD complète le HTML, il ne le remplace pas. Google compare les deux.

## Conclusion

Les données structurées renforcent la compréhension de ton contenu par Google et peuvent améliorer l'affichage dans les résultats. Commence par Article, LocalBusiness et FAQPage selon ton type de site, valide avec les outils Google, puis itère. Pour poser les fondations techniques qui facilitent l'indexation de ces pages, consulte aussi le guide sur le [SEO technique et les Core Web Vitals](/blog/articles/seo-technique-audit-core-web-vitals.html).
