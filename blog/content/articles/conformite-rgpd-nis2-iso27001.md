---
title: "RGPD, NIS2, ISO : se mettre en règle sans paniquer"
date: 2025-12-04
excerpt: "Ce que ces cadres demandent vraiment : des contrôles, des preuves, et du bon sens — pas un classeur poussiéreux."
type: article
tags: [RGPD, NIS2, ISO 27001, conformité, sécurité]
series: cybersecurite-secops-serie
series_order: 10
og_image: conformite-rgpd-nis2-iso27001-1200x630.jpg
---

# RGPD, NIS2, ISO : se mettre en règle sans paniquer

La **conformite**, on la vit souvent comme une contrainte : audits, questionnaires clients, politiques de 40 pages que personne ne lit. Elle peut aussi servir de cadre pour professionnaliser la securite.

Le piege, c'est la conformite "papier" : des docs beaux, des pratiques qui n'ont pas change d'un iota.

RGPD, NIS2 et ISO 27001 ne disent pas exactement la meme chose. Mais ils convergent vers une idee simple : gerer les **risques**, proteger les **donnees**, etre capable de repondre aux **incidents**, et **prouver** ce que tu fais.

Si tu as suivi le reste de cette serie ([IAM](/blog/articles/iam-mfa-principes-zero-trust.html), [vulns](/blog/articles/gestion-vulnerabilites-cve-patching.html), logs, IR), tu es deja plus avance que beaucoup de boites "certifiees" sur le papier.

## RGPD : donnees personnelles, pas "toute la cyber"

Le **RGPD** porte sur les donnees personnelles. Collecte minimale, base legale, droits des personnes (acces, suppression, opposition), securite et confidentialite, notification en cas de violation selon la gravite et les risques.

Ce n'est pas un standard technique detaille. C'est une obligation de moyens et de responsabilite autour des donnees des gens.

En pratique, ca te pousse a :

- **Cartographier** les traitements
- Limiter les **acces**
- Tracer les acces sensibles
- Chiffrer ce qui compte
- Preparer une [reponse a incident](/blog/articles/incident-response-runbook-postmortem.html) qui inclut l'angle "donnees personnelles"

Le registre des traitements n'est pas un exercice scolaire : c'est ta carte pour savoir ou sont les donnees le jour ou ca fuit.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/conformite-rgpd-nis2-iso.svg" alt="Schéma conformité : RGPD, NIS2 et ISO 27001 avec socle commun risques et preuves" class="schema-inline" width="640" />
  <figcaption>Trois cadres, un socle commun : risques, preuves, responsabilité, amélioration continue.</figcaption>
</figure>

Pour une TPE : liste tes outils (CRM, mail, site, facturation), quelles donnees ils tiennent, qui y accede, combien de temps tu gardes. Pour un SaaS : ajoute sous-traitants, transferts hors UE, analyse d'impact si tu fais du profiling ou du traitement a risque, et un process clair pour les demandes d'exercice de droits.

## NIS2 : resilience et obligation de prendre la cyber au serieux

**NIS2** vise a relever le niveau de cybersecurite des entites essentielles et importantes - secteurs critiques, services numeriques, etc. Gestion des risques, incidents, continuite, chaine d'approvisionnement, gouvernance.

Meme si tu n'es pas directement dans le perimetre, NIS2 influence les exigences clients, les contrats, et les audits. Les grands comptes te demanderont de plus en plus de prouver que tu tiens debout.

Concretement, NIS2 pousse vers ce que cette serie decrit deja : IAM, patching, detection, IR, supply chain. Ce n'est pas "acheter un outil NIS2". C'est avoir une **gouvernance** cyber (qui decide, qui est responsable), des mesures proportionnees, et un signalement d'incidents quand c'est requis.

Si un client te demande "etes-vous NIS2 ready ?", ne reponds pas par un slide. Montre **double authentification**, revues d'acces, sauvegardes testees, runbooks, et un plan d'amelioration date. C'est plus credible qu'un badge marketing. Les [bases cyber](/blog/articles/cybersecurite-fondamentaux-menaces-risques.html) aident a parler risque sans jargon.

