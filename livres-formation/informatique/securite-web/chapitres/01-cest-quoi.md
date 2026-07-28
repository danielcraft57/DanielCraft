# Chapitre 1 - C'est quoi la securite web ?

La **securite web**, pour un debutant, ce n'est pas un badge "hacker ethique" ni une suite d'outils chers. C'est un ensemble d'**habitudes** qui reduisent les accidents : comptes solides, trajet HTTPS, liens regardes deux fois, mises a jour faites, sauvegardes testees, droits limites, entrees de formulaires controlees. Chez DanielCraft, on enseigne la defense comme on enseigne le reste : petit, clair, testable. Lea protege un site artisan. Max a compris le jour ou un meme mot de passe a "saute" sur trois comptes. Sam dit a ses eleves : "Tu n'as pas a tout savoir. Tu as a freiner juste."

Ce livre reste **defense only**. On apprend a reconnaitre, a prevenir, a cocher une checklist. On n'ecrit pas d'exploits, pas de recettes d'attaque, pas de payloads. Si quelqu'un te promet "la faille en cinq minutes", ce n'est pas ce parcours. Ici, tu construis des freins.

:::retenir
Securite web debutant = habitudes repetables qui limitent les degats. Pas de panique. Pas d'attaque a reproduire.
:::

## Ce que ce n'est pas

Ce n'est pas de la cryptographie avancee. Ce n'est pas un audit pen-test. Ce n'est pas le RGPD complet (on en donne l'idee). Ce n'est pas "installer vingt plugins et dormir". Un plugin mal tenu peut ouvrir une porte. Ce n'est pas non plus "le cadenas HTTPS = site honnete" : HTTPS protege le trajet, pas ton jugement.

## Ce que tu vas savoir faire

A la fin, tu sauras expliquer les menaces courantes sans jargon, choisir une politique de mots de passe, lire un cadenas HTTPS sans magie, freiner face au phishing, planifier mises a jour et sauvegardes, limiter les permissions, comprendre l'idee des injections (validation, requetes preparees) sans jamais exploiter, securiser un formulaire, savoir ce que font sessions et cookies, minimiser les donnees perso, et livrer une checklist pour un petit site. Niveau base. Actionnable demain matin.

## Comment lire ce livre

Lis dans l'ordre au debut. Les premiers chapitres posent le sol : idee, menaces, mots de passe, HTTPS, phishing. Puis le quotidien : maj, sauvegardes, permissions. Ensuite le cote "entrees" : injections (idee), formulaires, sessions, RGPD (idee). Le mini-projet assemble. Les ateliers font faire. Le quiz verifie. A chaque fin, un "A toi". Fais-le. Cinq minutes actives battent une lecture passive.

## Petite histoire

Lea livrait un site vitrine. Le client a clique un mail "votre domaine expire demain" et a presque colle son mot de passe admin. Lea a freine : "On tape l'URL du registrar soi-meme." Max, lui, utilisait `Artisan2020!` partout. Une fuite ailleurs a donne acces a sa boite mail. Sam a dit : "Unique + gestionnaire. Point." Chez DanielCraft, ces histoires ne servent pas a faire peur. Elles servent a installer un frein.

## Erreur classique

Croire que la securite commence par un outil miracle, ou attendre "plus tard" parce qu'on n'est "pas une cible". Les petits sites sont des cibles faciles precisement parce qu'ils sont negliges. Autre piege : tout apprendre d'un coup et ne rien appliquer. Une habitude bat dix intentions.

:::attention
Ce livre ne montre jamais comment attaquer. Si une section te demande d'executer une "preuve d'attaque", ce n'est pas DanielCraft.
:::

## En vrai

Sur une feuille, note trois comptes critiques (mail, hebergeur, admin site) et une chose que tu feras cette semaine pour chacun (mot de passe unique, 2FA, verification URL). Garde ce papier pour le mini-projet.

## A toi

Ecris en trois phrases : (1) ce que tu proteges en priorite, (2) ce que tu acceptes d'apprendre d'abord, (3) ce que tu refuses (exploits, recettes d'attaque). Chez DanielCraft, ce petit brief vaut plus qu'une heure de videos floues.
