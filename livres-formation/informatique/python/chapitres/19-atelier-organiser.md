# Chapitre 19 - Atelier : organiser son code

Quand ca grandit, on coupe en fonctions (et parfois en classes). Pas pour faire joli. Pour retrouver ton fichier dans deux semaines sans maudire ton "toi du passe". Chez DanielCraft, l'organisation est une competence de debutant, pas un luxe de senior. Lea decoupe des qu'un script depasse une idee. Max a appris apres avoir tout mele. Sam note la clarte autant que le score du quiz. Trois chemins, meme conclusion : un nom clair et une responsabilite par fonction battent un monstre de 120 lignes.

Objectif : reprendre ton quiz et le rendre lisible. Duree : 30 a 45 minutes. Materiel : ton quiz existant (mini-projet) ou un quiz neuf de trois questions. Pas besoin d'un framework. Besoin d'un fichier que tu oses decouper.

## Ce que ce n'est pas

Ce n'est pas "creer dix fichiers pour trois lignes". Ce n'est pas non plus une architecture d'entreprise. Ce n'est pas obligatoire d'utiliser des classes si des fonctions suffisent. Une fonction / methode = une responsabilite. `poser` pose. `main` organise. Point. Et ce n'est surtout pas "renommer sans faire tourner". Chaque decoupage se valide par un lancement.

Imagine un tiroir unique ou tout est mele : questions, score, affichage, sauvegarde. Tu ouvres, tu cherches, tu pestes. Maintenant imagine trois tiroirs : `questions`, `jeu`, `main`. Tu trouves. Tu ajoutes une question sans casser le score. Lea visualise des dossiers clients. Max visualise des pieces detachees de devis. Sam visualise des fiches eleves. Chez DanielCraft, on mesure l'organisation a une question : "si tu reviens dans deux semaines, tu comprends encore ?"

## Version fonctions

```python
def poser_question(texte, bonne):
    rep = input(texte + " ").strip().lower()
    if rep == bonne:
        print("OK")
        return True
    print("Non, c'etait", bonne)
    return False


def main():
    score = 0
    if poser_question("Capitale de la France ?", "paris"):
        score += 1
    if poser_question("2 + 2 = ?", "4"):
        score += 1
    print("Score :", score)


if __name__ == "__main__":
    main()
```

Lis a voix haute. `poser_question` pose. `main` enchaine. Si tu ajoutes une question, tu touches surtout `main`. C'est ca, le gain.

## Pourquoi `if __name__ == "__main__"` ?

Ca veut dire : "lance `main()` seulement si on execute ce fichier directement". Utile quand tu importeras ce fichier ailleurs. Lea l'ajoute par reflexe. Sam l'explique avec un import reel en demo. Tu n'as pas a tout comprendre du mecanisme interne aujourd'hui. Tu as a prendre l'habitude. Plus tard, quand tu importeras `poser_question` dans un test, tu seras content que le quiz ne se lance pas tout seul.

## Version classe Question

```python
class Question:
    def __init__(self, texte, reponse):
        self.texte = texte
        self.reponse = reponse

    def poser(self):
        rep = input(self.texte + " ").strip().lower()
        ok = rep == self.reponse
        print("OK" if ok else f"Non : {self.reponse}")
        return ok


def main():
    quiz = [
        Question("Capitale de la France ?", "paris"),
        Question("2 + 2 = ?", "4"),
        Question("Langage de ce livre ?", "python"),
    ]
    score = sum(1 for q in quiz if q.poser())
    print(f"Score : {score}/{len(quiz)}")


if __name__ == "__main__":
    main()
```

La classe n'est pas obligatoire pour valider l'atelier. Elle montre une autre facon de ranger la meme idee. Si les fonctions te suffisent, reste-y. Si tu sens que "une question" est un objet, passe a la classe.

## Decouper en fichiers (idee)

Tu peux mettre les donnees ou la classe `Question` dans `questions.py`, la logique dans `jeu.py`, et le point d'entree dans `main.py`. Meme sur un petit projet, ca clarifie. Max a resiste, puis a avoue que c'etait plus simple a montrer a son neveu : "la, les questions ; la, le jeu". Lea le fait des qu'un client peut revenir dans six mois. Sam note la clarte avant la ruse.

## Petite histoire

Lea a rouvert un script "organise" deux mois plus tard et a sourit. Elle a ajoute une question en trente secondes. L'autre script "tout en vrac" lui a coute une heure. Sam projette les deux devant la classe. Le message passe sans sermon. Chez DanielCraft, on ne vend pas l'organisation comme une morale. On la vend comme du temps retrouve. Max a compris le jour ou il a du expliquer son fichier a quelqu'un d'autre. Expliquer force a ranger.

## Erreur a eviter

Decouper trop tot (sur-abstraction). Ou trop tard (copier-coller de blocs). Renommer sans faire tourner. Melanger affichage, donnees et regles dans la meme fonction de 80 lignes. Une responsabilite, un nom clair, un test rapide. Autre piege : creer cinq fichiers vides "pour faire pro" sans y mettre de vrai decoupage. L'organisation sert le lecteur. Pas l'ego.

## Livrable

Ton quiz decoupe avec au moins 2 fonctions. Bonus : classe `Question`. Bonus 2 : score en JSON. Un court `README` de 5 lignes : comment lancer. Sans README, ton futur toi cherchera encore "c'est quel fichier deja ?".

## En vrai

Rouvre le fichier demain matin sans te relire la veille. Si tu comprends en deux minutes, c'est bien organise. Sinon, renomme et decoupe encore un peu. Cette epreuve du lendemain est plus honnete qu'un sentiment de fierte le soir meme.

## A toi

Fais le decoupage ce soir. Demain, ajoute une seule amelioration (JSON, shuffle, ou fichier separe). Note le temps gagne. C'est ca, le retour sur investissement du rangement. Puis prepare-toi pour le quiz final : tu as les gestes, il reste a verifier les reflexés.
