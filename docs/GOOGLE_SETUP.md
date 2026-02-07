# Configuration Google Verification et Google Analytics

Ce guide explique comment obtenir et configurer Google Search Console (vérification) et Google Analytics pour danielcraft.fr.

## ✅ Configuration Actuelle

- **Google Search Console** : Vérifié via DNS TXT record
  - Code : `YCJxWstMUnz66PNyUF1JsgpqpXATeyl5D6gM1nSfJ88`
  
- **Google Analytics** : Configuré avec GA4
  - Measurement ID : `G-4VN3CKFP14`

## Google Search Console (Vérification)

Google Search Console permet de suivre les performances de votre site dans les résultats de recherche Google.

### Étapes pour obtenir le code de vérification

1. **Accéder à Google Search Console**
   - Allez sur [https://search.google.com/search-console](https://search.google.com/search-console)
   - Connectez-vous avec votre compte Google

2. **Ajouter une propriété**
   - Cliquez sur "Ajouter une propriété"
   - Entrez votre URL : `https://danielcraft.fr`
   - Cliquez sur "Continuer"

3. **Choisir la méthode de vérification**
   - Sélectionnez "Balise HTML" dans les méthodes proposées
   - Google vous donnera un code qui ressemble à : `abc123def456ghi789jkl012mno345pqr678stu901vwx234yz`

4. **Remplacer le code dans les fichiers HTML**
   - Ouvrez tous les fichiers HTML du site (index.html, processus.html, metz.html, portfolio.html, projets.html, statistiques.html)
   - Recherchez : `<meta name="google-site-verification" content="YOUR_GOOGLE_VERIFICATION_CODE">`
   - Remplacez `YOUR_GOOGLE_VERIFICATION_CODE` par le code fourni par Google
   - Sauvegardez les fichiers

5. **Vérifier la propriété**
   - Retournez sur Google Search Console
   - Cliquez sur "Vérifier"
   - Google va vérifier que la balise meta est présente sur votre site
   - Une fois vérifié, vous aurez accès aux données de recherche

### Alternative : Vérification par fichier HTML

Si vous préférez utiliser un fichier HTML au lieu d'une balise meta :

1. Google vous donnera un nom de fichier (ex: `google1234567890abcdef.html`)
2. Créez ce fichier à la racine de votre site
3. Uploadez-le sur votre serveur
4. Google vérifiera automatiquement

## Google Analytics (GA4)

Google Analytics permet de suivre le trafic et le comportement des visiteurs sur votre site.

### Étapes pour obtenir le Measurement ID

1. **Accéder à Google Analytics**
   - Allez sur [https://analytics.google.com](https://analytics.google.com)
   - Connectez-vous avec votre compte Google

2. **Créer un compte Analytics (si vous n'en avez pas)**
   - Cliquez sur "Commencer la mesure"
   - Remplissez les informations demandées :
     - Nom du compte : "DanielCraft" (ou ce que vous voulez)
     - Nom de la propriété : "danielcraft.fr"
     - Fuseau horaire : "Europe/Paris"
     - Devise : "Euro (€)"
   - Cliquez sur "Suivant"

3. **Configurer la propriété**
   - Sélectionnez "Web" comme plateforme
   - URL du site web : `https://danielcraft.fr`
   - Nom du flux de données : "Site web principal"
   - Cliquez sur "Créer le flux"

4. **Obtenir le Measurement ID**
   - Une fois le flux créé, Google vous donnera un Measurement ID
   - Il ressemble à : `G-XXXXXXXXXX` (où X sont des lettres et chiffres)

5. **Remplacer le Measurement ID dans les fichiers HTML**
   - Ouvrez tous les fichiers HTML du site
   - Recherchez : `gtag/js?id=G-XXXXXXXXXX` et `gtag('config', 'G-XXXXXXXXXX');`
   - Remplacez `G-XXXXXXXXXX` par votre vrai Measurement ID dans les deux endroits
   - Sauvegardez les fichiers

6. **Vérifier que ça fonctionne**
   - Visitez votre site : https://danielcraft.fr
   - Retournez sur Google Analytics
   - Allez dans "Rapports" > "Temps réel"
   - Vous devriez voir votre visite apparaître dans les 30 secondes

## Fichiers à modifier

Une fois que vous avez vos codes, vous devez les remplacer dans ces fichiers :

- `index.html`
- `processus.html`
- `metz.html`
- `portfolio.html`
- `projets.html`
- `statistiques.html`

## Recherche et remplacement rapide

### Pour Google Verification

Recherchez dans tous les fichiers :
```
YOUR_GOOGLE_VERIFICATION_CODE
```

Remplacez par votre code de vérification.

### Pour Google Analytics

Recherchez dans tous les fichiers :
```
G-XXXXXXXXXX
```

Remplacez par votre Measurement ID (il apparaît deux fois par fichier).

## Vérification finale

Après avoir ajouté les codes :

1. **Google Search Console**
   - Vérifiez que votre propriété est vérifiée
   - Soumettez votre sitemap : `https://danielcraft.fr/sitemap.xml`
   - Allez dans "Sitemaps" > "Ajouter un nouveau sitemap"

2. **Google Analytics**
   - Visitez votre site plusieurs fois depuis différents appareils/navigateurs
   - Vérifiez dans "Temps réel" que les visites sont enregistrées
   - Attendez 24-48h pour voir les données complètes dans les rapports standards

## Ressources utiles

- [Google Search Console - Documentation](https://support.google.com/webmasters)
- [Google Analytics - Documentation](https://support.google.com/analytics)
- [Tester votre site avec Google Rich Results](https://search.google.com/test/rich-results)
- [Google PageSpeed Insights](https://pagespeed.web.dev/) - Pour optimiser les performances

## Notes importantes

- Les codes sont uniques à votre site, ne les partagez pas publiquement
- La vérification Google Search Console peut prendre quelques minutes
- Les données Google Analytics peuvent prendre jusqu'à 24-48h pour apparaître dans les rapports standards
- Le temps réel fonctionne immédiatement dans Google Analytics

