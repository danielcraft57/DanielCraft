---
title: "SecOps & SOC : rôles, processus et fonctionnement"
date: 2025-11-06
excerpt: "SecOps n’est pas qu’un outil. Voici comment organiser un SOC (même petit) : responsabilités, triage, escalade, runbooks, et boucle d’amélioration."
type: article
tags: [SecOps, SOC, incident, détection, opérations]
series: cybersecurite-secops-serie
series_order: 2
og_image: secops-soc-fonctions-process-1200x630.jpg
---

# SecOps & SOC : rôles, processus et fonctionnement

Beaucoup d’entreprises achètent un SIEM ou un EDR et pensent “faire du SecOps”.  
En réalité, SecOps est une **organisation** : qui surveille quoi, comment on priorise, et comment on s’améliore.

---

## 1) SecOps vs SOC : différence

- **SecOps** : la sécurité “en exploitation” (process, outillage, remédiation, hardening).
- **SOC (Security Operations Center)** : la fonction de **détection & réponse** (monitoring, triage, escalade, incident response).

Un SOC peut être interne, externalisé, ou hybride.  
Mais il faut toujours des propriétaires côté entreprise.

---

## 2) Les missions du SOC (en clair)

1. **Collecter** des signaux (logs, événements endpoint, cloud)
2. **Détecter** (règles, corrélations, heuristiques)
3. **Trier** (réduire le bruit, prioriser)
4. **Investiguer** (contexte, timeline, impact)
5. **Répondre** (containment, éradication, restauration)
6. **Améliorer** (retour d’expérience, nouvelles règles, durcissement)

---

## 3) Le triage : l’étape critique

Si le triage est mauvais :

- tu alertes trop (fatigue)
- tu rates les vrais incidents

Bon triage = classifier par :

- **sévérité** (impact métier)
- **confiance** (probabilité que ce soit réel)
- **urgence** (fenêtre d’action)

Le but : décider vite *quoi faire maintenant*.

---

## 4) Processus minimum viable pour un “petit SOC”

Même sans équipe 24/7, tu peux mettre en place :

- une **boîte d’entrée** (tickets) par alerte
- une **priorisation** simple (P1/P2/P3)
- une **astreinte** ou un planning
- des **runbooks** pour 10 cas typiques (phishing, brute force, creds leak, malware, compte admin…)
- un canal de crise (Slack/Teams) + un doc “incident”

Tu passes de “panique” à “réponse organisée”.

---

## 5) Rôles et responsabilités

Un modèle simple :

- **L1** : triage (bruit vs signal)
- **L2** : investigation (corrélations, scope)
- **L3** : expertise (forensics, hunting, tooling)

Et côté IT :

- owners des systèmes (réseau, AD, cloud, apps) pour remédier vite.

Sans “ownership”, le SOC est juste un centre d’alertes.

---

## 6) Les artefacts indispensables

- **Runbooks** (pas des romans : étapes + commandes + contacts)
- **Playbooks** (orchestration / automatisation, si tu as un SOAR)
- **Post‑mortems** (root cause + actions)
- **Catalogues de détection** (quelles règles, quelle couverture)

---

## Conclusion

Le SOC efficace n’est pas celui qui a le plus d’outils.  
C’est celui qui :

- détecte suffisamment tôt
- réduit le bruit
- sait escalader
- améliore en continu

Prochain article : SIEM, logs et détection.

