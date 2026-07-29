# Zero trust : ne jamais faire confiance par defaut

**Zero trust** : chaque requete est verifiee, meme a l'interieur du reseau.

## Principes

1. **Verifier explicitement** : auth + authz a chaque appel.
2. **Moindre privilege** : acces minimal, duree limitee.
3. **Supposer la compromission** : segmenter, chiffrer, monitorer.

## En pratique web

- mTLS entre microservices.
- JWT scopes fins par endpoint.
- Pas de confiance implicite au VPN seul.

```text
Utilisateur -> API Gateway (auth) -> Service A (authz) -> BDD (role restreint)
```

## A retenir

- Zero trust = verifier partout, tout le temps.
- Le reseau interne n'est pas un bouclier magique.
