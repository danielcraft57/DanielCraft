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
- Tirets simples uniquement : `-` (pas de tirets cadratins)

### Orthographe et grammaire

- Accents obligatoires sur le contenu visible (pas de francais « sans accents »)
- Accords et conjugaisons corrects ; le ton oral (`t'es`, `y'a`) n'excuse pas une faute
- Avant de livrer du copy : relire les fichiers touches (voir aussi `.cursorrules`)

### Portee

S'applique au contenu visible et SEO des pages (`src/pages/`, includes de texte, `src/data/*.json` descriptifs, articles blog). Pas aux commentaires techniques de code ni aux logs de build.

### Ton Grand Est (argot populaire d'abord)

Le site parle aux commerces du **Grand Est**. On colore le francais avec un **argot local courant** - celui qu'on entend au magasin, au marche, entre voisins - pas un lexique dialectal rare.

**Priorite vocabulaire (obligatoire)** :
1. **Argot / regionalismes populaires** (connus hors du cercle des passionnes de patois) - c'est la base du site.
2. **Grammaire et accents** (elisions orales, cadence lorraine) - **actif** apres le vocabulaire. Voir sous-section « Grammaire et accents ». Ne pas phonetiser le texte pour « faire local ».
3. **Dialectal rare / platt / interjections mosellanes** - hors pages marketing. Reserve aux demos fiction, blog anecdotique, ou oral imite - jamais en hero, CTA, FAQ client.

**Dosage** : 1 touche locale de temps en temps (hero lead, bio, CTA soft, blog) - pas un mot regional par phrase. Le client doit comprendre du premier coup, meme s'il n'est pas de Metz.

**Vocabulaire OK (populaire, a privilegier)** :

| Dire | Sens / usage | Ou l'utiliser |
|------|----------------|---------------|
| `entre midi` | entre 12 h et 14 h (pas « a midi ») | bio, contact, CTA soft |
| `nareux` / `nareuse` / `faire le nareux` | difficile sur la bouffe / le propre ; au figure : tatillon sans raison | devis, prix, FAQ |
| `clanche` / `clancher` | poignee / ouvrir-fermer la porte | image, blog, demo artisan |
| `cornet` | sac plastique (marche, courses) | echantillons, metaphore « gouter avant » |
| `ca tire` | il y a un courant d'air | humour leger, blog, anecdote |
| `comment qu'c'est ?` | comment ca va ? | oral imite, jamais en H1 froid |
| `gros` | mec / l'ami (« a plus, gros ») | tres leger, fin de phrase orale |
| `une paire de` | plusieurs (« une paire d'actions ») | audit, livrables, FAQ |
| `viens avec` | viens avec nous / moi (sans « moi ») | CTA doux contact |
| `guette voir` | regarde / fais attention | variante de « regarde voir » |
| `dis voir` / `regarde voir` | dis-moi / regarde (imperatif + voir) | CTA, titres section |
| `couatcher` | papoter, discuter tranquillement | bio, contact, process |
| `chtuque` | un morceau (« un chtuque d'aide ») | dosage rare, FAQ / about |
| `attendre sur` | attendre quelqu'un (« j'attends sur toi ») | contact, delais - 1 fois max |
| `ca caille` / `ca pele` | il fait tres froid | blog / anecdote saison, pas hero |
| `faire bleu` | secher / zappe | humour leger seulement, pas promesse |
| `au magasin` / `a la boutique` | ancrage commerce local | bio, contact |
| `sur le terrain` | en vrai, chez les clients | trust, about |
| `demeler` | clarifier un vrai probleme | CTA, FAQ |
| article + prenom | « le Loic », « la Marie » | about, blog |
| Metz | a l'ecrit **toujours Metz** (pas « Mess ») | partout |

**Vocabulaire a eviter sur le site** (trop rare, trop platt, ou trop « lexique souvenir ») :

| Dire | Pourquoi |
|------|----------|
| `ca geths` / `ca geths sa moal` | platt / peu lisible hors Moselle |
| `schlappe`, `schneck`, `schlouk`, `shmer` | germanismes locaux - OK en demo fiction, pas en marketing DanielCraft |
| `chawée`, `prendre une rincee`, `broussiner` | meteo anecdotique - pas pour un CTA |
| `couarail`, `bassoter`, `beugner`, `trisser`, `chpritser` | peu connus hors region / hors generation |
| `fratz`, `boulimatche`, `staarf`, `petchave`, `zaubette` | trop argot rue / peu lisible |
| `Ach jo`, `oye`, `oh leck`, `oh ye`, `vi` / `ui`, `veck` | interjections orales - pas sur une page web |
| `cheuler`, `chouille`, `goutte` (eau-de-vie) | mots de soif - jamais en hero/CTA |
| `daron`, `schlinguer`, `grailler`, etc. | argot parisien ou generique deguise en local |
| `souffler la lumiere`, `flot` (noeud) | trop domestique / peu utile en marketing web |
| phonetique type `j'mopel` | illisible ; voir section Grammaire - accents a l'oral seulement |

**Grand Est au sens large** : parler des villes (Nancy, Epinal, Strasbourg, Thionville…) sans jargon alsacien ; ne pas confondre Lorraine et Alsace. Positionnement marketing = **Grand Est** ; ancrage perso Loic = Metz + terrain (Nancy, Epinal, Strasbourg). Touches culture OK en leger : mirabelle, marche, boutique - sans en faire un cliche.

**Exemples de ton** :
- « On peut se parler entre midi si t'es au magasin. »
- « Pas la peine de faire le nareux avec le devis : prix affiche, PDF direct. »
- « Dis voir ce qui bloque - on demele ca ensemble. »
- « Comme au marche : tu goutes avant de remplir le cornet. »
- « Viens avec ton besoin - on en parle. »
- « Tu repars avec une paire d'actions concretes - pas un roman. »
- « On peut juste couatcher 10 minutes pour cadrer. »
- « Guette voir les echantillons avant de te lancer. »
- « J'attends pas sur un miracle : brief clair, on avance. »

Sources d'inspiration (lexique courant, pas a copier tel quel) : parler lorrain quotidien (entre midi, nareux, clanche, cornet, gros, une paire de, viens avec, attendre sur), pas les listes folklore / platt.

### Grammaire et accents (2e temps - actif)

Le vocabulaire pose la couleur. La **grammaire** donne la cadence orale. Les **accents** (prononciation Moselle / Lorraine) restent **a l'oral** (visio, telephone, video) - **jamais** recopies en phonetique sur le site.

**Principe** : francais standard lisible + tournures locales. Le client doit pouvoir lire a voix haute sans buter.

#### A faire (ecrit web)

| Tour | Exemple | Note |
|------|---------|------|
| Tutoiement client | « ton site », « tu veux » | pages commerce / contact / FAQ / audit |
| Phrases courtes | « Brief clair. On avance. » | 1 idee par phrase quand c'est possible |
| Pause orale avec `-` | « Dis voir - on demele ca. » | tiret simple, pas cadratin |
| Elisions lisibles | `t'es`, `t'as`, `c'est`, `y'a` | OK ; garder l'apostrophe droite `'` |
| Negation orale legere | « j'attends pas sur… » | 1 fois de temps en temps, pas partout |
| Imperatif + `voir` | « dis voir », « regarde voir », « guette voir » | deja au lexique |
| `viens avec` (sans « moi ») | « Viens avec ton besoin » | calque local courant |
| `attendre sur` | « j'attends sur toi » | 1 fois max par page |
| Article + prenom | « le Loic » | about / blog, pas en H1 froid |
| Relance douce | « en vrai », « bon », « voila » | dosage rare, jamais en meta SEO |

#### A ne pas faire (ecrit web)

| Eviter | Pourquoi |
|--------|----------|
| Phonetique (`Mess`, `j'mopel`, `chuis`, `kekchose`) | illisible, faux local |
| Recoller l'accent (`vingt` avec T force a l'ecrit, `oeuf`/`boeuf`) | ca s'entend a l'oral, ca ne s'ecrit pas |
| Enlever tous les `ne` / ecrire en SMS | fatigue a la lecture, ton pas pro |
| Enchainer 3 tournures locales dans la meme phrase | surcharge ; 1 touche suffit |
| Tutoyer + vouvoyer dans le meme bloc | choisir **tu** sur le parcours client |
| `comment qu'c'est` en titre H1 | trop oral pour un hero |

