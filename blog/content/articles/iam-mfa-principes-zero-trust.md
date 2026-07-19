---
title: "Accès, double verrou et confiance zéro (expliqués simplement)"
date: 2025-11-20
excerpt: "Qui a le droit d'ouvrir quoi, pourquoi le double verrou compte, et l'idée de ne jamais faire confiance par défaut."
type: article
tags: [IAM, MFA, Zero Trust, accès, sécurité]
series: cybersecurite-secops-serie
series_order: 6
og_image: iam-mfa-principes-zero-trust-1200x630.jpg
---

# Accès, double verrou et confiance zéro (expliqués simplement)

La plupart des incidents ne commencent pas par un exploit hollywoodien. Ils commencent par un **acces** : mot de passe vole, jeton qui trainait dans un ticket Slack, session qui n'a jamais expire, compte admin "temporaire" devenu permanent.

Si tu controles mal qui entre et avec quels droits, le reste de la stack (EDR, SIEM, [WAF](/blog/articles/[aws](/blog/articles/aws-fondamentaux-cloud-aws-services.html)-securite-iam-kms-waf.html)) arrive trop tard.

Bonne nouvelle : un **IAM** solide, c'est souvent le meilleur retour sur investissement. Pas besoin d'un budget banque. Besoin de decisions claires, de **double authentification** partout ou ca compte, et d'arreter de faire confiance a un laptop juste parce qu'il est "dans le VPN".

## Ce que "bon IAM" veut vraiment dire

L'**IAM** (Identity and Access Management), ce n'est pas juste un annuaire joli. C'est le cycle de vie des identites : creation, droits, revue, revocation.

Qui a un compte, pourquoi, jusqu'a quand, et comment on le coupe le jour ou la personne part ou change de role.

Quatre principes tiennent presque tout le reste :

- **Least privilege** : donner le minimum necessaire pour faire le job, pas "admin au cas ou"
- **Separation des roles** : le compte du quotidien n'est pas le compte qui touche a la prod
- **Tracabilite** : savoir qui a fait quoi, quand, depuis quel appareil
- **Revue d'acces** : retirer ce qui n'est plus utile, au lieu d'empiler les droits pendant trois ans

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/iam-zero-trust-couches.svg" alt="Schéma IAM et Zero Trust : couches identité, appareil, réseau, application, données" class="schema-inline" width="640" />
  <figcaption>Zero Trust en couches : identité, appareil, réseau, application, puis données - vérifier en continu, ne jamais faire confiance par défaut.</figcaption>
</figure>

Chez une TPE, ca peut tenir sur un tableur et un outil d'identite simple (Google Workspace, Microsoft 365, ou un SSO SaaS). Chez un SaaS, tu ajoutes des roles plus fins et un provisioning propre. Pas "tout le monde est admin dans GitHub".

## Double authentification : non negociable, mais bien choisie

La **double authentification** (souvent appelee MFA), ce n'est plus un "nice to have". C'est le filet qui sauve quand le password leak (et ils leakent).

Obligatoire au minimum sur :

- la **messagerie**
- les consoles **cloud**
- le VPN ou l'acces distant
- les outils de developpement (Git, CI/CD)
- tous les comptes **admin**

Le type de second facteur compte. Une app d'authentification ou des passkeys, c'est solide. Le SMS, tu le gardes en secours si tu n'as vraiment pas le choix - le vol de carte SIM existe.

Evite aussi la fatigue des notifications push sans controle : si ton equipe valide a l'aveugle, tu as un faux sentiment de securite.

Petit detail qui change tout : la double auth sur le **mail**. Si quelqu'un vole la boite aux lettres, il reset tout le reste. Securise le mail avant de te vanter d'avoir "tout en MFA" sur des apps secondaires.

## Comptes admin : la catastrophe silencieuse

Un pattern qui marche presque partout :

