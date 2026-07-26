# Chapitre 11 - Regex leger avec re

Une expression reguliere (**regex**), c'est un motif pour chercher ou valider du texte. Exemple : "est-ce que ca ressemble a un email ?", "trouve tous les numeros", "extraire un code postal". Utile, parfois magique - et souvent dangereuse si tu en abuses.

Une regex, c'est un filtre sur du texte irregulier. Tu decris un motif ("quelque chose qui ressemble a un email"). Python cherche la premiere occurrence, ou toutes, ou verifie que la chaine entiere correspond. Pour du CSV, du JSON, des extensions de fichier : utilise l'outil du format, pas la regex. La regex brille quand le format est sale ou libre.

Attention : les regex peuvent devenir un sport extreme. Ici, on reste leger. Quelques cas utiles avec le module `re`. Chez DanielCraft, consigne : si un `.startswith` ou un `in` suffit, n'utilise pas de regex. Lea extrait des emails dans des exports clients. Max valide des codes postaux dans des adresses. Sam montre le minimum utile sans noyer ses eleves.

:::retenir
Regex oui, mais leger. Si `Path.suffix` ou le module `csv` suffisent, laisse tomber la regex.
:::

## search : y a-t-il un motif ?

```python
import re

texte = "Contacte-moi : ada@exemple.fr merci"
m = re.search(r"[\w.+-]+@[\w.-]+\.\w+", texte)
if m:
    print("Email trouve :", m.group())
else:
    print("Pas d'email")
```

Le `r"..."` est une raw string : les backslash restent plus lisibles. `search` trouve la premiere occurrence. `m.group()` donne le texte matche.

Ce motif email est simplifie (pas une validation legale absolue). Pour un exercice ou un filtre grossier, ca va. Pour de la vraie validation metier, les regles sont plus riches.

## match vs search vs fullmatch

`search` : quelque part dans la chaine. `match` : au debut. `fullmatch` : la chaine entiere doit correspondre.

```python
print(re.fullmatch(r"\d{5}", "75001"))  # code postal FR simplifie
print(re.fullmatch(r"\d{5}", "7500"))   # None
```

Pour valider une saisie complete, `fullmatch` est souvent le bon reflexe.

## Groupes

Tu veux extraire des morceaux :

```python
m = re.search(r"note\s*[:=]\s*(\d+(?:\.\d+)?)", "note: 14.5")
if m:
    print(float(m.group(1)))
```

Les parentheses capturent. `group(1)` est le premier groupe. Utile pour parser des logs ou des lignes un peu libres.

## findall

```python
texte = "Alice 14, Bob 11, Chloe 16"
notes = re.findall(r"\d+", texte)
print(notes)  # ['14', '11', '16']
```

Tu recuperes une liste de chaines. Convertis ensuite en nombres si besoin.

## Cas utiles du quotidien

Verifier qu'un identifiant ne contient que lettres, chiffres, tirets : `r"^[a-zA-Z0-9_-]+$"`. Chercher une URL grossiere : `r"https?://\S+"`. Remplacer des espaces multiples : `re.sub(r"\s+", " ", texte).strip()`.

```python
propre = re.sub(r"\s+", " ", "  trop   d'espaces  ").strip()
print(propre)
```

## Quand ne pas regex

Compter des lignes CSV : module `csv`. Parser du JSON : `json`. Verifier une extension de fichier : `Path(p).suffix == ".csv"`. Les regex brillent sur du texte irregulier. Sur des formats structures, utilise l'outil du format.

:::astuce
Pour valider une saisie complete (code postal, id), prefere `fullmatch`. Pour "trouver quelque part", `search`. Pour "tous les morceaux", `findall`.
:::

## Petite histoire

Max voulait extraire des numeros de facture d'un bloc de texte copie depuis un PDF. Il a ecrit une regex de trois lignes illisible, ca marchait une fois sur deux. Lea lui a montre `re.search` avec un groupe simple. Dix lignes, lisible, fiable pour son cas. La lecon : regex oui, mais leger et teste.

Sam montre en cours un email simplifie, puis dit : "ce n'est pas une validation legale". Les eleves comprennent la difference entre filtre grossier et regle metier. Chez DanielCraft, on prefere un filtre honnete a une regex "parfaite" de quatre-vingts caracteres.

## Erreur classique

Ecrire une regex illegible de trois lignes pour un probleme soluble en deux `split`. Ou oublier `r"..."` et se battre avec les `\` escapes. Ou croire qu'une regex email "parfaite" existe en dix caracteres. Ou utiliser regex la ou `Path.suffix` suffit.

## Zoom : lire un log avec regex

Parfois un CSV ou un JSON n'existe pas. Tu as une ligne de log libre :

```text
2026-07-24 ERROR user=alice note=14.5 action=save
```

Tu peux extraire la note sans tout parser :

```python
m = re.search(r"note=(\d+(?:\.\d+)?)", ligne)
if m:
    print(float(m.group(1)))
```

C'est le bon usage : texte irregulier, extraction ciblee. Si le format devient stable, passe a un vrai parseur (CSV, JSON, config). Lea utilise ce genre de regex une fois par mois sur des exports clients brouillons. Max prefere `csv` des que le format se stabilise.

## En vrai

Prends un paragraphe avec un email et un numero a 5 chiffres. Extraie les deux avec `search` / `findall`. Puis valide une saisie code postal avec `fullmatch`.

## A toi

Ecris `extraire_emails(texte)` qui retourne une liste (peut-etre vide). Teste avec 0, 1, 2 emails dans la chaine. Simple, utile, et tu as touche le coeur de `re` sans te noyer. Si tu sens l'envie d'une regex de trois lignes, arrete-toi et demande-toi si un `split` ou le module `csv` suffirait. Chez DanielCraft, cette pause evite plus de dettes que n'importe quel motif "elegant".

:::attention
Une regex illisible de trois lignes pour un `split` suffit rarement. Prefere le plus simple qui marche, puis teste.
:::
