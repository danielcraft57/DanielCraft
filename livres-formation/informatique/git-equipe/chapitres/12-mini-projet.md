# Chapitre 12 - Mini-projet : simulation d'equipe

Assez de theorie separee. On colle les briques. Tu vas simuler une petite equipe sur un mini site : page d'accueil, page offres, formulaire de contact. Lea, Max, Sam (meme si tu joues les trois roles tout seul). But : vivre le **flux** complet une fois, proprement. Chez DanielCraft, un mini-projet fait avec les mains bat dix chapitres lus sans depot.

Vous livrez `v0.1.0` d'un site vitrine. Puis Lea ajoute une section tarifs sur la page offres. Max corrige un bug : le formulaire accepte un email invalide. Sam protege `main`, ajoute une CI minimale si possible, et publie `v0.2.0`. Tu peux tout faire sur un seul compte en changeant de branches et en ouvrant des PR. Idealement, un ami joue le reviewer.

:::retenir
L'objet du mini-projet, c'est le flux, pas le pixel perfect. Un bandeau moche versionne proprement bat une refonte poussee n'importe comment sur main.
:::

## Preparation

Cree un depot GitHub vide (ou local + remote). Clone. Sur `main`, pose un site minimal : `index.html`, `offres.html`, `contact.html`, un peu de CSS. Commit initial clair. Pousse `main`.

```bash
git switch -c main
# si besoin : premier commit deja sur main
git push -u origin main
```

Active une **protection** simple sur `main` : PR obligatoire (chapitre 7). Sans ce filet, tu rates une partie de l'exercice.

## Role Lea : feature tarifs

```bash
git switch main
git pull
git switch -c feature/section-tarifs
```

Ajoute la section. Commits clairs (contenu, puis style si tu veux). Pousse. Ouvre une PR avec but + comment tester. Fais reviewer (ami ou toi via autre oeil). Merge. Tire `main`.

## Role Max : fix email

Pendant ou apres Lea, Max part de `main` a jour :

```bash
git switch main
git pull
git switch -c fix/validation-email
```

Corrige la validation. Ajoute un test minuscule si tu peux (meme une fonction JS + un runner simple). PR. Review. Merge. Si la **CI** existe, regarde le vert. Si elle n'existe pas encore, Sam s'en occupe ensuite, ou tu l'ajoutes dans une PR `chore/ci-legere`.

## Role Sam : filets et release

Sam verifie que `main` est protegee. Sam ajoute une CI legere qui lance les tests sur les PR. Sam, apres les merges utiles :

```bash
git switch main
git pull
git tag -a v0.2.0 -m "Tarifs + validation email"
git push origin v0.2.0
```

Cree une Release GitHub avec trois lignes de notes. Option bonus : cherry-pick si tu as laisse trainer un fix urgent sur une branche longue. Autre bonus : introduis un bug, retrouve-le avec bisect, corrige, tague `v0.2.1`.

:::astuce
Chronometre. Une demi-journee suffit souvent. Note ce qui frotte : c'est le vrai cours.
:::

## Criteres "c'est reussi"

`main` n'a recu que des merges via PR. Les messages de commit sur les features sont lisibles. Au moins une review a eu lieu (meme simulee). Un tag `v0.2.0` existe. Tu peux expliquer a voix haute le chemin d'une idee jusqu'a la release. Une personne exterieure peut cloner, lire le README "Comment on travaille", et comprendre comment proposer un changement sans dix questions.

## Planning suggere (demi-journee)

0h00-0h30 : socle site + remote + protection main. 0h30-1h30 : role Lea (feature tarifs + PR + merge). 1h30-2h30 : role Max (fix email + test + PR). 2h30-3h15 : role Sam (CI minimale + tag v0.2.0 + notes). 3h15-3h30 : retro ecrite dans le README. Si tu es seul, enchaine les casquettes. Si vous etes trois, prenez les roles pour de vrai et chronometrez les attentes de review : ca enseigne le "repondre vite".

## Petite histoire

Lea a voulu peaufiner le design pendant l'atelier. Max lui a dit : "HTML minimal, on versionne le flux." Ils ont livre `v0.2.0` avant 16h. Sam a ecrit la retro : "protection activee trop tard, on l'active des le jour 1 la prochaine fois." Trois lecons dans une demi-journee. Chez DanielCraft, c'est exactement le but.

## Erreur classique

Tout faire directement sur `main` "pour aller plus vite" : tu rates l'exercice. Ou ouvrir une seule PR geante Lea+Max+Sam. Decoupe. Le mini-projet entraine le decoupage. Autre piege : construire un design system pendant l'atelier Git.

:::attention
Ne construis pas un design system ici. L'objet, c'est le flux d'equipe. HTML/CSS minimal suffit.
:::

## En vrai

Chronometre. Une demi-journee suffit souvent. Note ce qui a frotte : protection, conflits, description de PR. Ces frottements sont le cours. A la fin, une personne exterieure (ami, collegue) peut-elle comprendre votre README sans vous poser dix questions ? Si oui, vous avez reussi plus que "faire des commandes".

## A toi

A la fin, ecris un paragraphe "ce que notre equipe a decide" : flux, noms de branches, rebase ou merge, qui release. Colle-le dans le README. Le mini-projet devient votre contrat leger. Bonus : coche protection `main` + au moins une PR mergee + un tag. Trois coches, un vrai kit.

## Zoom : demi-journee, vrai contrat

Le but n'est pas un site joli. Le but, c'est un depot ou le prochain mardi sera plus calme. Lea a voulu peaufiner le design. Max a rappele le flux. Sam a note la retro. Chez DanielCraft, cette demi-journee vaut dix lectures du chapitre flux - a condition d'ecrire le contrat a la fin.
