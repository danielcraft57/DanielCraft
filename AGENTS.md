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
