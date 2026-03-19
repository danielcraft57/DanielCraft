---
title: "SIEM : logs, corrélation et détection (sans se noyer)"
date: 2025-11-11
excerpt: "Centraliser les logs, définir une stratégie de rétention, créer des règles de détection utiles et réduire les faux positifs : le SIEM expliqué simplement."
type: article
tags: [SIEM, logs, détection, SecOps, SOC]
series: cybersecurite-secops-serie
series_order: 3
og_image: siem-log-management-detection-1200x630.jpg
---

# SIEM : logs, corrélation et détection (sans se noyer)

Un SIEM (Security Information and Event Management) sert à **collecter**, **normaliser** et **corréler** des événements pour détecter des comportements suspects.  
Le piège : tout logguer sans stratégie → facture énorme, bruit, fatigue.

---

## 1) Les logs utiles (par ordre de priorité)

Commence par ce qui aide vraiment à enquêter :

- **Identités** : authentification, MFA, échecs, élévations de privilèges
- **Endpoints** : exécution de process, persistance, antivirus/EDR
- **Réseau** : DNS, proxy, egress, flux vers l’extérieur
- **Cloud** : API calls, changements IAM, stockage public, clés
- **Applications** : erreurs auth, actions admin, opérations sensibles

Si tu dois choisir, choisis ce qui prouve “qui a fait quoi”.

---

## 2) Rétention : court vs long

Deux niveaux pratiques :

- **Hot** (rapide, cher) : 7–30 jours pour investiguer vite
- **Cold** (moins cher) : 90–365 jours pour remonter une attaque lente

Et surtout : indexe ce qui est interrogé, archive le reste.

---

## 3) Normalisation et contexte

Un log “brut” a peu de valeur.  
Ajoute du contexte :

- asset criticality (serveur prod vs poste dev)
- user role (admin vs user standard)
- géoloc/ASN
- tags (prod/dev)

Une alerte “échec login” devient utile si tu sais : *admin prod depuis un pays inattendu*.

---

## 4) Détections : règles simples d’abord

Les règles les plus rentables :

- brute force + succès
- login impossible travel
- création de clé API
- changement IAM / ajout admin
- exécution d’outils connus (rmm, powershell encodé)
- upload massif / exfil

Tu veux des alertes actionnables, pas des “bruits”.

---

## 5) Faux positifs : la vraie bataille

Réduire les faux positifs :

- whitelists contrôlées (sans ouvrir trop large)
- seuils (rate) adaptés
- enrichissement (contexte)
- suppression des signaux inutiles

Chaque faux positif non traité est une dette : il réduit la vigilance future.

---

## 6) Coverage : savoir ce que tu ne vois pas

Même un SIEM “plein” a des angles morts.

Maintiens :

- une carte des sources (qu’est-ce qui envoie ?)
- une liste des “high value assets” (priorité)
- une revue trimestrielle de coverage

---

## Conclusion

Un SIEM utile = stratégie + contexte + détections actionnables.  
Prochain article : EDR/XDR côté endpoints.

