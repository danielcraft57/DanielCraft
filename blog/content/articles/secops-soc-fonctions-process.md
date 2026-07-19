---
title: "SecOps et SOC : qui surveille quoi (expliqué simplement)"
date: 2025-11-06
excerpt: "Qui regarde les alertes, comment on trie, et comment on s'améliore après un raté — sans jargon inutile."
type: article
tags: [SecOps, SOC, incident, détection, opérations]
series: cybersecurite-secops-serie
series_order: 2
og_image: secops-soc-fonctions-process-1200x630.jpg
---

# SecOps et SOC : qui surveille quoi (expliqué simplement)

Beaucoup de boites achettent un [SIEM](/blog/articles/siem-log-management-detection.html) ou un [EDR](/blog/articles/edr-xdr-endpoint-detection-response.html) et se disent : "on fait du SecOps". Honnêtement, non.

Le **SecOps**, c'est surtout une organisation. Qui regarde quoi. Comment on decide que c'est urgent. Comment on s'ameliore apres un rate. L'outil sans process, c'est une **alarme** de voiture que personne n'entend dans le parking.

Que tu sois une petite boite avec un prestataire a mi-temps, ou un SaaS de quinze personnes, tu peux avoir un "petit SOC". Pas un open space avec des murs d'ecrans. Juste une facon claire de traiter les signaux sans paniquer a chaque notification.

## SecOps et SOC, ce n'est pas la meme chose

Le **SecOps**, c'est la securite au quotidien : fermer les portes, reparer, suivre avec l'IT. Le **SOC** (Security Operations Center), c'est la fonction "on surveille et on repond" : regarder, trier, escalader, gerer un [incident](/blog/articles/incident-response-runbook-postmortem.html).

Un SOC peut etre chez toi, chez un prestataire, ou un mix des deux. Ce qui ne marche jamais : externaliser et croire que tu n'as plus rien a faire. Il faut toujours des **proprietaires** cote entreprise. Sinon le prestataire te balance des alertes dans le vide, et toi tu reponds "on verra lundi".

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/secops-soc-boucle.svg" alt="Schéma de la boucle SecOps et SOC : collecter, détecter, trier, répondre, améliorer" class="schema-inline" width="640" />
  <figcaption>La boucle SecOps : collecter, détecter, trier, investiguer, répondre, puis améliorer.</figcaption>
</figure>

## Ce que fait vraiment un SOC

En clair, la machine tourne comme ca.

On **collecte** des signaux : logs, evenements sur les postes, cloud, parfois le mail. On **detecte** avec des regles et un peu de bon sens. On **trie** pour separer le bruit du vrai signal. On **enquete** : qui, quand, quel impact metier. On **repond** : isoler, couper un acces, restaurer. Et on **ameliore** : retour d'experience, nouvelles regles, portes mieux fermees.

Si une de ces etapes manque, ca se voit. Beaucoup de petites equipes ont de la detection (un EDR, des logs cloud) mais zero **triage** ecrit. Resultat : soit on ignore tout, soit on vit en mode urgence permanente.

## Le triage, c'est la que ca se gagne ou se perd

Un mauvais triage, c'est deux symptomes classiques. Soit tu alertes trop et tout le monde fatigue. Soit tu rates le vrai probleme parce qu'il etait noye dans le bruit.

Un bon triage classe vite selon trois axes :

- **Severite** : quel degat metier si c'est vrai
- **Confiance** : a quel point on croit l'alerte
- **Urgence** : combien de temps on a pour agir

Le but n'est pas d'ecrire un roman. C'est de decide *quoi faire maintenant*.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/secops-triage-severite.svg" alt="Schema entonnoir de triage SOC des alertes aux incidents" class="schema-inline" width="640" />
  <figcaption>Le triage decide si tu gagnes la journee ou si tu cours apres le bruit.</figcaption>
</figure>

Exemple simple. Une alerte "echec de login" sur un compte marketing, c'est souvent priorite basse. La meme alerte suivie d'un succes, puis d'une creation de cle API sur un compte admin cloud : ca devient priorite haute en deux minutes. Sans regles de triage, les deux atterrissent dans le meme canal Slack et meurent la.

## Le minimum viable pour un petit SOC

Meme sans equipe 24/7, tu peux tenir debout.

- Une **boite d'entree** unique pour les alertes (ticket, canal dedie, peu importe)
- Une priorisation simple **P1 / P2 / P3** avec des definitions en trois lignes
- Une astreinte, ou au moins "qui on appelle le week-end"
- Des **runbooks** (fiches d'actions) pour une poignee de cas : phishing, brute force, fuite de mots de passe, malware sur poste, compte admin suspect
- Un canal de crise et un doc incident d'**une page**

Tu passes de "panique collective sur WhatsApp" a "reponse organisee". Pour une petite boite, le runbook phishing peut tenir sur une checklist : isoler le compte, revoquer les sessions, reset de la **[double authentification](/blog/articles/iam-mfa-principes-zero-trust.html)**, verifier les regles de redirection mail, prevenir si des clients ont ete contactes. Rien de fancy. Juste ecrit **avant** le chaos.

Cote SaaS, ajoute le scenario "cle API exposee" et "compte admin cloud compromis". Ce sont les deux qui font vraiment mal. Si ton equipe sait deja qui revoque quoi et dans quel ordre, tu gagnes des heures precieuses.

## Roles sans se prendre pour une banque

Le modele L1 / L2 / L3 reste utile meme en version allegee.

- **L1** trie : bruit vs signal
- **L2** enquete : liens entre alertes, perimetre
- **L3** apporte l'expertise : analyse poussee, chasse, outillage

Dans une petite structure, la meme personne peut porter plusieurs casquettes. Ce qui compte, c'est de savoir *quand* on **escalade**, pas d'avoir trois badges LinkedIn.

Cote IT / ops, il faut des partenaires clairs : qui coupe un compte, qui isole une machine, qui touche a la prod. Le SOC qui alerte sans pouvoir faire agir l'IT, c'est du theatre. Le jour ou un serveur prod doit etre isole, tu ne veux pas decouvrir que personne n'a la main.

Pour les bases (menaces, risques, posture), vois aussi l'article sur les [fondamentaux cyber](/blog/articles/cybersecurite-fondamentaux-menaces-risques.html).

## La boucle d'amelioration (sinon tu stagnes)

Chaque incident un peu serieux merite un **retour d'experience** court. Pas un PowerPoint de culpabilite. Trois questions : qu'est-ce qui a marche, qu'est-ce qui a coince, qu'est-ce qu'on change.

Souvent le changement, c'est une regle de detection, une exclusion EDR trop large, un runbook manquant, ou un droit trop large qu'on avait "laisse pour plus tard".

Mesure aussi ce qui compte : temps de triage, taux de faux positifs sur les regles bruyantes, temps pour **contenir** un P1. Si ton SIEM genere 200 alertes par jour et que personne ne les traite, tu n'as pas un SOC. Tu as un generateur de culpabilite.

## Demarrer sans tout reconstruire

Cette semaine, choisis **dix alertes** reelles (ou des scenarios) et ecris pour chacune : priorite, premiere action, qui escalade. Mets ca dans un doc partage.

Demain, quand quelque chose sonne, tu auras deja un reflexe. SecOps, ce n'est pas "avoir plus d'outils". C'est avoir **moins d'improvisation** le jour ou ca compte.
