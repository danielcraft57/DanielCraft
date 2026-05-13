# Vitrines fictives (portfolio)

Sites statiques **100 % fictifs** pour captures d’écran (desktop, tablette, mobile). Aucune marque réelle.

## Images

Les fichiers `showcase/*/images/*.png` sont des **visuels générés** (ambiance photographique) pour la démo ; **aucune** entreprise réelle n’est représentée.

## Design (références)

- **Material Design 3** : surfaces tonales, formes (coins), élévation, typo **Roboto**, courbes de mouvement — [m3.material.io/styles](https://m3.material.io/styles).
- **UX « sites primés »** : hiérarchie typographique claire, cartes avec élévation et survol discret, en-têtes sticky où pertinent, `prefers-reduced-motion`, focus visible.

Fichiers partagés : `shared/reset.css`, `shared/tokens.css` (jetons M3). Hub : `hub.css`.

## Prévisualisation locale (recommandé)

À la **racine du dépôt** — sert le dossier `showcase/` et **ouvre le navigateur** sur le hub :

```bash
python showcase/serve_showcase.py
```

Options :

```bash
python showcase/serve_showcase.py --port 9000 --no-browser
python showcase/serve_showcase.py --host 0.0.0.0
```

Sous **Windows** (PowerShell), depuis la racine :

```powershell
.\scripts\serve_showcase.ps1
.\scripts\serve_showcase.ps1 -Port 9000 -NoBrowser
```

Alternative sans script : `cd showcase` puis `python -m http.server 8765`, puis ouvrir `http://127.0.0.1:8765/` (aucune ouverture auto du navigateur).

## Déploiement (nginx)

Copier le dossier `showcase/` sur le serveur (ex. `/var/www/showcase-demos/`) et exposer ce répertoire comme racine ou sous-chemin (`location /showcase/ { alias ...; }`). Les liens du hub utilisent des chemins relatifs par dossier.

## Structure

| Dossier        | Secteur     |
|----------------|-------------|
| `chocolatier/` | Artisanat   |
| `odontologie/` | Santé bucco |
| `banque/`      | Finance     |
| `industrie/`   | B2B / usine |
| `comptable/`   | Expertise   |
| `association/` | ESS         |
