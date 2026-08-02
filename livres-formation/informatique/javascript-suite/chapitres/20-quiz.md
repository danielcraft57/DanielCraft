# Quiz final

Pas de piege. L'idee : verifier que tu peux avancer sur un petit projet reel sans paniquer devant fetch, JSON ou un formulaire. Relis un chapitre si une question te bloque. Lea fait passer ce quiz avant de confier un vrai ticket client front. Sam l'utilise en fin de module. Max l'a refait une fois pour se rassurer. Chez DanielCraft, un quiz sert a reperer les trous, pas a humilier.

Coche sans tricher. Une premiere passe honnete vaut mieux qu'un score maquille. Si tu bloques, marque et continue. Tu reviendras. Le but, c'est la carte des chapitres a rouvrir.

:::astuce
Fais le quiz, note ton score, rejoue dans une semaine apres un mini projet. Le vrai progres se voit a la deuxieme passe.
:::

## Questions

1. Pourquoi appelle-t-on souvent preventDefault() sur un submit de formulaire ?
- A) Pour colorier le bouton
- B) Pour empecher l'envoi / rechargement par defaut du navigateur
- C) Pour vider le localStorage

2. JSON.stringify sert surtout a :
- A) Transformer un objet JS en texte JSON
- B) Afficher une image
- C) Creer un fichier CSS

3. Que fait await devant un fetch ?
- A) Il ignore la reponse
- B) Il attend la reponse avant de continuer dans la fonction async
- C) Il compile le HTML

4. Pourquoi verifier reponse.ok ?
- A) Parce que fetch ne leve pas toujours d'erreur sur un 404
- B) Parce que JSON est obligatoire
- C) Parce que le DOM l'exige

5. Dans un module, export sert a :
- A) Supprimer une fonction
- B) Rendre une fonction (ou valeur) importable ailleurs
- C) Lancer le serveur

6. CORS, en une idee :
- A) Un langage de programmation
- B) Une regle navigateur sur les requetes entre origines differentes
- C) Un type de variable

7. Le debounce sert surtout a :
- A) Attendre un petit silence avant d'agir (ex: recherche)
- B) Chiffrer les mots de passe
- C) Remplacer CSS

8. Ou placer le try/catch autour d'un chargement async ?
- A) Autour de l'appel await / logique de chargement
- B) Uniquement autour de console.log
- C) Autour de la balise html

9. Pour charger un script module dans HTML, on ecrit souvent :
- A) script type="module" src="main.js"
- B) script type="css" src="main.js"
- C) module href="main.js"

10. Un bon message d'erreur utilisateur ressemble a :
- A) TypeError: undefined is not a function
- B) Impossible de charger. Reessaie dans un instant.
- C) Une page blanche

11. response.json() renvoie :
- A) Directement un nombre magique
- B) Une promesse qui donne les donnees parsees
- C) Un fichier PDF

12. Organiser un projet, regle simple :
- A) Tout dans un seul fichier de 2000 lignes
- B) Un role clair par fichier
- C) Copier-coller le meme fetch partout

## Corriges

1-B, 2-A, 3-B, 4-A, 5-B, 6-B, 7-A, 8-A, 9-A, 10-B, 11-B, 12-B.

Si tu as 9/12 ou plus : tu es pret pour les petits projets reels (formulaire, liste API, modules). Sinon, relis les chapitres lies (formulaires, erreurs reseau, modules, CORS), puis refais le quiz apres une semaine de pratique.

## Petite histoire

Lea a rate `reponse.ok`. Elle a casse l'URL volontairement le soir meme et a vu le catch. Max a confondu stringify et parse : il a rejoue l'atelier JSON dix minutes. Sam affiche le score moyen sans nommer personne : "on revoit modules et CORS demain". Trois reactions, meme message : le quiz est une carte.

## Questions bonus (auto-eval)

13. Cite deux ingredients obligatoires d'un fetch POST JSON. 14. Difference entre catch reseau et !reponse.ok. 15. Pourquoi tester en file:// pose souvent probleme avec fetch et modules. Reponses libres : compare a tes chapitres 7, 8, 9.

## Note de rythme

Prends le temps. DanielCraft forme des gens qui livrent. Si tu as rate des questions, c'est un plan de relecture, pas un echec. Refais le mini-projet, puis le quiz.

## En vrai

Coche tes mauvaises reponses. Ouvre le chapitre lie. Refais un mini geste : un fetch casse, un preventDefault, un export. Cinq minutes. Un trou a la fois.

## A toi

Ecris tes trois questions ratees. A cote, une phrase "ce que je confonds". Dans sept jours, rejoue seulement ces trois. Le vrai score, c'est la deuxieme passe.

## Pour aller plus loin sans te perdre

Reviens a ce quiz dans un mois apres un vrai petit projet perso. Note ton score. L'objectif n'est pas 12/12 par coeur, c'est de ne plus bloquer sur fetch et JSON au quotidien.
