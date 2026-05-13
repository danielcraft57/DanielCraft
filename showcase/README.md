# Vitrines fictives (portfolio)

Sites statiques **100 % fictifs** pour captures d’écran (desktop, tablette, mobile). Aucune marque réelle.

## Prévisualisation locale

À la racine du dépôt :

```bash
cd showcase
python -m http.server 8765
```

Puis ouvrir `http://127.0.0.1:8765/`.

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
