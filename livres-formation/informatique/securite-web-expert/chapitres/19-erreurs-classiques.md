# Erreurs classiques niveau expert

Meme les seniors tombent dans ces pieges.

| Erreur | Pourquoi c'est grave | Fix |
|--------|---------------------|-----|
| Confiance au VPN seul | Lateral movement interne | Zero trust |
| WAF sans tuning | Faux sentiment ou blocages | Detection puis blocage |
| Secrets dans K8s YAML Git | Fuite permanente | Vault + sealed secrets |
| Ignorer supply chain | Compromission transitive | Lockfile + audit CI |
| Pas de runbook incident | Panique, delai x10 | Documenter maintenant |

> **Piege** - « On fera la securite en v2 » : la v2 n'arrive jamais avant la breach.

## A retenir

- Expert = eviter les raccourcis organisationnels.
