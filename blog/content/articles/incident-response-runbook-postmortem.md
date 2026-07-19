---
title: "Quand ça casse : quoi faire, puis quoi apprendre"
date: 2025-11-25
excerpt: "Une fiche simple pour réagir sous stress, puis un débrief pour ne pas refaire la même erreur."
type: article
tags: [incident response, SOC, SecOps, runbook, post-mortem]
series: cybersecurite-secops-serie
series_order: 7
og_image: incident-response-runbook-postmortem-1200x630.jpg
---

# Quand ça casse : quoi faire, puis quoi apprendre

Un **incident** securite, c'est de la haute pression. Les gens parlent vite. Les hypotheses fusent. Quelqu'un veut "juste reboot" pendant qu'un autre veut "tout analyser avant de toucher".

Sans preparation, tu perds du temps, tu prends de mauvaises decisions, et tu elargis l'impact au lieu de le reduire.

L'objectif n'est pas d'avoir une equipe de vingt personnes. C'est d'avoir une reponse structuree, meme a trois heures du matin, meme a deux personnes. Un cycle clair, un **runbook** d'une page, un decideur, et un post-mortem qui change vraiment quelque chose.

## Les six phases (a garder en tete, pas a reciter)

1. **Preparation** : runbooks, contacts, acces, outils, exercices
2. **Detection** : alerte [EDR](/blog/articles/edr-xdr-endpoint-detection-response.html), [SIEM](/blog/articles/siem-log-management-detection.html), user qui signale un [phishing](/blog/articles/cybersecurite-fondamentaux-menaces-risques.html), cloud qui crie
3. **Containment** : empecher la propagation
4. **Eradication** : supprimer la cause (malware, compte compromis, backdoor)
5. **Recovery** : remettre en service propre
6. **Lessons learned** : post-mortem et actions

Le piege classique, c'est de vouloir eradiquer avant de contenir. Tu te lances dans une analyse parfaite pendant que l'attaquant continue de se promener. Stabilise d'abord. Contenir, c'est **acheter du temps**. Ensuite tu nettoies. Ensuite tu remets en route.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/incident-response-cycle.svg" alt="Schéma du cycle de réponse à incident : préparation, détection, containment, éradication, recovery, lessons learned" class="schema-inline" width="640" />
  <figcaption>Le cycle IR : préparer, détecter, contenir, éradiquer, restaurer, puis apprendre - dans cet ordre, surtout pour le containment.</figcaption>
</figure>

La preparation, elle, se joue **avant**. Si ton seul "plan" c'est "on appelle le prestataire et on improvise", tu vas le payer en heures et en stress. Les acces d'urgence, les mots de passe break-glass, le numero du prestataire EDR : tout ca se verifie un mardi calme, pas le dimanche de l'incident.

## Le runbook minimal (une page, utilisable a 3h)

Un bon **runbook** n'est pas un roman de 40 pages. C'est une page (deux max) que quelqu'un peut suivre sous stress.

Il contient :

- **Qui contacter** : IT, produit, legal, com, prestataire
- **Comment ouvrir** l'incident : canal dedie, ticket, doc partage
- **Quoi collecter** avant de tout casser : logs, captures EDR, snapshots, timeline
- **Actions de containment** typiques : isoler un poste, reset creds, revoquer sessions, bloquer une sortie reseau, couper un role admin
- **Criteres de retour** a la normale : quoi verifier avant de dire "c'est fini"

Ecris-le pour les cas qui te concernent vraiment. TPE : phishing, ranconneur sur poste, compte Microsoft/Google compromis. SaaS : cle API exposee, compte admin cloud, acces anormal a la base, chaine CI/CD.

Un runbook generique "tous incidents" ne sert a rien. Trois runbooks concrets valent mieux qu'un framework photocopie. Range-le la ou l'equipe le trouve sans chercher. Un runbook introuvable a 3h du matin **n'existe pas**.

## Containment : exemples qui marchent

