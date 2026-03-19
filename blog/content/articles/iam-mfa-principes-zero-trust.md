---
title: "IAM, MFA et Zero Trust : contrôler les accès sans freiner"
date: 2025-11-20
excerpt: "Least privilege, MFA, comptes admin séparés, sessions courtes : les bases d’un IAM solide et une approche Zero Trust pragmatique."
type: article
tags: [IAM, MFA, Zero Trust, accès, sécurité]
series: cybersecurite-secops-serie
series_order: 6
og_image: iam-mfa-principes-zero-trust-1200x630.jpg
---

# IAM, MFA et Zero Trust : contrôler les accès sans freiner

La majorité des incidents commencent par un accès : identifiants volés, token compromis, session trop longue, privilèges excessifs.  
Une bonne stratégie IAM réduit drastiquement le risque, souvent avec peu de complexité.

---

## 1) Principes incontournables

- **Least privilege** : donner le minimum nécessaire
- **Séparation des rôles** : user standard ≠ admin
- **Traçabilité** : qui a fait quoi, quand
- **Revue d’accès** : retirer ce qui n’est plus utile

---

## 2) MFA : là où c’est non négociable

MFA obligatoire sur :

- mail
- consoles cloud
- VPN / accès distant
- outils dev (GitHub, CI/CD)
- comptes admin

Et privilégier :

- authenticator / passkeys
- éviter SMS quand possible (SIM swap)

---

## 3) Comptes admin : éviter la catastrophe silencieuse

Bon pattern :

- compte standard pour le quotidien
- compte admin séparé, utilisé uniquement quand nécessaire
- sessions courtes / élévation temporaire (JIT)

Un admin permanent, c’est un incident en attente.

---

## 4) Zero Trust : la version pragmatique

Zero Trust n’est pas “plus de sécurité partout”.  
C’est :

- ne pas faire confiance par défaut (même interne)
- vérifier l’identité et le contexte
- limiter le blast radius

Concrètement :

- segmentation réseau
- contrôle d’accès conditionnel (device, lieu, risque)
- tokens courts + rotation

---

## 5) Signaux à surveiller

Dans un SOC, les alertes IAM clés :

- ajout d’un rôle admin
- création de clé API
- login depuis pays/ASN atypique
- MFA désactivé
- changements massifs de permissions

---

## Conclusion

IAM + MFA + séparation admin = l’un des meilleurs ROI en cybersécurité.  
Prochain article : répondre à un incident (runbook, post‑mortem).

