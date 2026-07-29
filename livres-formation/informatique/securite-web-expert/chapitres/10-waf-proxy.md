# WAF, reverse proxy et edge

Le **WAF** (Web Application Firewall) filtre le trafic HTTP avant qu'il n'atteigne ton app.

## Couches

```text
Internet -> CDN/WAF -> Load balancer -> App -> BDD
```

## Ce que le WAF peut bloquer

- Signatures SQLi/XSS connues.
- Bots et scans automatises.
- Geo-blocking si pertinent.

## Limites

- Faux positifs sur API JSON.
- Regles custom pour ton metier.
- Le WAF **complete** le code, ne le remplace pas.

> **Astuce DanielCraft** - Mode detection d'abord, blocage apres tuning.

## A retenir

- WAF = filtre edge, pas substitute au code securise.
- TLS termine au proxy avec config moderne.
