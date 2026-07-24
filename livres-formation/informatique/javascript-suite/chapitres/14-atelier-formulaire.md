# Chapitre 14 - Atelier : formulaire robuste

Objectif : un formulaire contact (nom, email, message) qui refuse l'envoi si un champ manque, et qui explique clairement quoi corriger.

## Etapes

1. Cree `index.html` avec un formulaire, trois champs, un bouton, une zone `#erreurs`.
2. Ecoute `submit`. Appele `preventDefault()` tout de suite.
3. Lis les valeurs avec `.value.trim()`.
4. Construis une liste d'erreurs (tableau de phrases).
5. Si le nom est vide : "Indique ton nom."
6. Si l'email n'a pas de `@` : "Email incomplete."
7. Si le message a moins de 10 caracteres : "Message trop court."
8. Affiche les erreurs dans `#erreurs`. Si aucune erreur, affiche "Formulaire pret (simulation d'envoi)."

## Criteres de reussite

- Sans JS, le navigateur ne doit pas naviguer nulle part a cause du submit (donc preventDefault marche).
- Les messages sont en francais simple.
- Tu peux envoyer seulement quand tout est valide.
- Tu logs en console l'objet `{ nom, email, message }` une fois valide (simulation).

## Bonus

Desactive le bouton pendant une fausse attente d'une seconde (`setTimeout`), puis reactive-le. Ca prepare le vrai envoi reseau.

## Piege

Ne te contente pas de `alert()`. Les alertes agacent. Un message dans la page est plus pro, meme pour un exercice.
