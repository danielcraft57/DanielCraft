# Éco-conception web — positionnement & nouvelles prestations

Document de cadrage commercial et technique pour DanielCraft.  
Complète [PERFORMANCE.md](./PERFORMANCE.md) (optimisations internes du site) et le catalogue [`src/data/prestations.json`](../src/data/prestations.json).

---

## Message de positionnement (source)

> En tant qu'expert en éco-conception, moins de ligne de code inutile, des images optimisées et des vidéos qui ne se lancent pas toutes seules.
>
> Résultat : des pages qui se chargent rapidement, des utilisateurs qui restent, et un Google content qui te met en avant. Donc en épurant ton code et en limitant les recherches inutiles, tu vas pouvoir faire économiser des frais d'hébergement à ton entreprise. Un très bon argument pour un patron. Et aussi, l'éco-conception est un vrai argument de vente pour de nombreux clients qui ne veulent plus de marques qui polluent en silence.

---

## Synthèse en 3 bénéfices clients

| Public | Bénéfice | Formulation simple |
|--------|----------|-------------------|
| **Dirigeant / patron** | Coûts maîtrisés | Site plus léger → moins de bande passante, moins de ressources serveur, facture d'hébergement potentiellement réduite |
| **Marketing / commercial** | Conversion & image | Pages rapides → moins d'abandons ; engagement RSE → différenciation face aux concurrents |
| **Référencement** | Visibilité Google | Performance (Core Web Vitals), sobriété technique et bonne expérience = signaux positifs pour Google et les assistants IA |

---

## Principes opérationnels (ce qu'on fait concrètement)

- **Code épuré** : pas de bibliothèques ou scripts inutiles, pas de trackers superflus, HTML/CSS/JS au strict nécessaire.
- **Images optimisées** : formats modernes (WebP/AVIF), dimensions adaptées, lazy-loading, compression sans perte visible.
- **Vidéos sobres** : pas d'autoplay avec son ; lecture au clic ; poster léger ; hébergement adapté (pas de chargement massif à l'ouverture de page).
- **Requêtes limitées** : moins d'appels API, polices et icônes rationalisées, tiers (widgets, cartes, analytics) audités.
- **Hébergement aligné** : site statique ou léger quand c'est possible ; cache et compression (déjà documenté côté infra).

Ces principes sont déjà appliqués sur le site DanielCraft (voir PERFORMANCE.md). L'offre commerciale consiste à **les vendre explicitement** et à **les auditer/corriger** sur les sites clients.

---

## Lien avec le catalogue actuel

| Prestation existante | Slug | Lien éco-conception |
|---------------------|------|---------------------|
| Votre site est-il rapide ? | `rapport-vitesse` | Diagnostic partiel — manque l'angle coût/RSE et le plan médias |
| Remise en forme Google | `referencement-google` | Mentionne la vitesse mais pas l'éco-conception |
| Site vitrine professionnel | `site-vitrine` | Peut intégrer l'éco-conception comme **standard de livraison** ou **option nommée** |
| Pack mise à jour contenus | `maj-contenus` | Occasion d'alléger images/vidéos lors des MAJ |
| Hébergement & nom de domaine | `hebergement-domaine` | Argument économies si le site consomme moins |

**Écart actuel** : la performance est traitée comme un sous-sujet technique, pas comme un **argument patron + RSE + SEO** packagé.

---

## Nouvelles prestations proposées

### 1. Audit éco-numérique du site

