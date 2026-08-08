# Agents - DanielCraft

## Style des textes de pages

Quand tu rediges du contenu pour les pages du site (HTML, JSON meta/SEO, fiches prestations, livres, blog, includes marketing), ecris comme une personne reelle.

- Naturel, spontane, vivant - comme une discussion entre amis
- Evite les phrases toutes faites, le jargon trop formel ou technique, et les formulations trop parfaites
- Tournures simples, claires, directes ; un peu imparfaites si besoin, mais toujours humaines
- Tu peux raccourcir des phrases ou employer un ton plus detendu
- La reponse / le texte ne doit pas sembler ecrit par une IA ni ressembler a un chatbot

### Ponctuation

- Apostrophes droites uniquement : `'` (pas d'apostrophes courbees)
- Tirets simples uniquement : `-` (pas de tirets cadratins `—`)

### Portee

S'applique au contenu visible et SEO des pages (`src/pages/`, includes de texte, `src/data/*.json` descriptifs, articles blog). Pas aux commentaires techniques de code ni aux logs de build.

### Ton Grand Est / Lorrain (leger)

Le site parle aux commerces du **Grand Est**. On peut colorer le francais avec un **levain lorrain**, sans transformer la page en patois illisible.

**Dosage** : 1 touche locale de temps en temps (hero lead, bio, CTA soft, blog) - pas un mot dialectal par phrase. Le client doit comprendre du premier coup.

**Repères locaux (OK a glisser)** :

| Dire | Sens / usage |
|------|----------------|
| `entre midi` | entre 12 h et 14 h (pas « a midi ») |
| `ca geths` / `ca geths sa moal` | ca va ? / ca va bien (Moselle, influence platt) |
| `comment qu'c'est ?` | comment ca va ? (tournure locale) |
| `ca tire` | il y a un courant d'air |
| `nareux` / `nareuse` | difficile sur la bouffe / le propre (Robert 2021) |
| `clanche` / `clancher` | poignee / ouvrir-fermer la porte |
| `cornet` | sac plastique |
| `schlappe` | pantoufle |
| `schneck` | pain au raisin |
| `schlouk` | une gorgee |
| `chawée` | grosse averse (w comme Waterloo) |
| `prendre une rincee` | etre trempe sous la pluie |
| `couarail` | discussion improvisee, papotage |
| `bassoter` | ne pas avancer dans le boulot |
| `beugner` | abimer, cogner, faire une bosse |
| `trisser` | se tirer vite / gicler |
| `vi` / `ui` | oui (familier) |
| `Ach jo`, `oye`, `oh leck` | interjections mosellanes (tres leger, oral) |
| article + prenom | « le Loic », « la Marie » (tournure locale) |
| imperatif + `voir` | « regarde voir », « dis voir » |
| Metz | on dit **Mess** a l'oral ; a l'ecrit garder Metz |

**Grand Est au sens large** : parler des villes (Nancy, Epinal, Strasbourg, Thionville…) sans jargon alsa ; ne pas confondre Lorraine et Alsace. Positionnement marketing = **Grand Est** ; ancrage perso Loic = Metz + terrain (Nancy, Epinal, Strasbourg).

**A eviter sur le site** : gros mots de soif (`cheuler`, `chouille`) en hero/CTA ; argot parisien deguise en lorrain (`daron`, `schlinguer` - pas specifiquement local) ; phonetique illisible type `j'mopel`. Preferer une tournure naturelle + 1 mot local.

**Exemples de ton** :
- « On peut se parler entre midi si t'es au magasin. »
- « Pas la peine de faire le nareux avec le devis : prix affiche, PDF direct. »
- « Dis voir ce qui bloque - on demele ca ensemble. »

Sources d'inspiration (lexique, pas a copier tel quel) : parler lorrain / Moselle (clanche, entre midi, ca geths, nareux), Radio Melodie / lexiques locaux.

### Public client (prioritaire)

Les clients (commerces, artisans, independants du Grand Est) **ne sont pas informaticiens**. Ils n'ont pas a comprendre le jargon.

Quand tu rediges pour le site (accueil, fiches, audit, contact, FAQ, SEO grand public) :
- **Interdit** (sauf blog tech / livres / page pro explicite) : CMS, SSR, Lighthouse, framework, TypeScript, Astro, Next, API, DevOps, CI/CD, refactoring, etc.
- **Preferer** : site rapide, clair sur telephone, trouve sur Google, devis simple, livraison en jours, un seul interlocuteur, bien protege / suivi apres mise en ligne.
- Expliquer le **benefice** avant le **moyen**. Si un terme tech est indispensable, le traduire en une phrase simple juste apres.
- Ne jamais faire sentir le client « nul » en info : ton egal a egal, naturel.

### Positionnement IA (depuis 2025)

Loic travaille **avec l'IA** depuis **2025**, avec une **expertise prompts** (bien briefer l'outil = meilleurs resultats). Ca ne remplace pas le metier : ca accelere le brouillon, la doc, les tests, le detail - **lui valide, corrige, livre**.

