---
title: "Cybersécurité : menaces, risques et posture (les bases)"
date: 2025-11-04
excerpt: "Comprendre les menaces modernes (phishing, ransomware, supply chain), la notion de risque, et les contrôles de base pour bâtir une posture sécurité réaliste."
type: article
tags: [cybersécurité, risques, menaces, SecOps, sécurité]
series: cybersecurite-secops-serie
series_order: 1
og_image: cybersecurite-fondamentaux-menaces-risques-1200x630.jpg
---

# Cybersécurité : menaces, risques et posture (les bases)

La cybersécurité n’est pas un produit à acheter, c’est une **posture** : des décisions, des contrôles, et un fonctionnement quotidien.  
Cet article pose le vocabulaire et les idées qui évitent de partir dans tous les sens.

---

## 1) Menace, vulnérabilité, risque : clarifier

- **Menace** : ce qui peut te nuire (attaquant, malware, erreur humaine, panne).
- **Vulnérabilité** : une faiblesse exploitable (bug, config, mot de passe faible).
- **Risque** : probabilité × impact dans **ton** contexte.

Deux entreprises peuvent avoir la même vulnérabilité… et un risque très différent.

---

## 2) Les attaques les plus fréquentes en vrai

### Phishing & vol d’identifiants
Toujours numéro 1 : on cible les humains, pas les firewalls.

### Ransomware
Souvent précédé par :
- vol de creds
- mouvement latéral
- exfiltration (“double extorsion”)

### Supply chain
Tu te fais impacter par un fournisseur, une dépendance, une CI compromise.

### Exposition accidentelle
Bucket public, clé API pushée, port admin ouvert… les classiques.

---

## 3) Les contrôles “80/20” (ce qui réduit vraiment le risque)

Si tu veux des gains rapides :

- **MFA partout** (mail, VPN, consoles cloud, admin)
- **gestion des accès** (least privilege, comptes séparés, revues)
- **patching** régulier (OS, packages, dépendances)
- **backups testés** (et protégés) + plan de restauration
- **journalisation** centralisée (logs) + alertes
- **segmentation** (réseau, environnements)

Tu peux être “moyen” sur le reste et déjà éviter beaucoup de dégâts.

---

## 4) La posture : prévention, détection, réponse

Pense en 3 boucles :

1. **Prévenir** : réduire surface d’attaque
2. **Détecter** : repérer vite l’anormal
3. **Répondre** : contenir, éradiquer, restaurer

Une sécurité “pro” n’est pas celle qui promet “zéro incident”, c’est celle qui **réagit vite**.

---

## 5) Mesurer sans se mentir

Quelques métriques utiles :

- % comptes critiques avec MFA
- temps moyen de patch (MTTP)
- temps de détection (MTTD) et de remédiation (MTTR)
- couverture logs (quels systèmes envoient des logs ?)
- fréquence de restauration réussie (tests backup)

---

## Conclusion

Avant SOC, SIEM, EDR et tout le reste, il faut :

- clarifier ton **risque**
- mettre les contrôles **fondamentaux**
- organiser prévention / détection / réponse

La suite de la série rentre dans le concret SecOps et SOC.

