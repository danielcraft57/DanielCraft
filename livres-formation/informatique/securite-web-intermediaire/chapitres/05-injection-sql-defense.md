# Injection SQL : requetes preparees

Une **injection SQL** arrive quand du texte utilisateur est concatene dans une requete SQL.

```sql
-- Dangereux
SELECT * FROM users WHERE email = '" + input + "'
```

## Defense

**Requetes preparees** (prepared statements) : le SQL et les donnees sont separes.

```python
cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
```

## Regles

- Jamais concatener l'input utilisateur dans du SQL.
- Moindre privilege sur le compte DB.
- Valider le format des entrees (email, id numerique).

## A retenir

- Prepared statements = regle d'or.
- Valider + moindre privilege DB.