**Promesses client (langage simple)** :
- Environ **3x plus vite** qu'un process classique sans IA bien cadree
- Vitrine / projet standard souvent **livre en moins d'une semaine** (delais annonces selon devis)
- Dev depuis **2011**, licence **2018** : il sait quoi demander a l'IA, quoi garder, quoi jeter
- Tests + **securite** (anti piratage de base / bonnes pratiques) restent de son cote

**Arguments utiles (agents / docs - a traduire en francais simple sur le site)** - inspirés etudes 2025-2026 (Sonar, Black Duck, etc.) :
- Gains de vitesse reels sur l'ecriture et la doc (souvent plusieurs heures / semaine recuperees)
- L'IA aide aussi a **expliquer** du code, generer des **tests**, prototyper vite
- Adoption tres large chez les pros : l'outil est devenu standard, pas un gadget
- Le vrai metier aujourd'hui : **verifier** ce que l'IA propose (qualite, securite) - d'ou l'interet d'un dev experimente aux commandes
- Sans revue humaine, risque de code « qui a l'air bon » mais fragile : DanielCraft assume la **relecture + tests**

**A ne pas dire au client** : pourcentages d'etudes, noms d'outils IA, « LLM », « hallucination ». Preferer : « j'utilise l'IA pour aller plus vite, et je controle tout avant de livrer ».

**Ou placer sur le site** :
| Zone | Message (esprit) |
|------|------------------|
| Accueil `#about` | Dev 2011 + IA depuis 2025 + livraison rapide |
| Accueil FAQ | « Tu utilises l'IA ? » → oui, plus vite, je valide |
| `/audit` | Diagnostic rapide grace au duo experience + IA |
| `/contact` / wizard | Delais courts, un interlocuteur qui maitrise le process |
| `/processus` | Etape realisation : IA + controle humain |
| `/nos-offres` | Rappel delai vitrine |
| Fiches prestations | Delai indicatif + « methode moderne, controlee » (sans jargon) |
| Blog (serie pratique) | Articles pedagogiques sur travailler avec l'IA sans blabla |
| `/projets` ou espace pro | OK jargon leger pour pairs |

**Avatars** : toujours `loic-*-ingenieur` (hero A/B + about) - voir section Avatars Loic.

### Microdata schema.org (obligatoire sur pages marketing)

Preferer les **microdata** HTML (`itemscope` / `itemtype` / `itemprop`) coherents, pas du jargon visible.

Types usuels :
- Accueil : `WebPage` + `ProfessionalService` (`mainEntity`) + `Person` (`about`) + `FAQPage` (`hasPart`) + `Service`/`Offer` packs + `ItemList`/`BlogPosting` blog
- Contact : `ContactPage` + `ProfessionalService`
- Processus : `WebPage` + `HowTo` / `HowToStep`
- Audit / fiches : `Service` + `Offer` + `Person`/`Organization` provider
- Vitrines / offres : `CollectionPage` ; detail vitrine : `Product`

Regles :
- Completer `name`, `description`, `url`, `offers` (prix EUR), `provider` quand c'est une offre
- Images schema via `link itemprop="image"` si lazy-load (`data-src`)
- Mettre a jour les microdata si le JS change les titres/liens (ex. rotation blog)
- Ne pas casser l'accessibilite : microdata en meta/link hidden OK

