---
title: "Schema.org et données structurées pour le SEO"
date: 2025-09-19
excerpt: "JSON-LD, types Schema.org (Article, LocalBusiness, FAQPage), Rich Snippets. Comment structurer tes données pour améliorer l'affichage dans les résultats Google."
type: article
tags: [SEO, Schema.org, JSON-LD, données structurées, Rich Snippets]
series: seo-serie
series_order: 7
og_image: seo-schema-1200x630.jpg
---

# Schema.org et données structurées pour le SEO

Les données structurées (Schema.org) aident Google à comprendre ton contenu et à l'afficher sous forme de Rich Snippets : étoiles, FAQ, extraits enrichis. Ce guide présente les types essentiels et la mise en œuvre en JSON-LD.

<figure>
<img src="../../assets/images/blog/html-technique.svg" alt="Donnees structurees Schema.org et JSON-LD" class="schema-inline" width="400" />
<figcaption>Le balisage JSON-LD aide Google a comprendre et afficher ton contenu.</figcaption>
</figure>

---

## 1. Pourquoi les données structurées

- **Compréhension** : Google identifie le type de contenu (article, entreprise, produit, etc.)
- **Rich Snippets** : affichage enrichi dans les résultats (étoiles, prix, FAQ)
- **Voice search** : les assistants s'appuient sur les données structurées pour répondre

---

## 2. Format JSON-LD

Le format recommandé par Google : une balise `<script type="application/ld+json">` dans le `<head>` ou le `<body>`.

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Titre de l'article",
  "author": {"@type": "Person", "name": "Loïc DANIEL"},
  "datePublished": "2026-02-21"
}
```

---

## 3. Types utiles

### Article / BlogPosting

Pour les articles de blog : titre, auteur, date, image.

### LocalBusiness

Pour les fiches entreprise : nom, adresse, téléphone, horaires, avis.

### FAQPage

Pour les blocs FAQ : questions et réponses. Peut générer un encadré FAQ dans la SERP.

### HowTo

Pour les tutoriels : étapes numérotées. Rich Snippet possible.

### Product

Pour les fiches produits : nom, prix, disponibilité, avis.

---

## 4. Validation

- **Google Rich Results Test** : teste tes données structurées
- **Search Console** : rapport "Améliorations" pour les erreurs
- **Schema.org Validator** : vérification de la syntaxe

---

## Conclusion

Les données structurées renforcent la compréhension de ton contenu par Google et peuvent améliorer l'affichage dans les résultats. Commence par Article, LocalBusiness et FAQPage selon ton type de site.
