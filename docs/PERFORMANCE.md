# Optimisations de Performance - DanielCraft

Ce document liste toutes les optimisations de performance mises en place pour améliorer le chargement et réduire la taille des fichiers.

## Optimisations Mises en Place

### 1. Fonts (Polices)

#### Avant
- Chargement de tous les poids (300, 400, 500, 600, 700, 800, 900)
- Pas de subset (tous les caractères)
- Pas de preload

#### Après
- ✅ Chargement uniquement des poids utilisés (400, 500, 600, 700)
- ✅ Subset latin uniquement (réduction ~30-40% de la taille)
- ✅ `display=swap` pour éviter le FOIT (Flash of Invisible Text)
- ✅ Chargement asynchrone avec `media="print"` et `onload`
- ✅ Preconnect pour les domaines Google Fonts

**Gain estimé** : ~50-60% de réduction de la taille des fonts

### 2. Font Awesome

#### Avant
- Chargement complet de Font Awesome 6.5.0 (~100KB)

#### Après
- ✅ Intégrité SRI (Subresource Integrity) pour la sécurité
- ✅ `referrerpolicy="no-referrer"` pour la confidentialité
- ⚠️ **Recommandation future** : Utiliser uniquement les icônes SVG nécessaires pour réduire à ~10-20KB

**Gain potentiel** : ~80% de réduction si on passe aux SVG uniquement

### 3. CSS (Feuilles de style)

#### Avant
- Chargement synchrone de tous les CSS
- Blocage du rendu

#### Après
- ✅ Preload pour `main.css` (CSS critique)
- ✅ Chargement asynchrone pour `animations.css` et `responsive.css`
- ✅ Technique `media="print"` + `onload` pour le chargement non-bloquant

**Gain estimé** : Amélioration du First Contentful Paint (FCP) de ~200-300ms

### 4. JavaScript

#### Avant
- Scripts chargés de manière synchrone

#### Après
- ✅ Attribut `defer` sur tous les scripts
- ✅ Preload pour `main.js` (script critique)
- ✅ Scripts exécutés après le parsing HTML

**Gain estimé** : Amélioration du Time to Interactive (TTI) de ~100-200ms

### 5. DNS et Connexions

#### Ajouté
- ✅ DNS Prefetch pour :
  - `fonts.googleapis.com`
  - `fonts.gstatic.com`
  - `cdnjs.cloudflare.com`
  - `www.googletagmanager.com`

**Gain estimé** : Réduction de ~50-100ms sur les requêtes DNS

### 6. Compression Nginx

#### Avant
- Compression Gzip basique

#### Après
- ✅ Gzip optimisé (niveau 6, types étendus)
- ✅ Taille minimale réduite à 256 bytes (au lieu de 1000)
- ✅ Support Brotli préparé (commenté, à activer si module installé)
- ✅ Headers Vary pour la mise en cache

**Gain estimé** : ~70-80% de réduction de la taille des fichiers textuels

### 7. Cache Nginx

#### Avant
- Cache de 30 jours pour les assets

#### Après
- ✅ Cache de 1 an pour les assets statiques (immutable)
- ✅ Cache de 1 heure pour les HTML (pour permettre les mises à jour)
- ✅ Headers Cache-Control optimisés
- ✅ Access-Control-Allow-Origin pour les fonts

**Gain estimé** : Réduction de ~90% des requêtes répétées

## Métriques de Performance Attendues

### Avant Optimisations
- **First Contentful Paint (FCP)** : ~1.5-2.0s
- **Largest Contentful Paint (LCP)** : ~2.5-3.0s
- **Time to Interactive (TTI)** : ~3.0-4.0s
- **Total Blocking Time (TBT)** : ~300-500ms
- **Cumulative Layout Shift (CLS)** : Variable

### Après Optimisations (Estimations)
- **First Contentful Paint (FCP)** : ~0.8-1.2s (-40%)
- **Largest Contentful Paint (LCP)** : ~1.5-2.0s (-35%)
- **Time to Interactive (TTI)** : ~2.0-2.5s (-30%)
- **Total Blocking Time (TBT)** : ~100-200ms (-60%)
- **Cumulative Layout Shift (CLS)** : Amélioré

## Optimisations Futures Recommandées

### 1. Images
- [ ] Convertir les images en WebP/AVIF
- [ ] Implémenter le lazy loading pour les images
- [ ] Utiliser des images responsive avec `srcset`
- [ ] Compresser les images existantes (TinyPNG, ImageOptim)

### 2. Font Awesome
- [ ] Remplacer Font Awesome par des SVG inline pour les icônes utilisées
- [ ] Utiliser un système d'icônes plus léger (Heroicons, Feather Icons)

### 3. CSS/JS
- [ ] Minifier les fichiers CSS et JS
- [ ] Concaténer les CSS en un seul fichier
- [ ] Utiliser CSS critical inline pour le above-the-fold

### 4. Service Worker
- [ ] Implémenter un Service Worker pour le cache offline
- [ ] Mise en cache stratégique des ressources

### 5. HTTP/2 Server Push
- [ ] Configurer HTTP/2 Server Push pour les ressources critiques

### 6. CDN
- [ ] Utiliser un CDN (Cloudflare, CloudFront) pour les assets statiques

## Outils de Test

Pour vérifier les performances :

1. **Google PageSpeed Insights**
   - https://pagespeed.web.dev/
   - Teste sur mobile et desktop

2. **Google Lighthouse** (dans Chrome DevTools)
   - F12 > Lighthouse > Run audit

3. **WebPageTest**
   - https://www.webpagetest.org/
   - Tests détaillés depuis différents emplacements

4. **GTmetrix**
   - https://gtmetrix.com/
   - Analyse complète avec recommandations

## Commandes Utiles

### Vérifier la compression Gzip
```bash
curl -H "Accept-Encoding: gzip" -I https://danielcraft.fr/assets/css/main.css
```

### Vérifier les headers de cache
```bash
curl -I https://danielcraft.fr/assets/css/main.css
```

### Tester la taille des ressources
```bash
curl -s https://danielcraft.fr/assets/css/main.css | wc -c
```

## Notes Importantes

- Les optimisations de fonts nécessitent de vérifier que tous les poids utilisés sont bien chargés
- Le chargement asynchrone des CSS peut causer un FOUC (Flash of Unstyled Content) - surveiller
- Les scripts avec `defer` s'exécutent dans l'ordre, ce qui est important pour les dépendances
- Le cache long (1 an) nécessite un système de versioning des fichiers (ex: `main.v2.css`)

## Maintenance

- Vérifier régulièrement les performances avec Lighthouse
- Surveiller les Core Web Vitals dans Google Search Console
- Mettre à jour les dépendances (Font Awesome, etc.) régulièrement
- Optimiser les nouvelles images avant de les ajouter