#### Accents (oral seulement - note agents)

A Metz / Moselle a l'oral : on entend souvent **Mess**, le **t** de *vingt*, parfois *oeuf* / *boeuf* avec le **f**. Sur le site : orthographe francaise normale (**Metz**, *vingt*, *oeufs*). Si un script video / podcast : respecter l'oral local sans le forcer a l'ecran.

**Exemples de cadence** (grammaire, pas jargon) :
- « T'es au magasin entre midi ? On peut en parler. »
- « J'attends pas sur un miracle. Brief clair, on avance. »
- « Viens avec ce qui bloque - on demele ca. »
- « En vrai, trois pages bien faites battent un site a rallonge. »

### Public client (prioritaire)

Les clients (commerces, artisans, independants du Grand Est) **ne sont pas informaticiens**. Ils n'ont pas a comprendre le jargon.

Quand tu rediges pour le site (accueil, fiches, audit, contact, FAQ, SEO grand public) :
- **Interdit** (sauf blog tech / livres / page pro explicite) : CMS, SSR, Lighthouse, framework, TypeScript, Astro, Next, API, DevOps, CI/CD, refactoring, etc.
- **Preferer** : numero et horaires visibles sur telephone, bouton appeler en un clic, trouve sur Google, devis simple, livraison en jours, un seul interlocuteur, bien protege / suivi apres mise en ligne.
- **Eviter** les formulations vagues (`clair sur telephone`, `responsive`, `optimise`) - voir `src/data/vocabulaire-client.json` et MCP `docs/MCP_VOCABULAIRE.md`.
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
| `/#contact` / wizard | Premier contact client ; delais courts, un interlocuteur qui maitrise le process |
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
- Au client commerce : benefices concrets d'abord (numero et horaires visibles sur telephone, trouve sur Google, ca charge vite).

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
3. Brancher dans `src/pages/index.html` (hero + `#about`) ; ancre contact = titre « Parlons de votre besoin » (`#contact`)
4. `python build.py index contact` (+ sync `dist/assets`)

Schema : `itemprop="image"` / `link` vers `loic-about-ingenieur.png`.

## Projet

- **DanielCraft** : site portfolio / commerce local (Metz), build Python (`build.py`), templates dans `src/`, assets dans `assets/`, sortie `dist/`.
- **Accueil** : `src/pages/index.html` (+ CSS/JS home).
- **Catalogue offres** : `/nos-offres` (`prestations.json`, hub categories, fiches `/prestations/<slug>/`).
- **Livres** : `/bouquins` (redirect `/livres`) + dossier source `livres-formation/`.
- **Echantillons** : `/echantillons` (exemples de sites par metier, **pas a vendre**). Anciennes URLs `/vitrines/` et `/devantures/` redirigent. Catalogue `src/data/vitrines.json`.
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
