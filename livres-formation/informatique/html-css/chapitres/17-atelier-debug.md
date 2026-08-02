# Chapitre 17 - Atelier debug : la page est cassee

Ca arrive. Souvent. Et c'est normal. Ici, on apprend a chercher sans paniquer. Le **debug**, ce n'est pas la preuve que tu es nul. C'est le metier. Une page qui casse, c'est une page qui te parle : quelque chose ne va pas, et tu vas trouver ou. Chez DanielCraft, on dit clairement : les gens qui avancent supportent de chercher. Ceux qui abandonnent au premier bug ne decouvrent jamais la satisfaction de reparer seuls.

Lea passe une part non negligeable de sa semaine a lire des chemins faux et des classes mal orthographiees. Ce n'est pas glamour, mais c'est paye. Max a gagne en confiance le jour ou il a reussi a reparer sa page vitrine seul. Sam transforme les paniques en methode. Objectif : casser volontairement, puis reparer avec une checklist. Duree : 25 a 40 minutes. En 2026, quand quelqu'un dit "je debug", il parle souvent de cette hygiene. Tu restes le pilote. L'erreur est un signal.

:::retenir
Une hypothese. Un test. Puis la suivante. Jamais dix changements d'un coup.
:::

## Ce que ce n'est pas

Ce n'est pas "lire la console JavaScript" en premier (on est surtout HTML/CSS ici). Ce n'est pas changer dix choses a la fois. Ce n'est pas recopier tout internet. Une hypothese, un test, une conclusion. Puis la suivante. Lea appelle ca "chirurgie", pas "demolition". Sam chronometre la panique puis la methode : la deuxieme gagne toujours.

Tu es medecin de page web. Tu observes le symptome : style absent, image cassee, menu folle, scroll horizontal. Tu demandes : qu'est-ce qui a change en dernier ? Tu verifies les organes vitaux : doctype, balises fermees, chemins, link CSS, classes qui matchent. Tu simplifies : tu commentes un gros bloc, tu retestes. Tu ne remplaces pas le patient entier au premier doute. Max prefere ca aux soirees a tout recommencer. Lea aussi.

## Methode en 5 etapes

1. Relis la derniere chose que tu as changee.
2. Observe le resultat. Ouvre F12 si besoin.
3. Verifie les balises ouvertes et fermees.
4. Verifie les chemins : `href`, `src`, `<link>` CSS.
5. Simplifie : commente un gros bloc, reteste, isole le coupable.

:::attention
Casse volontairement, puis repars. Tu entraines le calme sans la pression d'un vrai client qui attend.
:::

## Checklist HTML

`<!DOCTYPE html>` present. `lang="fr"`. `charset` UTF-8 et **viewport** dans le head. Balises fermees. Un seul **`h1`**. Ancres du menu qui matchent des `id` reels. Labels de formulaire lies aux champs. Chez DanielCraft, cette checklist sauve des heures.

## Checklist CSS

`<link rel="stylesheet" href="style.css">` present, nom exact. Classe HTML = classe CSS (casse comprise). Point-virgules. **`box-sizing: border-box`** si les largeurs debordent. Piege classique : `Style.css` vs `style.css`. Sur Windows ca peut marcher. Ailleurs, ca casse. Noms simples, minuscules, partout.

## Exercices

Exercice 1 (10 min) : enleve une balise fermante `</section>`. Observe. Repare.

Exercice 2 (10 min) : renomme ton CSS sans mettre a jour le `<link>`. Observe la page nue. Repare.

Exercice 3 (10 min) : casse le `src` d'une image. Lis le **`alt`**. Corrige.

Exercice 4 (optionnel) : `.menu` en HTML et `.Menu` en CSS. Comprends. Uniformise.

## Petite histoire

Lea raconte qu'un junior a reecrit tout un fichier CSS pour un point-virgule manquant. Elle lui a appris : "c'est une ligne, pas un fichier entier". Max a cherche deux heures un style absent : le `<link>` etait commente. Sam chronometre panique puis methode. Trois scenes, une posture : calme, checklist, petit fix.

## Erreur classique

Changer dix choses a la fois. Tu ne sauras plus ce qui a marche. Un changement, un test, une note. Ecris ce que tu as appris apres chaque bug : symptome, cause, correction, lecon. Sans livrable, le cerveau classe ca comme "galere". Avec livrable, comme "competence". Autre piege : tout effacer pour recommencer. Rarement necessaire. Souvent panique.

## En vrai

Refais l'atelier sur une copie de ta page perso. Casse trois choses differentes. Repare avec la checklist. Chronometre-toi : tu dois aller plus vite qu'au premier essai. Le calme s'installe avec la repetition. Pas magie. Habitude.

## A toi

Cree un fichier notes `atelier-debug.md` (ou papier) avec : symptome, cause, correction, lecon pour chaque exercice. Refais l'atelier une semaine plus tard sans relire tes notes d'abord. Si tu vas plus vite, tu as integre. Sinon, recommence. DanielCraft prefere la repetition active au binge de tutos oublies le lendemain.
