---
title: "Cybersécurité : ce qui peut te faire mal (et comment te protéger)"
date: 2025-11-04
excerpt: "Comme pour une maison : menaces, faiblesses, risques, et les gestes simples pour se protéger sans paniquer."
type: article
tags: [cybersécurité, risques, menaces, SecOps, sécurité]
series: cybersecurite-secops-serie
series_order: 1
og_image: cybersecurite-fondamentaux-menaces-risques-1200x630.jpg
---

# Cybersécurité : ce qui peut te faire mal (et comment te protéger)

Imagine ta maison. Tu ne laisses pas la porte grande ouverte toute la nuit. Tu fermes a cle, tu regardes parfois par la fenetre, et tu sais quoi faire si l'alarme sonne. La **cybersecurite**, c'est la meme idee... mais pour ton ordinateur, ton site, ta boite mail et tes fichiers clients.

Ce n'est **pas** un produit magique qu'on achete un vendredi. C'est surtout des **habitudes**. Des petits gestes un peu ennuyeux qui, le jour ou ca va mal, changent tout.

Si tu as une petite entreprise ou un projet en ligne, tu n'as pas besoin d'un discours de conference. Tu as besoin de savoir : qu'est-ce qui peut me faire mal ? Qu'est-ce qui est du bruit ? Ou je commence ?

## Menace, faiblesse, risque : trois mots differents

Une **menace**, c'est ce qui peut te faire mal. Un pirate, un faux mail, un logiciel malveillant, un employe presse qui clique trop vite, une panne chez un fournisseur.

Une **faiblesse** (on dit aussi [vulnerabilite](/blog/articles/gestion-vulnerabilites-cve-patching.html)), c'est un trou dans ta defense : un mot de passe trop simple, un logiciel pas a jour, une cle partagee dans un document "temporaire" qui a trois ans.

Le **risque**, c'est quand une menace rencontre une faiblesse *chez toi*. Probabilite × degats. Deux entreprises peuvent avoir le meme trou technique. Pour l'une, c'est un vieux serveur de test. Pour l'autre, c'est la base clients. Meme trou, risque totalement different.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/cyber-menaces-risque-posture.svg" alt="Schema menaces, faiblesses, risque et posture de securite" class="schema-inline" width="640" />
  <figcaption>Menace, faiblesse et risque : trois idees distinctes. Ne les melange pas.</figcaption>
</figure>

Exemple simple : un compte admin sans **[double authentification](/blog/articles/iam-mfa-principes-zero-trust.html)** sur un outil cloud, c'est un gros risque pour un service en ligne. Pour un artisan avec un site vitrine, le vrai probleme peut plutot etre : toute la facturation passe par une seule boite Gmail sans protection. Le **contexte** decide.

## Ce qui arrive vraiment (pas dans les films)

Le **phishing**, c'est le champion. Des mails qui ont l'air vrais. Tu es presse, tu cliques, et parfois la porte s'ouvre. Chez beaucoup d'entreprises, ca commence par la boite d'un commercial ou du support. Ensuite les acces importants. Ensuite quelqu'un qui cree une cle secrete et disparaît.

Le **ransomware**, c'est le "ranconneur" : on bloque tes fichiers et on demande de l'argent. En vrai, ca arrive rarement d'un coup. Souvent on vole d'abord des mots de passe, on se promene un peu, parfois on copie tes donnees *avant* de tout verrouiller. Si tes **sauvegardes** sont branchees en permanence sur le meme reseau, elles peuvent etre bloquees en meme temps. Catastrophe.

La **chaine d'outils** (supply chain), c'est plus sournois. Tu n'as rien "casse". C'est un plugin, un outil en ligne, un prestataire qui a laisse trainer une cle. Pour une petite boite, tu n'es pas toujours la cible principale : tu es collatéral. L'outil populaire se fait piquer, et tes donnees clients se retrouvent dehors.

