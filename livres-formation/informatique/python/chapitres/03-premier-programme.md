# Chapitre 3 - Ton premier programme

Ouvre `salut.py` et ecris une seule ligne claire :

```python
print("Salut Python")
```

Lance ensuite :

```bash
python salut.py
```

Si tu vois `Salut Python`, bravo. Ce n'est pas un gadget. C'est le premier pont solide entre ton texte et l'ecran. Chez DanielCraft, on traite ce moment comme une ceremonie discrete : tu as donne un ordre, la machine a obei. Lea sourit encore la premiere fois. Max a dit "c'est tout ?". Sam a repondu : "c'est le debut de tout".

A partir d'ici, chaque chapitre ajoute une brique. Tu n'as pas besoin de tout inventer. Tu as besoin de retaper, changer une valeur, relancer, observer.

## Ce que ce n'est pas

Un premier programme, ce n'est pas une application complete. Ce n'est pas non plus "trop simple pour compter". Beaucoup de gens veulent un jeu, un site, un bot des le jour un. Ils se noient. Ici, on commence par afficher. Ensuite on demande. Ensuite on decide. Ensuite on repete. La progression est volontairement lente - et efficace.

Ce n'est pas non plus "copier-coller une fois et passer". Si tu ne retapes pas, ton doigt n'apprend pas, et ton oeil ne voit pas les petites fautes. Retape. Change la phrase. Relance.

**print**(...) = "montre ca a l'ecran". Le texte va entre guillemets. Les nombres peuvent vivre sans guillemets. Tu peux melanger plusieurs choses separees par des virgules : Python ajoute un espace entre. Plus loin, les **f-strings** collent des variables dans une phrase lisible. **input** demande quelque chose a l'humain. Attention : `input` renvoie toujours du texte, meme si tu as tape `12`.

:::retenir
`print` montre. `input` demande. Les f-strings collent des valeurs dans une phrase claire.
:::

## print, f-strings, commentaires

```python
print("Coucou")
print(2 + 2)
print("2 + 2 =", 2 + 2)
```

Les f-strings (pratique quotidienne) :

```python
prenom = "Leo"
age = 12
print(f"Je m'appelle {prenom} et j'ai {age} ans")
```

Le `f` devant la chaine laisse coller des variables avec `{...}`. Plus lisible que coller avec `+` partout. Lea les utilise dans presque tous ses scripts clients. Max les a adoptes pour ses messages de devis.

**Commentaires** :

```python
# Ceci est une note pour toi. Python l'ignore.
print("Je compte")  # commentaire en fin de ligne
```

Ecris des commentaires utiles, pas "ici j'affiche". Plutot : pourquoi tu fais un truc pas evident. Sam interdit les commentaires qui repetent le code mot pour mot.

## input : demander quelque chose

```python
prenom = input("Ton prenom ? ")
print("Salut", prenom)
print(f"Enchante, {prenom} !")
```

`input` attend que tu ecrives puis Entree. Souvent, on nettoie :

```python
reponse = input("Ville ? ").strip()
```

**strip()** enleve les espaces avant/apres. Utile. Les gens tapent souvent un espace sans le voir. Max a passe dix minutes a chercher pourquoi `"Lyon "` n'egalait pas `"Lyon"`. `strip()` a regle le mystere.

:::astuce
Retape chaque exemple a la main. Changer une seule phrase et relancer vaut mieux que coller dix tutos.
:::

## Petite histoire

Lea a ecrit un mini script de presentation pour un atelier : prenom, hobby, ville. Elle l'a lance devant un client pour montrer "voir, c'est lisible". Le client a sourit. Pas parce que c'etait genial techniquement. Parce que c'etait comprehensible. Chez DanielCraft, on aime ce genre de preuve : le code sert un humain, pas l'inverse.

Sam fait retaper l'exemple a chaque eleve. Ceux qui collent bloquent plus tard. Ceux qui tapent avancent plus vite au chapitre variables. La lecon n'est pas morale. Elle est musculaire.

## Erreur classique

Oublier les guillemets :

```python
print(Salut)  # erreur : Salut n'existe pas comme variable
```

Le message d'erreur pointe souvent la ligne. Lis-la. Autre classique : confondre le fichier ouvert dans l'editeur et le fichier lance dans le terminal. Tu modifies `salut.py`, mais tu lances `test.py`. Relis le nom. Respire. Relance.

## Exemple complet

```python
# mini presentation
prenom = input("Prenom ? ").strip()
hobby = input("Hobby ? ").strip()
print(f"Salut {prenom}. Cool pour {hobby}.")
print("Fin du programme.")
```

Retape-le. Change les phrases. Ajoute une troisieme question si tu veux. Puis seulement, passe a "A toi".

## En vrai

Retape l'exemple sans copier-coller. Change les phrases. Relance. Regarde. Si une erreur apparait, ne ferme pas le terminal en panique : lis la derniere ligne, corrige, relance. C'est le vrai sport du debutant.

## A toi

Demande le prenom et l'age (age en texte pour l'instant). Affiche : `Bonjour, <prenom> ! Tu as <age> ans.` avec une f-string. Bonus : ajoute une 3e question (ville ou animal prefere) et affiche une mini bio en 2 lignes.

## Zoom : texte vs nombre

Pour l'instant, l'age reste du texte. `"12" + "1"` donnerait `"121"`, pas `13`. Au chapitre types, tu convertiras avec `int(...)`. Ici, le but est plus simple : parler avec `print` et `input` sans te noyer. Une competence a la fois. Chez DanielCraft, on appelle ca "ne pas empiler les mysteres".
