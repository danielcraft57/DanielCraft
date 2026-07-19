---
title: "SIEM : lire les traces de ton système sans te noyer"
date: 2025-11-11
excerpt: "Les journaux d'activité, comment les rassembler, et repérer le vrai signal sans mille fausses alertes."
type: article
tags: [SIEM, logs, détection, SecOps, SOC]
series: cybersecurite-secops-serie
series_order: 3
og_image: siem-log-management-detection-1200x630.jpg
---

# SIEM : lire les traces de ton système sans te noyer

Un **SIEM** (Security Information and Event Management), dans l'idee, c'est simple. Tu ramasses des evenements. Tu les ranges proprement. Tu cherches des comportements louches.

En pratique, le piege classique c'est de tout logger "au cas ou". Facture qui explose. Tableau de bord joli. Bruit partout. Et personne qui enquete vraiment.

Si tu es une petite boite ou un SaaS en croissance, tu n'as pas besoin d'avaler Internet. Tu as besoin d'une strategie de **logs** assez bonne pour repondre a "qui a fait quoi, quand". Et assez sobre pour que ton budget et ton equipe survivent.

## Les logs qui servent vraiment

Commence par ce qui aide a enquete, pas par ce qui fait du volume.

Les **identites** d'abord : connexions, **[double authentification](/blog/articles/iam-mfa-principes-zero-trust.html)**, echecs, elevations de droits. Ensuite les **postes** : programmes lances, signaux antivirus ou [EDR](/blog/articles/edr-xdr-endpoint-detection-response.html). Le **reseau** : DNS, proxy, sorties bizarres. Le **cloud** : appels API, changements d'acces, stockage public, creation de cles. Les **apps** : erreurs d'auth, actions admin, exports massifs, suppressions, changements de role.

Si tu dois choisir, choisis ce qui prouve **"qui a fait quoi"**. Les logs de debug verbeux, on s'en passera au debut.

Chez un SaaS, logs cloud + logs d'identite + EDR, c'est deja une base solide. Chez une TPE plus classique : messagerie (Microsoft 365 / Google Workspace) + firewall + postes critiques. Souvent le bon point de depart.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/siem-pipeline-logs.svg" alt="Schéma du pipeline SIEM : collecte, normalisation, corrélation et alertes" class="schema-inline" width="640" />
  <figcaption>Le pipeline SIEM : collecter, normaliser, corréler, alerter - sans tout indexer à chaud.</figcaption>
</figure>

## Retention : chaud, froid, et un peu de lucidite

Tout garder "chaud" (interrogeable vite, cher) pendant un an, c'est le moyen le plus rapide de regretter son SIEM.

En pratique, deux niveaux suffisent souvent :

- **Chaud** : 7 a 30 jours pour enquete vite
- **Froid / archive** : 90 a 365 jours pour remonter une attaque lente ou repondre a une demande legale / client

Indexe ce que tu interroges vraiment. Archive le reste. Et note tes besoins de [conformite](/blog/articles/conformite-rgpd-nis2-iso27001.html) avant de decider au feeling. Un SaaS B2B qui vend a des grands comptes n'a pas les memes exigences qu'un site vitrine. Ce n'est pas de la theorie : c'est ce qui apparait dans les questionnaires securite.

## Normalisation et contexte : le log brut ne suffit pas

Un evenement "login failed" tout seul, c'est du **bruit**. Le meme evenement avec le role de l'utilisateur, l'importance de la machine, une geoloc, et un tag prod/dev, ca devient une **piste**.

Une alerte "echec login" devient utile si tu sais : admin prod, depuis un pays jamais vu, juste apres une campagne de faux mails.

Le contexte, c'est aussi l'**inventaire** et les noms. Si tes machines s'appellent toutes "PC-12" sans proprietaire, ton [petit SOC](/blog/articles/secops-soc-fonctions-process.html) perd du temps a chaque alerte. Pareil pour les comptes de service sans owner. Le SIEM n'est pas magique : il amplifie la qualite de ton hygiene.

## Des detections simples avant la science-fiction

Les regles les plus rentables sont souvent banales :

- Brute force suivi d'un succes
- Connexion "impossible" geographiquement
- Creation de cle API
- Changement d'acces / ajout admin
- Execution d'outils suspects
- Upload / sortie de donnees massive

Tu veux des alertes **actionnables**, pas des "bruits interessants". Une bonne regle a un owner, une severite, et une fiche d'actions d'une demi-page. Si personne ne sait quoi faire quand elle sonne, ce n'est pas une detection. C'est de la decoration.

Pour un SaaS, commence par les actions d'acces cloud et les acces admin applicatifs. Pour une TPE, commence par les comptes mail et les postes dirigeants. La ou une compromission fait le plus de degats. Les bases [menaces / risques](/blog/articles/cybersecurite-fondamentaux-menaces-risques.html) aident a choisir.

## Faux positifs : la vraie bataille quotidienne

Reduire les **faux positifs**, c'est du travail de fond. Listes blanches controlees (sans ouvrir trop large). Seuils adaptes a ton trafic reel. Enrichissement de contexte. Suppression des sources inutiles. Et surtout : une revue reguliere des regles qui crient pour rien.

Le piege, c'est d'etouffer une regle bruyante en la desactivant completement. Parfois il faut juste la **resserrer**. Un SaaS qui fait beaucoup de deploiements va generer des patterns "anormaux" pour un modele bancaire. Adapte. Ne copie pas des regles Internet sans les ajuster a ton rythme.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/siem-faux-positifs.svg" alt="Schema signal versus bruit dans un SIEM" class="schema-inline" width="640" />
  <figcaption>La vraie bataille du SIEM : moins d'alertes, plus d'actions.</figcaption>
</figure>

## Operer un SIEM sans equipe de vingt personnes

Tu n'as pas besoin de chasse avancee des le jour 1. Tu as besoin de : sources prioritaires branchees, une poignee de regles utiles, un canal de **triage**, et quelqu'un qui regarde vraiment. Une heure par jour bien placee bat huit heures de dashboards ignores.

Mesure le taux de faux positifs et le temps moyen de prise en charge. Si une regle genere 40 alertes par semaine et zero vrai positif depuis deux mois, traite-la. Sinon ton equipe apprend a ignorer *toutes* les alertes, y compris les bonnes.

Et n'oublie pas le **cout**. Chaque Go logge a un prix. Chaque regle a un cout humain. Le SIEM mature, ce n'est pas "plus de data". C'est "la bonne data, au bon endroit, avec des gens qui savent quoi en faire".

## Un scenario concret pour ancrer

Imagine un SaaS de douze personnes. Lundi matin, alerte : creation d'une cle d'acces depuis un compte rarement utilise. Le SIEM a aussi vu un login avec double authentification OK depuis un reseau inhabituel une heure avant.

Sans **correlation**, tu as deux tickets moyens. Avec correlation et contexte (compte admin, prod, reseau jamais vu), tu as un P1. Tu revoques la cle, tu forces un reset de session, tu audits les autres actions. Vingt minutes plus tard, tu sais si c'etait un vrai [incident](/blog/articles/incident-response-runbook-postmortem.html) ou un collegue en deplacement.

Ce genre de chaine, c'est exactement ce pour quoi tu paies un SIEM. Pas pour stocker des logs serveur jusqu'a la fin des temps.