### Positionnement tech (pas de CMS classiques)

Loic : **dev depuis 2011**, **licence en 2018**. DanielCraft ne vend **pas** du WordPress, Prestashop, Wix, Squarespace ni autre usine a plugins. On assume un stack **moderne, perf et maintenable**.

Quand tu ecris (accueil, bio, blog, livres, fiches) :
- **Interdit** de presenter le travail comme « un site WordPress » / « sous CMS » / page builder.
- Preferer : sites **faits sur-mesure**, rapides, clairs - la stack precise reste en **2e rideau** sauf page tech / blog / livres.
- Au client commerce : benefices d'abord (rapide, clair sur telephone, trouve sur Google).

**Stacks populaires** (usage interne / blog tech / livres - **pas** en hero client) 2025-2026 :

| Famille | Outils | Pourquoi c'est pertinent |
|---------|--------|---------------------------|
| Contenu / vitrine ultra-rapide | **Astro** | Ideal marketing, blog, catalogue |
| App React full-stack | **Next.js** | Standard marche |
| Full-stack leger | **SvelteKit** | Bundles petits, bon throughput |
| UI | **React**, **Vue** (+ **Nuxt**) | Ecrans interactifs |
| Langage | **TypeScript** | Moins de bugs |
| CSS | **Tailwind CSS** | Iteration rapide |
| Backend / outils | **Python**, **Node**, **Go**, **Rust** | Selon besoin |

**Ce site (DanielCraftFr)** : generateur Python (`build.py`), HTML/CSS/JS soignes, assets WebP.

**Livres / exemples** : stack moderne - **jamais** WordPress comme produit phare.

Detail marketing IA : `docs/POSITIONNEMENT_IA.md`.

### Avatars Loic (valides aout 2026)

Photos de base + generation : look **ingenieur**, un peu plus **muscle / air sportif** (valide par Loic).

| Fichier | Usage |
|---------|--------|
| `assets/images/home/loic-hero-ingenieur.png` (+ `.webp`) | Hero accueil frame A (`eager`) |
| `assets/images/home/loic-hero-ingenieur-b.png` (+ `.webp`) | Hero crossfade frame B (~9s CSS) |
| `assets/images/home/loic-about-ingenieur.png` (+ `.webp`) | Qui suis-je + page contact |

**Ne pas** remplacer par `loic-hero.png` / `loic-about.png` (anciennes variantes) sauf demande explicite.

Pipeline apres regen :
1. Copier les PNG dans `assets/images/home/`
2. Redimensionner (hero ~800x1200, about 800x800), compresser PNG + regenerer WebP (quality ~80-85) - supprimer les `.webp` existants avant sinon `build.py` les saute
3. Brancher dans `src/pages/index.html` (hero + `#about`) et `src/pages/contact.html`
4. `python build.py index contact` (+ sync `dist/assets`)

Schema : `itemprop="image"` / `link` vers `loic-about-ingenieur.png`.

## Projet

- **DanielCraft** : site portfolio / commerce local (Metz), build Python (`build.py`), templates dans `src/`, assets dans `assets/`, sortie `dist/`.
- **Accueil** : `src/pages/index.html` (+ CSS/JS home).
- **Catalogue offres** : `/nos-offres` (`prestations.json`, hub categories, fiches `/prestations/<slug>/`).
- **Livres** : `/livres` + dossier source `livres-formation/`.
- **Portfolio** : section `#portfolio` / `assets/js/portfolio.js` (images `assets/images/projets/`).
- **Page projets GitHub** : `src/pages/projets.html` + `assets/js/github-projects.js` / `src/data/projects.json`.
- **Blog** : `blog/`, build `blog/build_blog.py` integre au build principal.
- **Dev local** : `.\scripts\serve_dev.ps1` (PHP + watch). WebP : `.\scripts\serve_dev.ps1 --webp` (sinon `--no-webp` par defaut).
- **Deploiement** : voir `docs/DEPLOYMENT.md` et `scripts/deploy-content.ps1`.