| Champ | Proposition |
|-------|-------------|
| **Slug** | `audit-eco-numerique` |
| **service_slug** | `eco_audit_site` |
| **Catégorie** | `technique` ou nouvelle catégorie `eco` |
| **Prix indicatif** | 149 € HT (entre le rapport vitesse 120 € et l'audit IA 400 €) |
| **Titre client** | Votre site pollue-t-il en silence ? |
| **Tagline** | Bilan clair : poids, vitesse, médias et gaspillages |
| **Pitch** | Mesure du poids des pages, scripts tiers, images et vidéos. Rapport en français avec 3 chiffres clés pour votre patron (Mo transférés, temps de chargement mobile, estimation d'allègement possible) et liste d'actions prioritaires. |
| **Inclus** | Test mobile + desktop, inventaire médias lourds / autoplay, scripts inutiles, rapport PDF, échange 20 min |
| **Différence vs `rapport-vitesse`** | Angle **éco + coût hébergement + image RSE**, pas seulement « pourquoi c'est lent » |

---

### 2. Allègement express (images & vidéos)

| Champ | Proposition |
|-------|-------------|
| **Slug** | `alleger-medias` |
| **service_slug** | `eco_medias_optimize` |
| **Catégorie** | `site-contenu` |
| **Prix indicatif** | 190 € HT |
| **Titre client** | Images et vidéos allégées |
| **Tagline** | Même rendu visuel, pages beaucoup plus légères |
| **Pitch** | Conversion des images en formats modernes, redimensionnement, compression, remplacement des vidéos en autoplay par lecture au clic. Idéal après l'audit ou pour un site qui « rame » sur mobile. |
| **Inclus** | Jusqu'à ~30 images ou équivalent, 1 à 2 vidéos traitées, tests avant/après, mise en ligne |
| **Addon possible** | Lot images supplémentaires +45 € / 15 images |

---

### 3. Site allégé — corrections techniques

| Champ | Proposition |
|-------|-------------|
| **Slug** | `site-allege` |
| **service_slug** | `eco_perf_fix` |
| **Catégorie** | `technique` |
| **Prix indicatif** | 290 à 490 € HT selon complexité |
| **Titre client** | Rendre mon site plus rapide et plus sobre |
| **Tagline** | On enlève ce qui ralentit sans casser votre site |
| **Pitch** | Suite logique de l'audit : suppression de scripts inutiles, optimisation du chargement, cache, polices et icônes rationalisées, correction des vidéos en autoplay. |
| **Inclus** | Corrections prioritaires du rapport, mesure avant/après, compte-rendu avec gain estimé en secondes et en Mo |
| **Upsell** | Couplage naturel avec `referencement-google` ou `visibilite-complete` |

---

### 4. Site vitrine éco-conçu (option ou variante)

| Champ | Proposition |
|-------|-------------|
| **Slug** | `site-vitrine-eco` **ou** option sur `site-vitrine` |
| **service_slug** | `pack_vitrine_eco` |
| **Catégorie** | `identite` |
| **Prix indicatif** | Inclus dans le forfait vitrine **ou** +0 € (différenciateur) **ou** +90 € si badge / page engagement livrés |
| **Titre client** | Site vitrine sobre et rapide |
| **Tagline** | Professionnel, léger, prêt pour Google et pour vos clients sensibles à l'environnement |
| **Pitch** | Même livrable qu'un site vitrine, avec charte **éco-conçue by design** : pas de vidéo qui se lance seule, images optimisées dès la création, code minimal, hébergement adapté. |
| **Inclus** | Tout le pack vitrine + engagement performance (objectif Core Web Vitals verts ou proches) + mention « site éco-conçu » sur une page dédiée |
| **Argument vente** | « Vous ne payez pas plus cher, vous polluez moins » — fort pour artisans, associations, commerces locaux |

---

### 5. Page « Notre engagement numérique »

| Champ | Proposition |
|-------|-------------|
| **Slug** | `page-engagement-numerique` |
| **service_slug** | `eco_page_rse` |
| **Catégorie** | `site-contenu` |
| **Prix indicatif** | 85 € HT (proche d'une page supplémentaire) |
| **Titre client** | Page engagement numérique responsable |
| **Tagline** | Montrez à vos clients que votre site aussi est sérieux sur l'environnement |
| **Pitch** | Une page claire sur votre démarche (site léger, hébergeur, médias sobres) — argument commercial pour les clients qui fuient les marques « qui polluent en silence ». |
| **Inclus** | Rédaction + mise en page + intégration menu, texte validé avec vous |

---

### 6. Suivi sobriété mensuel (abonnement)

| Champ | Proposition |
|-------|-------------|
| **Slug** | `suivi-eco-mensuel` |
| **service_slug** | `eco_monitor_mensuel` |
| **Catégorie** | `maintenance` |
| **Prix indicatif** | 29 € HT / mois |
| **Titre client** | Veille performance & sobriété |
| **Tagline** | Chaque mois, on vérifie que votre site reste léger |
| **Pitch** | Nouvelles images, plugins ou contenus peuvent regonfler le site. Contrôle mensuel du poids et de la vitesse, alerte si dégradation, petites corrections dans un quota léger. |
| **Inclus** | Rapport court mensuel, 1 alerte proactive, 30 min corrections mineures / an cumulées |
| **Bundle** | Proposer avec `entretien-mensuel` (39 €) en pack « Sérénité + Sobriété » ~59 € |

---

### 7. Atelier « Site plus vert pour mon équipe »

| Champ | Proposition |
|-------|-------------|
| **Slug** | `atelier-eco-web` |
| **service_slug** | `eco_formation_2h` |
| **Catégorie** | `maintenance` (ou `technique`) |
| **Prix indicatif** | 120 € HT (équivalent dépannage 2 h) |
| **Titre client** | Atelier : publier sur le web sans alourdir le site |
| **Tagline** | Vos équipes ajoutent du contenu sans casser la performance |
| **Pitch** | Pour les clients qui mettent à jour eux-mêmes : bonnes pratiques images, vidéos, PDF, avant de publier. Réduit les appels support et les régressions. |
| **Inclus** | Visio 2 h, checklist imprimable, enregistrement si souhaité |

---

## Priorisation recommandée (MVP catalogue)

| Priorité | Prestation | Pourquoi |
|----------|------------|----------|
| **P1** | Audit éco-numérique | Porte d'entrée faible, différenciante, complète `rapport-vitesse` |
| **P1** | Allègement express | Livrable concret, visible, facile à vendre après audit |
| **P2** | Site vitrine éco-conçu (différenciateur) | Pas forcément une nouvelle ligne : badge + process sur l'offre existante |
| **P2** | Site allégé — corrections | Panier moyen, suite naturelle de l'audit |
| **P3** | Page engagement numérique | Upsell léger, argument RSE pur |
| **P3** | Suivi sobriété mensuel | Revenu récurrent, à lancer après premiers clients éco |
| **P3** | Atelier équipe | B2B / associations, volume plus faible |

---

## Angles de communication (site, devis, oral)

### Pour le patron
- « Un site plus léger, c'est moins de données à chaque visite — ça peut alléger la facture d'hébergement et éviter de surdimensionner le serveur. »
- « Chaque seconde de chargement en plus, c'est des prospects qui partent avant de vous appeler. »

### Pour le client final (marque)
- « Nous avons choisi un site éco-conçu : pas de vidéos qui tournent dans le vide, des images optimisées, un web plus respectueux. »
- « Pour ceux qui ne veulent plus soutenir des marques qui polluent en silence. »

### Pour Google / visibilité
- « Google favorise les sites rapides et agréables sur mobile — l'éco-conception et le SEO vont dans le même sens. »
- Lier à `visibilite-complete` et `referencement-google`.

---

## Catégorie catalogue optionnelle

Ajout possible dans `prestations.json` :

```json
{
  "id": "eco",
  "title": "Web sobre & performant",
  "nav_label": "Éco-conception",
  "icon": "fa-leaf",
  "description": "Sites plus légers, plus rapides et plus économes — bon pour la planète, pour Google et pour votre budget."
}
```

Alternative : garder les prestations éco dans `technique` + `site-contenu` pour ne pas multiplier les onglets au lancement.

---

## Prochaines étapes techniques (quand validation)

1. ~~Ajouter les entrées P1/P2 dans `src/data/prestations.json`.~~ Fait (7 prestations éco).
2. ~~Créer les SVG `/assets/images/prestations/`.~~ Fait.
3. ~~Enregistrer les slugs dans `assets/js/contact-wizard.js`.~~ Fait.
4. **Sync Facturio** : `python scripts/facturio_sync_prestations.py --full` (descriptions courtes + heures réalistes dans `scripts/facturio_product_payload.py`).
5. Article blog court : « Éco-conception web : ce que ça change pour votre entreprise ».
6. Mention sur la page d'accueil / section « Pourquoi DanielCraft » : éco-conception comme standard de livraison.

---

## Références internes

- [PERFORMANCE.md](./PERFORMANCE.md) — preuves techniques sur le site DanielCraft
- [seo-technique-audit-core-web-vitals.md](../blog/content/articles/seo-technique-audit-core-web-vitals.md) — contenu blog aligné SEO/perf
- Prestation existante `rapport-vitesse` — ne pas cannibaliser : positionner l'audit éco comme **superset** (perf + RSE + coût)
