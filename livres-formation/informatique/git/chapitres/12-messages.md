# Chapitre 12 - De bons messages de commit

Un bon message sauve ton futur toi.
Et ton equipe.

## Regle simple

- Premiere ligne : resume court (50-72 caracteres ideaux)
- Verbe a l'imperatif : "Ajouter", "Corriger", "Clarifier"
- Explique le **pourquoi** si ce n'est pas evident

## Oui

```text
Corriger le total TTC (oubli de la TVA)
Ajouter la page contact
Retirer le fichier .env du suivi
```

## Non

```text
update
fix
wip
asdf
final final 2
```

## Corps optionnel

```bash
git commit -m "Corriger le calcul du panier" -m "Le total ignorait les codes promo. Desormais appliques avant TVA."
```

## Conventional Commits (apercu)

Tu verras parfois :

```text
feat: ajouter export PDF
fix: corriger lien casse du sommaire
docs: preciser l'install Windows
```

Utile en equipe. Pas obligatoire pour apprendre.

## Une idee = un commit ?

Idealement : un commit = une intention.
Pas "j'ai change 40 fichiers sans rapport".
Pas non plus 40 micro-commits illegibles.
Le juste milieu vient avec l'experience.

## A toi

Reecris ces messages pourris en bons messages :
1. `update`
2. `fix stuff`
3. `aaa`

## En vrai, sur le terrain

Lis ton `git log --oneline`.
Si tu ne comprends plus un message d'hier, renomme ta facon d'ecrire.

## Mini defi

Fais 3 commits sur ton carnet avec des messages "pro".
## Exemple de fil propre

```text
Initialiser le projet
Ajouter la page d'accueil
Corriger le lien du menu mobile
Ignorer le fichier .env
Documenter l'installation dans le README
```

Tu peux lire ca dans 10 secondes et comprendre l'histoire.
C'est ca, le but.