## Production

- **SSH** : utilisateur `pi`, hote `node12.lan` (reseau LAN).
- **Stack** : **nginx** sur la meme machine ; contenu typiquement sous `/var/www/...`.
- Exemple PowerShell (adapter chemins / URL) :

```powershell
.\scripts\deploy-content.ps1 `
  -ServerUser "pi" `
  -ServerHost "node12.lan" `
  -ServerPath "/var/www/danielcraft.fr" `
  -SiteBase "https://danielcraft.fr" `
  -NginxLogName "danielcraft.fr"
```

- Preferer les secrets et cibles de deploiement dans `.env.local` / `.env` (non versionnes), variables `DEPLOY_*`.

## Initiative : mini-sites « portfolio » par secteur

**Objectif** : creer **plusieurs sites web artificiels** (vitrines / one-page / petit multi-page), heberges ou servis localement, pour produire des **captures d'ecran** (desktop, tablette, mobile) et enrichir le portfolio DanielCraft avec des visuels credibles par **vertical metier**.

**Verticales cibles (exemples)** :

| Secteur          | Notes rapides                                    |
|------------------|--------------------------------------------------|
| Chocolatier      | ambiance artisan, produits, boutique / click     |
| Odontologie      | cabinet dentaire, prise de RDV, confiance sante  |
| Banque / finance | institutionnel, sobriete, conformite visuelle    |
| Industrie        | B2B, securite, process, machines / qualite       |
| Comptable        | expertise, conformite, PME, call-to-action clair |
| Association      | mission, dons, benevolat, evenements             |

**Contraintes** :

- **Fiction** : noms d'entreprise, logos et textes **inventes** ou clairement generiques ; ne pas copier des sites reels ni des marques deposees.
- **Coherence** : chaque demo a sa charte (couleurs, typo, ton) alignee secteur.
- **Captures** : prevoir viewports typiques (ex. ~1920x1080, ~768x1024, ~390x844) ; pipeline a documenter dans la branche dediee.

**Implementation actuelle** : dossier **`showcase/`** a la racine (hub `showcase/index.html` + un sous-dossier par secteur, CSS dediee, `shared/reset.css`).

**Pistes techniques** (nginx / prod) :

- Servir ce dossier en statique (sous-chemin ou sous-domaines sur `node12.lan`).
- Ou depot / repertoire separe deploye a cote du site principal, lie depuis le portfolio par image + legende « demo concept ».

Branche de travail historique pour cette idee : **`feature/portfolio-demo-showcases`**.

## Livres de formation

Dossier **`livres-formation/`** : livres PDF (informatique, commerce, marketing, communication), plusieurs dizaines de pages, langage simple, PDF dans `pdf/`, prompts images/schemas dans `prompts/`.

**Directive de style (obligatoire)** : voir `livres-formation/DIRECTIVES.md` (alignee avec la section Style ci-dessus : ton humain, apostrophes `'`, tirets `-`).

**Methode** : voir `livres-formation/METHODE.md`. Auteur : **DanielCraft**.

Moteur partage : `livres-formation/_book_lib.py`. Chaque chapitre commence sur une **nouvelle page**. Sommaire avec chapitres **et** sous-chapitres cliquables.

## Images produit (prestations)

- Prompts : `assets/images/maquettes/prestations/PROMPTS-IMAGES.md`
- Cibles : `assets/images/prestations/cards/<slug>.jpg` et `categories/<id>.jpg` (+ WebP via le builder)
- Install : `python scripts/install_prestation_product_images.py`
- Pointer `image` dans `prestations.json` vers le JPG (pas SVG) pour activer le hero fiche

## Regles pour les agents

- Modifier le minimum necessaire ; respecter le style existant (HTML, CSS, JS, Python).
- Ne pas committer de secrets (`.env`, credentials).
- Apres changements structurels, lancer le build localement si pertinent (`python build.py` ou `python build.py --no-webp`).
- Pour tout contenu dans `livres-formation/`, appliquer `DIRECTIVES.md` et `METHODE.md`.
- Auteur PDF / metadonnees des livres : **DanielCraft**.
