# Chapitre 18 - Hygiene des secrets : jamais de cles dans Git

Un commit peut vivre longtemps. Il se copie sur les machines, les forks, les backups, les CI logs. Si tu commits une **cle** API, un mot de passe, un fichier `.env` rempli, tu as publie un **secret**. Meme si tu "effaces" le fichier au commit suivant, l'histoire le contient encore. Les robots scannent les depots publics en permanence. Les depots prives fuient aussi : fork demain, stagiaire apres-demain, capture d'ecran un jour. Chez DanielCraft, on prefere un projet un peu moins "pratique a cloner" qu'un projet qui fuit des cles.

Ce chapitre est non negociable. Pas un "nice to have". Pas un chapitre "si tu as le temps". Si tu ne retiens qu'une phrase du livre apres le flux : les secrets ne vivent pas dans Git.

:::retenir
Jamais de secrets dans Git. Invalide d'abord, nettoie ensuite. Un `git rm` seul ne suffit pas.
:::

## Ce qu'on ne commit pas

Fichiers `.env`, `.env.local`, cles privees SSH, fichiers `credentials.json`, dumps de base avec donnees reelles, exports de mots de passe, tokens de bot, certificats prives. Les exemples de config, oui. Les vraies valeurs, non. Un screenshot de dashboard cloud avec une cle visible dans une PR, non. Un `console.log` qui affiche le token, non. Un fichier de fixture "pour que ca marche chez toi" avec la vraie cle, non.

Lea a un jour commit un dump "anonyme" qui contenait encore des emails clients. Max a commit une cle "de dev" qui ouvrait trop. Sam a commit un `.pem` "temporairement". Trois scenes, une meme lecon : temporaire dans Git, c'est permanent dans l'histoire.

## .gitignore est ton ami

Dans le depot :

```text
.env
.env.*
!.env.example
```

Tu commits `.env.example` avec des fausses valeurs :

```text
API_KEY=remplace_moi
DATABASE_URL=postgres://user:pass@localhost:5432/app
```

Chaque developpeur copie vers `.env` en local et remplit. Le `.env` reste hors Git. **`.env.example`** est un contrat : il liste les variables necessaires sans valeurs sensibles. Un nouveau developpeur (ou toi sur une nouvelle machine) sait quoi remplir. Si l'exemple ment (variable manquante), l'onboarding souffre et quelqu'un recommit un vrai `.env` "pour aider". Garde l'exemple juste.

:::astuce
Commit `.env.example` avec des fausses valeurs. Ignore `.env`. Au premier jour d'un collegue, il copie, remplit, avance - sans jamais pousser de vrai secret.
:::

## Comment l'equipe partage les secrets

Pas via un commit "temporaire". Via un gestionnaire (coffre, secrets GitHub, variable d'environnement du serveur, outil d'equipe). Le canal "je te colle la cle sur Discord" est deja risque : prefere un outil qui expire, qui audit, qui restreint. La **CI** lit les secrets depuis les reglages du depot, pas depuis le code. Le fichier yaml decrit le job. Les valeurs sensibles vivent ailleurs.

En review, un oeil sur les fichiers suspects : `.pem`, `.env`, `id_rsa`, longs tokens dans le source. Un reviewer qui attrape ca avant le merge sauve des soirees. Les branches protegees et la CI n'empechent pas a elles seules un secret dans une PR. L'humain et `.gitignore` comptent. Approve fantome egal secret qui passe.

## Si le mal est fait

1. Revoque ou regenere la cle tout de suite chez le fournisseur (cloud, API, DB).
2. Enleve le secret du code actuel.
3. Considere l'historique : selon la gravite, filtre l'historique (outils specialises) ou traite le depot comme compromis pour cette cle.
4. Previens l'equipe. Transparence bat honte silencieuse.

La priorite absolue : invalider le secret. Un `git rm` seul ne suffit pas. "Je vais l'enlever au prochain commit" laisse le tresor dans le passe. Les scanners le trouvent. Les attaquants aussi.

:::attention
"C'est un depot prive, donc OK" est faux. Prive aujourd'hui, fork demain, fuite un jour. Revoque des qu'un secret a circule.
:::

## Exemple Max

Max ajoute l'envoi d'email. Le fournisseur donne une cle. Max met la cle dans `config.js` "pour tester". Il commit. Il pousse. La cle est publique sur le remote. Scenario cauchemar classique. La bonne version : `process.env.MAIL_API_KEY` (ou equivalent) plus `.env` ignore plus exemple dans `.env.example`. Cinq minutes de plus. Des semaines de moins a gerer un incident.

Lea, en review, a vu un long token dans un fichier JS. Elle a demande changes. Max a revoque, corrige, remercie. Ce n'etait pas un tribunal. C'etait un filet. Chez DanielCraft, on applaudit le reviewer qui attrape un secret comme on applaudit celui qui trouve un bug de paiement.

## Checklist avant le premier push d'une feature API

Est-ce que la cle est dans le code source ? Dans un screenshot de la PR ? Dans un log `console.log` ? Dans un fichier de fixture committe ? Si oui a l'une de ces questions, stop. Sors le secret. Regenere si elle a deja circule. Relis le diff une derniere fois avec les yeux "secret hunter". Cinq minutes ici epargnent une nuit blanche.

## Petite histoire

Sam a commit une cle "temporairement" un mardi. Mercredi, un bot a ouvert une issue "exposed credential". Jeudi, rotation de toutes les cles proches, audit, excuses. Vendredi, `.gitignore` renforce et phrase dans le README. L'equipe a gagne une cicatrice utile. Mieux vaut lire ce chapitre avant la cicatrice.

## Erreur classique

"C'est un depot prive, donc OK." Non. "Je vais l'enlever au prochain commit." L'histoire garde. "C'est juste une cle de dev." Souvent la cle de dev ouvre encore trop. Autre piege : coller la cle dans le titre de la PR ou dans un commentaire GitHub "pour que Max teste". Le commentaire reste. Le titre reste. Traite GitHub comme un lieu public avec memoire.

## En vrai

Audit rapide :

```bash
git ls-files | findstr /i "env pem key credential"
```

(sous Linux/mac : `git ls-files | grep -iE 'env|pem|credential'`)

Verifie `.gitignore`. Tourne les cles qui ont fuit ne serait-ce qu'une fois en local douteux. Regarde aussi les anciennes PR et les screenshots. L'hygiene depasse Git : c'est une posture.

## A toi

Ajoute (ou verifie) `.env.example` plus regles `.gitignore` sur ton depot de test. Ecris dans le README : "Jamais de secrets dans Git. Les cles vivent hors depot." Lis cette phrase a chaque nouvelle integration d'API. Puis respire. Tu viens de fermer une porte que beaucoup laissent ouverte.
