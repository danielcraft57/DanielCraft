# Upload de fichiers : securiser

Un upload mal gere = execution de code ou fuite de donnees.

## Regles

1. **Renommer** les fichiers (UUID), jamais le nom utilisateur.
2. **Verifier le type** : magic bytes, pas seulement l'extension.
3. **Stocker hors webroot** ou servir via CDN sans execution.
4. **Limiter taille** et nombre par utilisateur.
5. **Antivirus** optionnel sur fichiers sensibles.

```python
ALLOWED = {"image/jpeg", "image/png", "application/pdf"}
if mime not in ALLOWED:
    raise ValidationError("Type non autorise")
```

## A retenir

- Extension `.jpg` ne garantit rien : verifier le contenu.
- Jamais d'upload executable dans un dossier servi par le web server.
