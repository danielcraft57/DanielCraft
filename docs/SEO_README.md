# SEO - Optimisation Référencement

Ce document explique les optimisations SEO mises en place sur danielcraft.fr.

## Balises Open Graph

Toutes les pages incluent les balises Open Graph complètes selon [ogp.me](https://ogp.me/) :

- `og:title` - Titre de la page
- `og:description` - Description
- `og:type` - Type de contenu (website)
- `og:url` - URL canonique
- `og:image` - Image de partage (1200x630px recommandé)
- `og:image:secure_url` - Version HTTPS de l'image
- `og:image:type` - Type MIME de l'image
- `og:image:width` - Largeur (1200px)
- `og:image:height` - Hauteur (630px)
- `og:image:alt` - Texte alternatif
- `og:site_name` - Nom du site (DanielCraft)
- `og:locale` - Locale (fr_FR)

## Twitter Cards

Toutes les pages incluent les balises Twitter Card :

- `twitter:card` - Type de carte (summary_large_image)
- `twitter:title` - Titre
- `twitter:description` - Description
- `twitter:image` - Image de partage
- `twitter:image:alt` - Texte alternatif

## Schema.org (JSON-LD)

Structured data selon [schema.org](https://schema.org/) :

### Page d'accueil (index.html)
- **Person** - Informations sur Loïc DANIEL
- **LocalBusiness** - Informations sur l'entreprise
- **ProfessionalService** - Services proposés avec offres détaillées

### Page Processus (processus.html)
- **WebPage** - Page web
- **HowTo** - Processus en 5 étapes

### Page Metz (metz.html)
- **WebPage** - Page web
- **LocalBusiness** - Business local avec services pour Metz

### Page Portfolio (portfolio.html)
- **CollectionPage** - Page de collection
- **ItemList** - Liste de projets

## Fichiers SEO

### sitemap.xml
Plan du site XML pour les moteurs de recherche. Contient toutes les pages importantes avec :
- URL
- Date de dernière modification
- Fréquence de changement
- Priorité

### robots.txt
Instructions pour les robots des moteurs de recherche :
- Autorise l'indexation de toutes les pages
- Référence le sitemap
- Interdit l'indexation du dossier blog

## Meta Tags Standards

Chaque page inclut :
- `<title>` - Titre optimisé (50-60 caractères)
- `<meta name="description">` - Description (150-160 caractères)
- `<meta name="keywords">` - Mots-clés pertinents
- `<meta name="author">` - Auteur
- `<meta name="robots">` - Instructions pour les robots
- `<link rel="canonical">` - URL canonique
- `<html lang="fr">` - Langue de la page

## Images Open Graph et visuels marketing

**IMPORTANT** : Les images Open Graph sont désormais organisées par page dans `assets/images/og/`

Architecture recommandée :
- `assets/images/og/home-1200x630.jpg` - Page d'accueil
- `assets/images/og/portfolio-1200x630.jpg` - Page portfolio
- `assets/images/og/prestations-1200x630.jpg` - Page autres prestations
- `assets/images/og/metz-1200x630.jpg` - Page développeur à Metz

Spécifications communes :
- Format : JPEG
- Dimensions : 1200x630px (ratio 1.91:1)
- Poids : < 1MB recommandé
- Style : cohérent avec danielcraft.fr (fond clair, accent rouge `#dc2626`, typographie type Inter)

En complément, des visuels marketing sont générés pour :
- Le **hero** de la page d'accueil (`assets/images/hero/`)
- Certains **projets** du portfolio (`assets/images/projects/`)

Ces images peuvent être lourdes (JPEG haute qualité) et sont donc ignorées par Git via `.gitignore`. Elles sont considérées comme des assets générés à partir des prompts documentés dans `docs/prompt_og_image.md`.

Outils pour créer l'image :
- Canva (template "Facebook Post")
- Figma
- Photoshop

## Validation

Pour valider le SEO :

1. **Open Graph** : [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/)
2. **Twitter Cards** : [Twitter Card Validator](https://cards-dev.twitter.com/validator)
3. **Schema.org** : [Google Rich Results Test](https://search.google.com/test/rich-results)
4. **Sitemap** : [XML Sitemap Validator](https://www.xml-sitemaps.com/validate-xml-sitemap.html)

## Google Search Console et Google Analytics

### Google Search Console (Vérification)
- ✅ Vérification configurée via DNS TXT record
- ✅ Code de vérification : `YCJxWstMUnz66PNyUF1JsgpqpXATeyl5D6gM1nSfJ88`
- 📖 Voir le guide complet : [GOOGLE_SETUP.md](./GOOGLE_SETUP.md)

### Google Analytics (GA4)
- ✅ Script Google Analytics GA4 configuré dans toutes les pages HTML
- ✅ Measurement ID : `G-4VN3CKFP14`
- 📖 Voir le guide complet : [GOOGLE_SETUP.md](./GOOGLE_SETUP.md)

## Prochaines Étapes

- [x] Ajouter Google Analytics (configuré avec G-4VN3CKFP14)
- [x] Ajouter Google Search Console (vérifié via DNS)
- [ ] Créer / mettre à jour les 4 images OG (`home-1200x630.jpg`, `portfolio-1200x630.jpg`, `prestations-1200x630.jpg`, `metz-1200x630.jpg`) dans `assets/images/og/`
- [ ] Soumettre le sitemap dans Google Search Console
- [ ] Optimiser les images (compression, WebP)
- [ ] Ajouter des balises hreflang si multilingue
- [ ] Créer un fichier humans.txt

