# Chapitre 18 - Hygiene des secrets : jamais de cles dans Git

Un commit peut vivre longtemps. Il se copie sur les machines, les forks, les backups, les CI logs. Si tu commits une cle API, un mot de passe, un fichier `.env` rempli, tu as publie un secret. Meme si tu "effaces" le fichier au commit suivant, l'histoire le contient encore.

Ce chapitre est non negociable. Chez DanielCraft, on prefere un projet un peu moins "pratique a cloner" qu'un projet qui fuit des cles.

## Ce qu'on ne commit pas

Fichiers `.env`, `.env.local`, cles privees SSH, fichiers `credentials.json`, dumps de base avec donnees reelles, exports de mots de passe, tokens de bot, certificats prives.

Les exemples de config, oui. Les vraies valeurs, non.

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

Chaque developpeur copie vers `.env` en local et remplit. Le `.env` reste hors Git.

## Comment l'equipe partage les secrets

Pas via un commit "temporaire". Via un gestionnaire (coffre, secrets GitHub, variable d'environnement du serveur, outil d'equipe). Le canal "je te colle la cle sur Discord" est deja risque : prefere un outil qui expire, qui audit, qui restreint.

La CI lit les secrets depuis les reglages du depot, pas depuis le code.

## Si le mal est fait

1. Revoque ou regenere la cle tout de suite chez le fournisseur (cloud, API, DB).
2. Enleve le secret du code actuel.
3. Considere l'historique : selon la gravite, filtre l'historique (outils specialises) ou traite le depot comme compromis pour cette cle.
4. Previens l'equipe. Transparence > honte silencieuse.

La priorite absolue : invalider le secret. Un `git rm` seul ne suffit pas.

## Revue et secrets

En review, un oeil sur les fichiers suspects : `.pem`, `.env`, `id_rsa`, longs tokens dans le source. Un reviewer qui attrape ca avant le merge sauve des soirees.

Les branches protegees et la CI n'empechent pas a elles seules un secret dans une PR. L'humain et `.gitignore` comptent.

## Exemple Max

Max ajoute l'envoi d'email. Le fournisseur donne une cle. Max met la cle dans `config.js` "pour tester". Il commit. Il pousse. La cle est publique sur le remote. Scenario cauchemar classique. La bonne version : `process.env.MAIL_API_KEY` (ou equivalent) + `.env` ignore + exemple dans `.env.example`.

## Erreur classique

"C'est un depot prive, donc OK." Non. Prive aujourd'hui, fork demain, stagiaire apres-demain, fuite un jour. "Je vais l'enlever au prochain commit." L'histoire garde. "C'est juste une cle de dev." Souvent la cle de dev ouvre encore trop.

## En vrai

Audit rapide :

```bash
git ls-files | findstr /i "env pem key credential"
```

(sous Linux/mac : `git ls-files | grep -iE 'env|pem|credential'`)

Verifie `.gitignore`. Tourne les cles qui ont fuit ne serait-ce qu'une fois en local douteux.


## Checklist avant le premier push d'une feature API

Est-ce que la cle est dans le code source ? Dans un screenshot de la PR ? Dans un log `console.log` ? Dans un fichier de fixture committe ? Si oui a l'une de ces questions, stop. Sors le secret. Regenere si elle a deja circule.

## .env.example est un contrat

Il liste les variables necessaires sans valeurs sensibles. Un nouveau developpeur (ou toi sur une nouvelle machine) sait quoi remplir. Si `.env.example` ment (variable manquante), l'onboarding souffre et quelqu'un recommit un vrai `.env` "pour aider". Garde l'exemple juste.

## Secrets et captures d'ecran

En review, attention aux screenshots de dashboard cloud avec des cles visibles. Attention aux videos de demo. L'hygiene depasse Git : c'est une posture.


## A toi

Ajoute (ou verifie) `.env.example` + regles `.gitignore` sur ton depot de test. Ecris dans le README : "Jamais de secrets dans Git. Les cles vivent hors depot." Lis cette phrase a chaque nouvelle integration d'API.
