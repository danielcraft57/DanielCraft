---
title: "Incident Response : runbooks, containment et post‑mortem"
date: 2025-11-25
excerpt: "Que faire quand ça arrive : triage, containment, éradication, restauration, communication, et un post‑mortem utile. Un guide concret pour éviter le chaos."
type: article
tags: [incident response, SOC, SecOps, runbook, post-mortem]
series: cybersecurite-secops-serie
series_order: 7
og_image: incident-response-runbook-postmortem-1200x630.jpg
---

# Incident Response : runbooks, containment et post‑mortem

Un incident sécurité est une situation “haute pression”.  
Sans préparation, tu perds du temps, tu prends de mauvaises décisions, et tu empirés l’impact.

L’objectif : une réponse structurée, même avec une petite équipe.

---

## 1) Les phases (à garder en tête)

1. **Triage** : est‑ce réel ? quelle sévérité ?
2. **Containment** : empêcher la propagation
3. **Éradication** : supprimer la cause (malware, compte compromis)
4. **Restauration** : remettre en service propre
5. **Amélioration** : post‑mortem + actions

Le containment vient avant l’éradication : tu stabilises d’abord.

---

## 2) Le runbook minimal (une page)

Un bon runbook contient :

- qui contacter (IT, produit, légal, com)
- comment ouvrir l’incident (canal + doc)
- quoi collecter (logs, EDR, snapshots)
- actions de containment (isoler, reset creds, bloquer egress)
- critères de retour à la normale

Il doit être utilisable à 3h du matin.

---

## 3) Containment : exemples concrets

Selon le cas :

- isoler un endpoint via EDR
- désactiver un compte + reset tokens
- couper l’egress vers un domaine/ASN
- bloquer un binaire hash/IOC
- segmentation temporaire

But : réduire le blast radius rapidement.

---

## 4) Communication : éviter le chaos

Règles simples :

- un incident commander (1 décideur)
- une timeline (qui fait quoi quand)
- des updates réguliers (toutes les 30–60 min)
- pas de spéculation (seulement des faits)

Et si données personnelles : penser RGPD (notification potentielle).

---

## 5) Post‑mortem : utile, pas politique

Un post‑mortem utile :

- décrit la cause racine (technique + organisation)
- liste les actions avec owner + date
- identifie les détections manquantes
- réduit la probabilité de récidive

Sans action, le post‑mortem est un récit. Avec action, c’est une amélioration.

---

## Conclusion

La différence entre une entreprise “mature” et “fragile” n’est pas l’absence d’incidents, mais la capacité à **répondre vite et proprement**.

Prochain article : sécurité cloud (CSPM/CWPP).

