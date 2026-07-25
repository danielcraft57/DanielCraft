# Chapitre 2 - Installer et ecrire Python

Avant de coder, il te faut un Python qui repond vraiment. Pas un logo sur un site. Une commande dans le **terminal** qui affiche un numero de version. Sur Windows, le chemin le plus simple reste souvent le site officiel python.org : tu telecharges la version recente, tu lances l'installateur, et tu coches "**Add Python to PATH**" si tu vois l'option. Ensuite tu ouvres un terminal et tu tapes `python --version`. Si un numero apparait, c'est bon. Parfois, sur Windows, c'est `py --version` qui repond mieux. Les deux existent. Garde celui qui marche chez toi et note-le. Lea a perdu une heure a cause du PATH non coche. Max a trouve `py` plus simple. Sam montre les deux a ses eleves pour eviter la panique.

Chez DanielCraft, on insiste sur ce detail parce que la moitie des "Python ne marche pas" du premier jour sont des histoires d'installation, pas de talent. Tu n'es pas en retard. Tu configures ton atelier.

## Ce que ce n'est pas

Installer Python, ce n'est pas "devenir developpeur". Ce n'est pas non plus installer vingt outils d'un coup. Ce n'est pas obligatoire d'ouvrir Docker, WSL, ou une usine a gaz des le chapitre 2. Un **interpreteur**, un editeur simple, un dossier de test : ca suffit pour tout ce livre. Plus tard, tu decouvriras les environnements virtuels. Pour l'instant, on reste terre a terre.

Ce n'est pas non plus une etape "triviale pour les autres". Beaucoup de gens bloquent ici. Si tu bloques, tu es dans la moyenne. Relis, reessaie, change de terminal, verifie le PATH. Puis avance.

Ton ordi a une boite a outils. Python est un outil dans la boite. Le terminal est la facon de parler a l'outil. L'**editeur** (VS Code, IDLE...) est l'endroit ou tu ecris la recette. Le fichier `.py` est la feuille. Quand tu lances `python salut.py`, tu dis : "execute cette feuille avec cet outil". Si le terminal dit "introuvable", deux causes classiques : mauvais dossier, ou Python pas dans le PATH. Pas de mystere cosmique.

:::attention
Sans PATH coche a l'install, Windows repond souvent "commande introuvable". Ce n'est pas toi. C'est la config. Recoche, reteste.
:::

## Ou ecrire le code ?

Deux options debutant : **VS Code** (gratuit) avec l'extension Python, ou **IDLE** (fourni avec Python), plus basique mais rassurant. Plus tard tu pourras aimer PyCharm ou autre. Pour ce livre, VS Code ou IDLE suffisent largement. Lea travaille dans VS Code parce qu'elle y a deja son HTML. Max prefere IDLE au debut : moins de panneaux. Sam alterne selon le cours. Choisis, note ton choix, n'en change pas toutes les cinq minutes.

## Fichier `.py` et dossier propre

Cree un dossier `mes-tests-python`. Dedans, cree un fichier `salut.py`. C'est ton programme. Astuce : un dossier par projet. Evite de tout mettre sur le Bureau en vrac. Quand tu auras dix fichiers, tu remercieras cette habitude. Chez DanielCraft, on traite le rangement comme une competence, pas comme du menage optionnel.

## Lancer

Dans le dossier du fichier :

```bash
python salut.py
```

Ou :

```bash
py salut.py
```

Si le terminal dit "introuvable", c'est souvent le mauvais dossier (tu n'es pas au bon endroit), ou le PATH pas coche a l'install. Utilise `cd` pour te deplacer vers le bon dossier, puis relance. Lea tape souvent `pwd` ou `cd` avant de se plaindre. Bon reflexe.

## La console interactive

```bash
python
```

Tu peux tester des lignes une par une. Utile pour un calcul vite fait.

```python
>>> 2 + 2
4
>>> exit()
```

`exit()` pour quitter. Ou Ctrl+Z puis Entree sur Windows. Sam utilise la console devant la classe pour montrer qu'une idee se teste sans creer un fichier. Max s'en sert pour verifier `19.99 * 1.2` avant de le mettre dans un script.

## Virtualenv ? (apercu)

Plus tard, les projets serieux utilisent un "**environnement virtuel**". Idee : isoler les bibliotheques d'un projet pour ne pas melanger les versions.

```bash
python -m venv .venv
```

Puis on active, puis `pip install ...`. Pour l'instant, tu n'en as pas besoin. Mais le mot existe. Tu le reverras. Mieux vaut l'avoir entendu une fois que de le decouvrir en panique le jour J.

:::astuce
Note dans `notes.md` : version Python + commande qui marche (`python` ou `py`) + editeur choisi. Ce papier te sauvera dans trois semaines.
:::

## Petite histoire

Lea a installe Python trois fois avant de cocher le PATH. La quatrieme, `python --version` a repondu. Elle a cree `mes-tests-python`, lance un fichier vide, vu "rien", sourit quand meme : l'atelier etait pret. Max a demande a Sam de verifier avec lui. Sam a regarde le message d'erreur, a dit "mauvais dossier", a montre `cd`. Trois minutes. Chez DanielCraft, on celebre ces petites victoires : elles annoncent les grandes.

## Erreur classique

Tu lances `python salut.py` depuis le mauvais dossier. Le terminal dit qu'il ne trouve pas le fichier. Solution : `cd` vers le bon dossier, puis relance. Autre classique : installer Python sans PATH, puis croire que "Python est casse". Reinstalle en cochant l'option, ou cherche comment ajouter Python au PATH sur ta version de Windows. Puis reteste.

## En vrai

Ouvre le terminal. Tape la commande de version. Note le resultat sur papier ou dans un fichier `notes.md`. Si ca marche, tu es pret pour ecrire. Si ca ne marche pas, reste ici jusqu'a ce que ca marche. Le chapitre 3 suppose un Python qui repond.

## A toi

1. Verifie `python --version` (ou `py --version`).
2. Cree le dossier `mes-tests-python` et le fichier `salut.py`.
3. Cree aussi `notes.md` : version Python + outil choisi (VS Code / IDLE).

On ecrira dans `salut.py` au chapitre suivant.
