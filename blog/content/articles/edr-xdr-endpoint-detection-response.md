---
title: "EDR et XDR : protéger les ordinateurs et réagir vite"
date: 2025-11-13
excerpt: "Des outils qui surveillent PCs et serveurs, isolent en cas de souci, et aident à répondre sans panique."
type: article
tags: [EDR, XDR, endpoint, SOC, SecOps]
series: cybersecurite-secops-serie
series_order: 4
og_image: edr-xdr-endpoint-detection-response-1200x630.jpg
---

# EDR et XDR : protéger les ordinateurs et réagir vite

L'**EDR** (Endpoint Detection & Response), c'est probablement l'un des outils les plus rentables en securite. Pourquoi ? Parce qu'il se place la ou beaucoup d'attaques se jouent vraiment : les **postes** et les **serveurs**.

Pas dans un PowerPoint. Sur la machine de ton commercial. Sur le bastion un peu oublie. Sur le laptop du fondateur qui a encore des droits admin "parce que c'est plus simple".

Mais un EDR n'est pas une baguette magique. Si tu le deploies a moitie, avec des exclusions enormes et zero plan de reponse, tu as surtout achete une licence et un **faux sentiment** de securite.

## Antivirus vs EDR : pourquoi le "classique" ne suffit plus

L'**antivirus** classique travaille surtout par signatures. Contre le connu, ca aide. Contre un ranconneur moderne ou un attaquant qui detourne des outils legitimes (PowerShell, outils admin), tu as besoin de **comportement** et de traces.

L'EDR collecte ce qui se passe sur la machine : programmes lances, lignes de commande, reseau, persistance. Il detecte des patterns suspects. Et surtout, il permet de **repondre** : isoler une machine, tuer un process, mettre en quarantaine, parfois revenir en arriere.

C'est la difference entre "on a un bandeau rouge" et "on coupe la machine avant que ca se propage".

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/edr-xdr-couches.svg" alt="Schéma des couches EDR et XDR : endpoint, identité, mail, réseau, cloud" class="schema-inline" width="640" />
  <figcaption>EDR sur l'endpoint, XDR quand on corrèle plusieurs couches (identité, mail, réseau, cloud).</figcaption>
</figure>

## XDR : utile si tu peux vraiment correler

Le **XDR** (Extended Detection & Response) promet d'elargir la correlation : postes, identite, email, reseau, cloud. L'idee est bonne.

En pratique, c'est interessant si tu peux relier une chaine : faux mail → login anormal → malware → fuite de donnees. Sinon tu te retrouves avec plusieurs produits sous une meme marque, sans vision globale reelle.

Pour une TPE, un bon EDR bien opere bat souvent un "XDR" mal branche. Pour un SaaS qui vit dans le cloud, la correlation identite + poste + logs cloud a clairement plus de sens. Ne paie pas le label. Paie la capacite a **raconter une attaque** de bout en bout.

Ca se branche bien avec un [SIEM](/blog/articles/siem-log-management-detection.html) et un petit [SOC](/blog/articles/secops-soc-fonctions-process.html) qui trie vraiment.

## Deploiement : les pieges qui tuent la valeur

Les classiques :

- Des agents **pas partout** : angles morts garantis
- Des exclusions **trop larges** "parce que ca cassait une appli metier"
- Des serveurs de prod oublies pendant qu'on couvre uniquement les laptops
- Aucun plan de reponse : on detecte, mais on ne sait pas qui isole quoi

Un bon debut : couvrir d'abord les actifs **critiques** (dirigeants, admins, serveurs prod, bastions). Definir ce qui est normal chez toi. Documenter cinq actions de reponse : isolation reseau, kill process, collecte legere, reset credentials, rollback si dispo.

Tester une isolation sur une machine de test. Oui, vraiment. Le jour J, tu seras content d'avoir deja clique une fois.

Chez un SaaS, les runners CI et les bastions SSH sont souvent des trous. Chez une TPE, ce sont les postes "VIP" et les machines qui accedent a la compta. Priorise. Couvrir **60 %** des machines critiques vaut mieux que 100 % des postes non critiques et zero serveur.

## Les alertes qui valent le coup

Les signaux haute valeur reviennent souvent :

- PowerShell encode / commandes louches
- Creation de **persistance** (demarrage auto, services, taches planifiees)
- Vol de mots de passe en memoire
- Outils legitimes detournes
- Connexions sortantes anormales, surtout vers des destinations jamais vues

Et surtout : correlater avec l'**identite**. Qui, d'ou, quand. Un process suspect lance par un compte admin a 3h du matin depuis un laptop inhabituel, ce n'est pas la meme chose qu'un script IT documente en journee. Voir aussi [IAM / double authentification](/blog/articles/iam-mfa-principes-zero-trust.html).

Si ton EDR crie pour chaque install legitime d'imprimante, resserre. Si tu n'as jamais d'alerte sur les vols de credentials, verifie ta couverture. Le silence total n'est pas forcement une bonne nouvelle.

## Repondre : containment d'abord

Lors d'un [incident](/blog/articles/incident-response-runbook-postmortem.html), l'EDR sert d'abord a **contenir**. Isoler la machine suspecte pour freiner le mouvement lateral. Couper les sessions. Collecter assez de preuves pour comprendre le perimetre. Ensuite seulement, eradiquer et restaurer.

La tentation, c'est de reformater trop vite "pour etre tranquille". Parfois c'est necessaire. Parfois tu detruis juste les indices qui t'auraient dit combien d'autres machines sont touchees.

Un petit runbook aide : containment → scope → eradication → recovery → lessons learned.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/edr-containment.svg" alt="Schema des etapes de containment EDR" class="schema-inline" width="640" />
  <figcaption>Repondre = containment d'abord, analyse ensuite.</figcaption>
</figure>

Pour une petite equipe, decide a l'avance qui a le droit d'isoler une machine de prod. Ce n'est pas un detail. Une isolation mal synchronisee avec l'IT peut faire plus de bruit metier qu'un malware discret. Securite et continuite, meme conversation.

## Operer l'EDR au quotidien

Regarde les alertes. Vraiment. Une revue **quotidienne** courte vaut mieux qu'un bilan mensuel de 200 items ignores. Tune les exclusions avec parcimonie. Mets a jour les agents. Verifie la couverture chaque mois (les laptops "oublies" reviennent toujours).

L'EDR brille quand quelqu'un l'**opere**. Sinon c'est un antivirus un peu plus bavard. Si tu externalises la surveillance, garde quand meme un owner interne pour les decisions de containment et les acces.

Au final, EDR bien deploye + **double authentification** + sauvegardes testees, c'est deja une posture tres respectable. Le XDR peut venir apres, quand les bases tiennent.

## Petit scenario terrain

Un commercial clique un faux "suivi de colis". L'EDR voit un process inhabituel, une persistance timidement posee, une connexion sortante.

Si l'agent est la et que quelqu'un regarde, tu isoles le laptop en quelques minutes, tu revoques la session mail, tu verifies s'il y a eu mouvement lateral.

Si l'agent n'etait pas installe "parce que ca ralentissait Excel", tu decouvres le probleme trois jours plus tard via un client qui recoit des mails bizarres.

Meme entreprise. Meme [phishing](/blog/articles/cybersecurite-fondamentaux-menaces-risques.html). Posture differente. C'est tout l'interet de l'EDR : **raccourcir** cette fenetre, pas promettre l'immunite.
