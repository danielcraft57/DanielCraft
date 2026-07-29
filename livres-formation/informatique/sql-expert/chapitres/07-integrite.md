# Integrite : contraintes et cles

La base protege les donnees **meme si l'app se trompe**.

## Outils

| Contrainte | Role |
|------------|------|
| PRIMARY KEY | Identite unique |
| FOREIGN KEY | Lien valide vers une autre table |
| UNIQUE | Pas de doublon metier |
| CHECK | Regle simple (`montant > 0`) |
| NOT NULL | Champ obligatoire |

```sql
ALTER TABLE commandes
  ADD CONSTRAINT fk_client
  FOREIGN KEY (client_id) REFERENCES clients(id);
```

## A retenir

- Integrite en base = filet de securite.
- Soft delete et FK : predire le comportement (CASCADE ou non).