## ISO 27001 : un systeme de management, pas un firewall

**ISO 27001**, ce n'est pas "avoir un antivirus et un firewall". C'est un **SMSI** (systeme de management de la securite de l'information) : politiques, gestion des risques, selection de controles (Annexe A), audits internes, amelioration continue (planifier, faire, verifier, ameliorer).

Tu definis ton perimetre, tu evalues les risques, tu traites, tu mesures, tu corriges.

Une bonne ISO reduit les erreurs repetees. Une mauvaise ISO produit des politiques que personne n'applique et des preuves bricolees la veille de l'audit. Si tu vises la certification, commence par le **fond** (risques reels, controles utiles), pas par le logo. Le logo sans fond, ca se voit a la premiere non-conformite majeure.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/conformite-preuves.svg" alt="Schema boucle politique controle preuve audit" class="schema-inline" width="640" />
  <figcaption>Conformite pragmatique = controle + preuve, pas binder poussiereux.</figcaption>
</figure>

Meme sans viser la certif, s'inspirer d'ISO 27001 aide : inventaire d'actifs, classification, politiques **courtes**, revues periodiques, preuves continues (pas un classeur PDF annuel). L'idee planifier / faire / verifier / ameliorer vaut pour une TPE de cinq personnes autant que pour un groupe.

## Transformer la conformite en securite reelle

Si tu veux du concret, aligne-toi sur ce qui reduit vraiment le risque :

- Politiques **courtes** et applicables (deux pages > vingt pages)
- Inventaire des actifs et des donnees
- IAM : double auth, droits au minimum, revues
- Patching et vulns avec delais
- Logs + detection ([SIEM](/blog/articles/siem-log-management-detection.html), [SOC](/blog/articles/secops-soc-fonctions-process.html))
- Sauvegardes **testees** (restore, pas seulement backup)
- Runbooks incidents + exercices
- Revues regulieres

La conformite est "reussie" quand elle ameliore le quotidien operationnel. Si ton registre RGPD est a jour mais que tout le monde partage le meme compte admin cloud, tu as un probleme. Si tu as un certificat ISO et zero detection d'incident, tu as un autre probleme.

Les **preuves** suivent les pratiques - pas l'inverse. Fais les bonnes choses, documente legerement. Evite de documenter des fictions. Un auditeur un peu experimente sent la difference entre un process vivant et un PDF genere la veille.

## Un kit de demarrage "audit-proof" (sans se noyer)

- Registre des traitements (RGPD) a jour, meme imparfait
- Classification simple des donnees : public / interne / sensible
- Revue d'acces **trimestrielle** (une heure, pas un projet de six mois)
- Plan de reponse a incident + un exercice tabletop
- Plan de continuite minimum : que se passe-t-il si le SaaS critique tombe, si le laptop du dirigeant est perdu, si la prod est down 24h
- Liste des sous-traitants et de leurs engagements
- Politique de mots de passe / double auth d'**une page**

Pour un SaaS qui vend a des entreprises : ajoute un pack "security & privacy" (resume des mesures, localisation des donnees, process incident, contacts). Ca reduit les allers-retours questionnaires et ca force a clarifier ce que tu fais vraiment.

Tu n'as pas besoin de tout certifier pour etre credible. Tu as besoin d'etre capable d'expliquer, de montrer, et de tenir ce que tu promets dans les contrats.

## Fin de serie : ce qui reste

RGPD, NIS2 et ISO 27001 convergent : risques, donnees, incidents, preuves, amelioration. Si tu appliques le fil de la serie - fondamentaux, SecOps, [EDR](/blog/articles/edr-xdr-endpoint-detection-response.html)/SIEM, vulns, IAM, IR, [cloud](/blog/articles/securite-cloud-cspm-cwpp.html), [DevSecOps](/blog/articles/devsecops-sast-dast-sbom.html) - tu n'as pas "fini" la cyber. Mais tu as un **socle**.

Le reste, c'est de la repetition et de l'amelioration, pas de la magie.

Choisis une action cette semaine : revue d'acces, exercice IR d'une heure, ou mise a jour du registre des traitements. La conformite utile commence la - pas dans un PowerPoint de 60 slides.
