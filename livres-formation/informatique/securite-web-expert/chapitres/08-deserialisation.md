# Deserialisation et injections de gadgets

Deserialiser des donnees **non fiables** (pickle Python, Java ObjectInputStream, PHP unserialize) peut executer du code.

## Defense

- **Eviter** la deserialisation de donnees utilisateur.
- Preferer **JSON** avec schema strict.
- Si obligatoire : bibliotheque durcie, liste blanche de classes.

## Web/API

- Ne pas accepter de blobs binaires opaques sans validation.
- Signer les payloads internes (HMAC) si tu dois transporter des objets.

> **Piege** - `eval()` et `Function()` en JS sont des deserialisations deguisees.

## A retenir

- Deserialisation = execution implicite : treat as code.
- JSON + validation > formats binaires legacy.