- Compte **standard** pour le quotidien (mail, Slack, docs)
- Compte **admin** separe, utilise uniquement quand il faut toucher a l'infra ou a la prod
- Sessions **courtes**
- Elevation temporaire (juste a temps) plutot qu'un badge admin permanent

Pourquoi ? Parce qu'un admin permanent, c'est un [incident](/blog/articles/incident-response-runbook-postmortem.html) en attente. [Phishing](/blog/articles/cybersecurite-fondamentaux-menaces-risques.html), malware, session volee sur un cafe wifi - et soudain l'attaquant a les cles de la maison.

Avec un compte separe et double auth dure, le rayon de degats baisse. Avec du "juste a temps", encore plus : les droits n'existent que le temps de la tache.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/iam-mfa-facteurs.svg" alt="Schema des facteurs d'authentification MFA" class="schema-inline" width="640" />
  <figcaption>MFA = au moins deux facteurs. Zero Trust = verifier en continu.</figcaption>
</figure>

Cote cloud, ca veut dire des roles scopes, pas "administrateur de tout" pour "aller plus vite". Cote SaaS produit, ca veut dire que les developpeurs n'ont pas tous les droits de prod en permanence. Oui, ca freine un peu. Non, ce n'est pas un frein inutile - c'est le frein qui evite l'accident.

Le piege classique des petites equipes, c'est le compte partage "devops" avec le mot de passe dans le gestionnaire de toute la boite. Le jour ou quelqu'un part mal, ou ou un poste est compromis, tu ne sais meme plus qui a fait quoi. Un compte **nomme**, double auth individuelle, droits revus : basique, mais ca sauve des post-mortems.

## Zero Trust, version pragmatique (pas le slide PowerPoint)

Le **Zero Trust**, ce n'est pas "acheter une boite et coller le logo sur le site". C'est une posture : ne pas faire confiance par defaut, meme a l'interne. Verifier l'identite et le contexte. Limiter le rayon de degats si ca casse.

Les couches du schema aident a penser :

- **Identite** : annuaire, double auth, SSO, cycle de vie
- **Appareil** : conformite, posture, [EDR](/blog/articles/edr-xdr-endpoint-detection-response.html) - un device non mange ou compromis ne devrait pas acceder a tout
- **Reseau** : acces cible, micro-segmentation - le VPN plat "tout le monde voit tout" est un modele des annees 2010
- **Application** : droits fins
- **Donnees** : chiffrement, labels, protection si vraiment sensible

Tu n'as pas a tout deployer d'un coup. Pour une TPE : double auth partout + comptes admin separes + acces conditionnel basique. Pour un SaaS : ajoute acces conditionnel, segmentation des environnements, jetons courts, et des alertes sur les changements d'acces.

## Signaux IAM a surveiller (meme sans gros [SOC](/blog/articles/secops-soc-fonctions-process.html))

Quelques alertes qui valent de l'or :

- Ajout d'un role admin ou d'une permission large
- Creation de cle API
- Login depuis un pays ou un reseau inhabituel
- Double auth desactivee ou methode changee
- Changements massifs de permissions
- Reset de password suivi d'un acces a des ressources sensibles

Ces evenements, tu les centralises (logs cloud, audit Microsoft/Google, logs d'identite) et tu les traites comme des P1 potentiels. Pas besoin de 200 regles. Dix regles bien choisies sur l'IAM battent souvent cent regles bruyantes ailleurs. Un [SIEM](/blog/articles/siem-log-management-detection.html) sobre aide.

## Demarrer sans tout reconstruire

Cette semaine, fais trois choses :

1. Active la **double authentification** sur mail, cloud et Git - vraiment, pas "on verra"
2. Liste les comptes **admin** et separe ceux qui vivent en mode permanent
3. Planifie une **revue d'acces** courte (une heure) pour retirer les droits morts

IAM + double auth + separation admin, c'est l'un des meilleurs leviers en cybersecurite. Ca ne remplace pas le [patching](/blog/articles/gestion-vulnerabilites-cve-patching.html) ni les logs. Mais sans ca, le reste est un chateau de cartes.
