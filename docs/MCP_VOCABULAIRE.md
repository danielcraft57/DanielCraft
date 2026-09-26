# MCP vocabulaire client DanielCraft

Serveur MCP local pour verifier et proposer le bon vocabulaire sur les pages commerce (accueil, offres, fiches, FAQ).

## Source de verite

- Lexique JSON : `src/data/vocabulaire-client.json`
- Regles ton Grand Est : `AGENTS.md` + `.cursor/rules/pages-ton-humain.mdc`

## Outils exposes

| Outil | Role |
|-------|------|
| `check_copy` | Detecte les formulations interdites ou trop vagues dans un texte |
| `get_alternatives` | Propose des remplacements pour une phrase problematique |
| `list_benefits` | Liste les formulations benefice par categorie |
| `list_banned` | Liste tout ce qu'il faut eviter cote client |
| `get_zone_guidance` | Conseils pour hero, lead, checklist, etc. |

## Installation

```powershell
cd mcp/vocabulaire
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Activer dans Cursor

Ajouter dans `.cursor/mcp.json` (projet) ou les reglages MCP utilisateur :

```json
{
  "mcpServers": {
    "danielcraft-vocabulaire": {
      "command": "python",
      "args": ["mcp/vocabulaire/server.py"],
      "cwd": "C:/Users/loicDaniel/Documents/DanielCraft/DanielCraftFr"
    }
  }
}
```

Adapter `cwd` si le depot est ailleurs. Avec venv :

```json
{
  "mcpServers": {
    "danielcraft-vocabulaire": {
      "command": "C:/Users/loicDaniel/Documents/DanielCraft/DanielCraftFr/mcp/vocabulaire/.venv/Scripts/python.exe",
      "args": ["C:/Users/loicDaniel/Documents/DanielCraft/DanielCraftFr/mcp/vocabulaire/server.py"]
    }
  }
}
```

Redemarrer Cursor apres ajout.

## Exemples d'usage agent

- Avant de rediger l'accueil : `get_zone_guidance("hero_h1")`
- Apres un brouillon : `check_copy("Un site clair sur telephone pour artisans")`
- Remplacement rapide : `get_alternatives("clair sur telephone")`

## Etendre le lexique

Editer `src/data/vocabulaire-client.json` :

1. Ajouter une entree dans `interdit` (phrase, variantes, raison, alternatives)
2. Ou enrichir `benefices` / `zones`
3. Redemarrer le serveur MCP si deja lance

Pas besoin de toucher `server.py` pour du contenu pur.
