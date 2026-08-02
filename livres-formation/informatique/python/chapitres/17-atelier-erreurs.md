# Chapitre 17 - Atelier : lire les erreurs

Le terminal parle. Apprends a l'ecouter. Une erreur, c'est un GPS, pas une insulte. Chez DanielCraft, cet atelier vaut presque autant qu'un chapitre de syntaxe : si tu sais lire la derniere ligne, trouver le numero, corriger le plus petit truc, puis relancer, tu deviens autonome. Lea gagne des heures comme ca. Max a arrete d'envoyer des captures floues a Sam. Sam exige la methode avant l'aide. Trois attitudes, meme muscle : diagnostic avant bricolage.

Objectif : reconnaitre les erreurs courantes et reparer sans tout reecrire. Duree : 25 a 40 minutes. Materiel : ton quiz ou un petit script + le terminal. Pas besoin d'internet. Pas besoin d'un framework. Besoin de calme et d'une seule hypothese a la fois.

## Ce que ce n'est pas

Ce n'est pas un catalogue a memoriser par coeur. Ce n'est pas non plus "attraper toutes les erreurs avec try" avant de les comprendre. Lis d'abord. Protege ensuite. Ce n'est pas une competition de vitesse : un atelier fait a fond bat trois ateliers survoles. Et ce n'est surtout pas "demander de l'aide sans citer la derniere ligne". Chez DanielCraft, on forme des gens qui livrent un diagnostic, meme petit.

Tu es medecin du code. Le symptome, c'est le message rouge. Le type d'erreur, c'est la famille de maladie. Le numero de ligne, c'est l'endroit ou ca fait mal. Ta premiere action n'est pas d'operer au hasard. C'est de lire, localiser, changer une seule chose, retester. Lea visualise un GPS. Max visualise un devis casse qu'il relit ligne par ligne. Sam visualise un eleve qui apprend a se debrouiller avant d'appeler.

## Les familles a reconnaitre

NameError : tu utilises un nom inconnu. Souvent une faute de frappe : `scroe` au lieu de `score`. TypeError : tu melanges mal les types, ex. `"3" + 1`. ValueError : conversion impossible, ex. `int("bonjour")`. IndexError / KeyError : tu sors d'une liste ou tu demandes une cle absente.

```python
liste = [1, 2]
print(liste[5])          # IndexError
d = {"a": 1}
print(d["b"])            # KeyError
```

IndentationError / SyntaxError : deux points `:` oublie, decalage foireux, parenthese non fermee. FileNotFoundError : mauvais chemin, mauvais dossier, fichier pas encore cree. Tu n'as pas a tout retenir. Tu as a reconnaitre le nom, puis agir.

## Methode DanielCraft

Lis d'abord la derniere ligne de l'erreur (le type). Va au numero de ligne. Corrige le plus petit truc, puis relance. Si besoin, entoure avec `try/except` - mais comprends d'abord. Une seule hypothese a la fois. Si tu changes dix choses, tu ne sauras plus ce qui a reparation. Note en une phrase ce que le message t'a dit. Cette note devient ton muscle.

## Exercice 1 - Syntaxe (8 min)

Casse volontairement ton quiz (enleve un `:`). Lance. Lis l'erreur. Note le type. Repare. Relance. Ecris une ligne : "ce que le message m'a dit". Si tu sautes la note, tu rates la moitie de l'atelier.

## Exercice 2 - ValueError (10 min)

Fais un `int(input(...))` et tape `abc`. Lis. Puis protege avec `try/except` comme au chapitre 15. Redemande jusqu'a obtenir un entier. Verifie aussi qu'un vrai nombre passe. Les deux chemins comptent.

## Exercice 3 - Fichier (10 min)

Ouvre un fichier qui n'existe pas. Attrape `FileNotFoundError`. Affiche un message propre. Bonus : cree le fichier s'il manque, avec un contenu par defaut. Lea adore ce bonus : l'outil devient accueillant au lieu d'exploser.

## Exercice 4 - Index / cle (8 min)

Provoque un IndexError et un KeyError. Corrige avec un test de longueur / `.get`. Ne te contente pas de "ca marche" : explique pourquoi ca cassait. Sam exige l'explication orale. Max se la fait a lui-meme dans le terminal.

## Petite histoire

Lea envoyait a Sam des captures floues : "ca marche pas". Sam repondait : "derniere ligne ?". Elle a appris a coller le type d'erreur. Le diagnostic est passe de vingt minutes a deux. Max, lui, changeait trois variables a la fois et ne savait plus quoi avait reparation. Depuis, une hypothese, un test. Chez DanielCraft, on repete cette scene parce qu'elle change des carrieres debutantes plus vite qu'une nouvelle syntaxe.

## Livrable

Un fichier `atelier-erreurs.md` avec : 4 types d'erreurs nommes, une capture ou copie de message, 5 lignes de lecons. Sans livrable, le cerveau classe ca comme "lu", pas comme "su". Range-le a cote de ton quiz. Tu le rouvriras.

## Erreur a eviter

Changer dix variables a la fois. Fermer le terminal sans lire. Demander de l'aide sans citer la derniere ligne de l'erreur. Croire que `try/except` remplace la comprehension. Autre piege : recopier une "solution Stack Overflow" sans comprendre le type d'erreur chez toi. Le message local reste roi.

## En vrai

Prends un vieux script. Casse-le volontairement trois facons differentes. Repare. Tu entraines le muscle. C'est le vrai atelier. Si tu n'as pas de vieux script, casse volontairement le quiz du mini-projet. Meme effet.

## A toi

Fais les quatre exercices. Puis explique a voix haute, comme a Max ou Lea, la difference entre TypeError et ValueError. Si tu y arrives sans notes, c'est bon signe. Ecris ensuite le livrable. Cinq minutes d'ecriture solidifient une heure de lecture.