Selon le scenario, le **containment** change :

- Poste suspect : isolation via EDR (reseau coupe, machine encore allumee pour analyser)
- Compte compromis : desactivation, reset **[double authentification](/blog/articles/iam-mfa-principes-zero-trust.html)**, revocation des sessions et jetons, revue des regles mail
- Cloud : coupe d'une cle d'acces, retrait d'un role trop large, blocage temporaire d'un stockage public
- Reseau : bloquer un domaine suspect, limiter les sorties
- Indicateur connu : bloquer un hash / une signature

Le but n'est pas d'etre elegant. C'est de reduire le **rayon de degats** rapidement. Documente ce que tu fais en meme temps : qui a isole quoi, a quelle heure. Ta timeline, c'est ta memoire collective - et souvent ta preuve pour le legal ou le client.

Attention au "containment" qui detruit les preuves. Redemarrer en masse, reformater trop tot, ecraser les logs : tu te tires une balle dans le pied. Contenir proprement, c'est **isoler sans effacer**. Sauf ranconneur actif ou chaque seconde compte - et la tu suis le runbook ranconneur, pas l'instinct.

## Communication : un decideur, des faits

Sans cadre, l'incident devient un chaos Slack. Regles simples :

- Un **incident commander** (un seul decideur)
- Une **timeline** partagee (qui fait quoi, quand)
- Des updates regulieres (toutes les 30 a 60 minutes au debut)
- Des **faits**, pas de speculation : "on a vu X a Y heure" vaut mieux que "je pense que c'est un APT"

Si des donnees personnelles sont potentiellement touchees, leve le drapeau [RGPD](/blog/articles/conformite-rgpd-nis2-iso27001.html) tot : legal / DPO dans la boucle. Mieux vaut preparer une analyse que decouvrir a J+5 que tu etais hors delai. Pareil cote clients SaaS : mieux vaut une com factuelle et precoce qu'un silence qui detruit la confiance.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/incident-postmortem.svg" alt="Schema du deroule d'un post-mortem d'incident" class="schema-inline" width="640" />
  <figcaption>Un post-mortem sans actions datees, c'est du theatre.</figcaption>
</figure>

Evite aussi le canal unique ou tout le monde discute - clients, speculation, tech et com melanges. Un canal **operationnel** pour ceux qui agissent, un canal **status** pour ceux qui ont besoin d'etre informes. Sinon le bruit ralentit les gens qui doivent contenir.

## Post-mortem : utile, pas politique

Le **post-mortem** n'est pas une seance de culpabilite. C'est un outil d'amelioration.

Cause racine technique *et* organisationnelle (souvent le vrai probleme, c'est un droit trop large ou une alerte ignoree). Actions avec **owner** et **date**. Detections manquantes. Process a corriger.

Si personne ne repart avec une tache assignee, tu as ecrit un recit, pas un plan.

Fais-le a chaud (dans la semaine), mais pas dans l'emotion de la nuit de crise. Une heure, un doc court, des decisions. Ensuite, verifie que les actions avancent. Le post-mortem sans suivi, c'est du theatre. Et si la meme cause revient trois mois plus tard, ce n'est plus un incident - c'est un process qui n'a jamais bouge.

Un petit [SOC](/blog/articles/secops-soc-fonctions-process.html) sans post-mortem, ca stagne vite.

## Exercer avant d'en avoir besoin

Tu n'as pas besoin d'un red team hollywoodien. Un **tabletop** d'une heure tous les trimestres change deja la donne.

Prends un scenario : "cle [AWS](/blog/articles/aws-fondamentaux-cloud-aws-services.html) leakee sur GitHub public" ou "comptable clique sur un phishing, notification push validee". Marche le runbook. Chronometre. Note ou ca coince (acces manquant, contact introuvable, outil qui demande une double auth que personne n'a).

La difference entre une boite mature et une boite fragile, ce n'est pas l'absence d'incidents. C'est la capacite a repondre **vite et proprement**.
