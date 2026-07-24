# Chapitre 19 - Atelier : organiser son code

Quand ca grandit, on coupe en fonctions (et parfois en classes).

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

## Pourquoi `if __name__ == "__main__"` ?

Ca veut dire : "lance `main()` seulement si on execute ce fichier directement".
Utile quand tu importeras ce fichier ailleurs.

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

## Decouper en fichiers (idee)

- `questions.py` : donnees ou classe `Question`
- `jeu.py` : logique
- `main.py` : point d'entree

Meme sur un petit projet, ca clarifie.

## Regle simple

Une fonction / methode = une responsabilite.
`poser` pose.
`main` organise.

## A toi

Reprends ton quiz.
1. Decoupe avec au moins 2 fonctions
2. Bonus : passe en classe `Question`
3. Bonus 2 : sauve le score en JSON

## Check

Si tu rouvres le fichier dans 2 semaines et tu comprends encore :
c'est bien organise.