Et puis il y a l'erreur toute bete : un dossier de fichiers ouvert a tout le monde, une cle secrete poussee sur GitHub un vendredi soir, un acces distant laisse ouvert "juste le temps de reparer". Ces trucs-la font autant de degats que les attaques de film. Et ils sont bien plus frequents.

## Les gestes qui marchent vraiment (le 80/20)

Tu n'as pas besoin d'etre parfait. Tu as besoin de quelques gestes qui reduisent vraiment le danger.

- **Double authentification** partout ou ca compte : mail, outils admin, cloud, GitHub.
- Des **droits limites** : chacun a seulement ce dont il a besoin. Pas d'admin permanent sur le PC du quotidien.
- Des **mises a jour** regulieres (meme imparfaites).
- Des **sauvegardes testees** (pas seulement "on a une sauvegarde quelque part") et isolees.
- Un minimum d'**alertes** qui veulent dire quelque chose.
- Un peu de **separation** : le site de test n'est pas le site de prod.

Une petite entreprise avec double authentification + sauvegardes testees + pas d'admin partout a deja ecarte une grosse partie des catastrophes. Acheter un outil cher "parce que le voisin l'a", sans personne pour le regarder, ca ne marche presque jamais. C'est une alarme de maison que personne n'ecoute.

## Prevenir, detecter, repondre

Pense a trois boucles.

1. **Prevenir** : fermer les portes (moins de surface attaquable).
2. **Detecter** : voir l'anormal assez tot.
3. **Repondre** : savoir quoi faire sans improviser a 2h du matin sur WhatsApp.

La securite "pro" ne promet pas zero probleme. Elle promet de **reagir vite et proprement**. Si tu ne fais que prevenir, tu decouvres souvent le souci via un client mecontent. Si tu detectes sans savoir repondre, tu regardes l'incendie avec un joli tableau de bord.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/cyber-pddr.svg" alt="Schema prevenir, detecter, repondre" class="schema-inline" width="640" />
  <figcaption>Trois boucles : prevenir, detecter, repondre — et mesurer pour ne pas se mentir.</figcaption>
</figure>

Pour une petite equipe, "repondre" peut tenir sur **une page** : qui coupe quoi, ou sont les sauvegardes, comment on previent les clients. Pas besoin d'un roman de 80 pages. Besoin d'un truc qu'on ouvrira vraiment sous stress.

## Mesurer sans se mentir

Quelques chiffres utiles :

- pourcentage de comptes importants avec double authentification **vraiment** activee
- delai pour reparer une faille grave exposee
- temps entre une alerte et la premiere action humaine
- taux de reussite du **dernier test** de restauration de sauvegarde

Si tu ne mesures que le nombre d'outils achetes, tu mesures ton budget pub tech, pas ta protection. Et si tu n'as jamais teste une restauration, ton "on peut tout recuperer en 4 heures" est de la science-fiction.

## Par ou commencer demain matin

Prends **une heure**. Liste tes trois trucs qui feraient le plus mal s'ils tombaient (CRM, boite mail, base clients, depot de code). Sur ces trois-la seulement : double authentification, droits admin, sauvegardes, exposition reseau. Le reste peut attendre.

Ensuite, note les trous que tu acceptes **consciemment**. Un vieux serveur qu'on ne peut pas mettre a jour tout de suite, un prestataire avec trop de droits. Accepter un risque en le notant, ce n'est pas grave. L'ignorer jusqu'a l'accident, si.

Dans la suite de la serie, on verra comment organiser un petit [SecOps](/blog/articles/secops-soc-fonctions-process.html), un [SIEM](/blog/articles/siem-log-management-detection.html) qui ne te noie pas, l'[EDR](/blog/articles/edr-xdr-endpoint-detection-response.html), et un vrai cycle de faiblesses a corriger. Pour l'instant, retiens juste ca : **menace ≠ faiblesse ≠ risque**, et une posture simple bien tenue bat une pile d'outils mal utilises. Toujours.
