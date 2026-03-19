---
title: "EDR / XDR : détection et réponse sur les endpoints"
date: 2025-11-13
excerpt: "EDR, XDR, antivirus “next-gen” : ce que ça fait réellement, comment le déployer, et quels signaux/alertes sont les plus utiles en SOC."
type: article
tags: [EDR, XDR, endpoint, SOC, SecOps]
series: cybersecurite-secops-serie
series_order: 4
og_image: edr-xdr-endpoint-detection-response-1200x630.jpg
---

# EDR / XDR : détection et réponse sur les endpoints

L’EDR (Endpoint Detection & Response) est l’un des outils les plus efficaces en SecOps, parce qu’il se place là où l’attaque se déroule souvent : **les postes et serveurs**.

Mais un EDR n’est pas une baguette magique : il faut savoir quoi en attendre, comment le déployer et comment l’opérer.

---

## 1) Antivirus vs EDR (et pourquoi ça ne suffit plus)

- Antivirus classique : basé sur signatures, efficace contre le “connu”.
- EDR : collecte de télémétrie (process, réseau, persistance) + détections comportementales + réponse (isoler, tuer un process, quarantaine).

Un ransomware “moderne” est souvent détecté par comportement (chiffrement massif, outils admin détournés), pas par signature.

---

## 2) XDR : élargir la corrélation

XDR (Extended Detection & Response) corrèle :

- endpoints
- identité
- email
- réseau
- cloud

En pratique, XDR est intéressant si tu peux :

- lier un phishing → login anormal → exécution malware → exfiltration

Sinon, tu fais du “multi‑outil” sans vision globale.

---

## 3) Déploiement : les pièges

Pièges classiques :

- agents pas partout (angles morts)
- exclusions trop larges (“ça casse une app”)
- pas de gestion des serveurs (prod) vs postes (users)
- pas de plan de réponse (on détecte, mais on ne sait pas quoi faire)

Bon début :

- couvrir d’abord les actifs critiques
- définir un “baseline” (ce qui est normal)
- documenter 5 actions de réponse (isolation, kill, rollback, collecte)

---

## 4) Les alertes les plus utiles

Les signaux “haute valeur” :

- exécution PowerShell encodée / suspicious command line
- création de persistance (registry run keys, services)
- dump credentials (LSASS)
- tools LOLBins (living off the land)
- connexions sortantes anormales

Et surtout : **corréler avec identité** (qui, d’où, quand).

---

## 5) Réponse : containment d’abord

Lors d’un incident, l’EDR sert à :

- isoler l’hôte
- stopper un process
- bloquer une signature/IOC
- collecter les artefacts

La règle : contenir avant d’“éradiquer”, sinon tu perds des preuves et tu déclenches l’attaquant.

---

## Conclusion

EDR/XDR est un levier énorme pour la détection/réponse, mais il doit être :

- bien déployé (coverage)
- bien opéré (triage, runbooks)
- bien corrélé (identité, réseau, cloud)

Prochain : vulnérabilités, CVE et patching.

