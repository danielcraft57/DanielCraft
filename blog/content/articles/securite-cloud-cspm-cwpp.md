---
title: "Sécurité cloud : CSPM, CWPP et erreurs de configuration"
date: 2025-11-27
excerpt: "Dans le cloud, la majorité des incidents viennent de la config : IAM, stockage public, clés. CSPM/CWPP expliqués et checklist pragmatique."
type: article
tags: [cloud, CSPM, CWPP, sécurité, DevSecOps]
series: cybersecurite-secops-serie
series_order: 8
og_image: securite-cloud-cspm-cwpp-1200x630.jpg
---

# Sécurité cloud : CSPM, CWPP et erreurs de configuration

Le cloud ne rend pas “automatiquement” plus sécurisé.  
Il rend les changements plus rapides… donc les erreurs plus fréquentes si tu n’as pas de garde‑fous.

La bonne nouvelle : les contrôles cloud les plus efficaces sont souvent des **contrôles de configuration**.

---

## 1) Shared responsibility : ne pas se tromper de niveau

Le fournisseur sécurise :
- le datacenter
- l’hyperviseur
- certains services managés

Toi, tu sécurises :
- IAM, clés, secrets
- données
- configuration réseau
- workloads (VM, conteneurs)
- logs et monitoring

---

## 2) CSPM vs CWPP (simple)

- **CSPM** (Cloud Security Posture Management) :
  - détection de mauvaises configurations cloud (bucket public, IAM trop large)
  - conformité et posture

- **CWPP** (Cloud Workload Protection Platform) :
  - protection des workloads (VM/containers) : runtime, vulnérabilités, comportements

En pratique, beaucoup d’outils fusionnent les deux.

---

## 3) Les erreurs cloud les plus fréquentes

- IAM trop permissif (admin partout)
- stockage public involontaire (S3, blobs)
- clés API dans le code / CI
- egress non contrôlé (exfiltration facile)
- logs non activés (pas de preuves)

---

## 4) Checklist posture cloud “80/20”

1. MFA + rôles least privilege + revues
2. logs d’audit activés (API calls) + centralisation
3. chiffrement par défaut (at-rest + in-transit)
4. blocage du stockage public par policy
5. segmentation réseau (subnets, security groups)
6. rotation clés + secrets manager
7. scanning images + dépendances

---

## 5) Détection cloud utile

Alertes SOC cloud :

- création clé API
- désactivation logs
- changement IAM admin
- bucket rendu public
- accès “impossible travel”
- spikes d’egress

---

## Conclusion

Dans le cloud, la sécurité se gagne par :

- politiques (guardrails)
- IAM solide
- logs + détection

Prochain article : DevSecOps (SAST/DAST/SBOM).

