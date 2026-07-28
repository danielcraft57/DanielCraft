# Chapitre 4 - ORDER BY et LIMIT

Tu sais lire et filtrer. Maintenant tu **ordonnes** et tu **coupes**. `ORDER BY` trie le resultat. `LIMIT` garde les N premieres lignes apres le tri (selon le moteur ; l'idee reste "top N"). Chez DanielCraft, c'est le duo "top 5" sans paniquer. Lea trie les commandes du plus gros total au plus petit. Max limite a 10 pour ne pas noyer le client. Sam rappelle : "trie d'abord, coupe ensuite - sinon tu coupes au hasard".

```sql
SELECT id, client_id, total
FROM commandes
ORDER BY total DESC
LIMIT 5;
```

`ASC` = croissant (souvent par defaut). `DESC` = decroissant. Tu peux trier sur plusieurs colonnes : `ORDER BY ville ASC, nom ASC`.

:::retenir
`ORDER BY` trie. `LIMIT` coupe. Ensemble : top N utile.
:::

## Ou placer les clauses

Ordre mental courant :

```sql
SELECT ...
FROM ...
WHERE ...
ORDER BY ...
LIMIT ...;
```

Tu filtres d'abord (WHERE), tu tries le sous-ensemble, tu coupes. Si tu LIMIT sans ORDER, l'ordre peut etre instable selon le moteur. Pour un "top", ORDER est quasi obligatoire.

## Petite histoire

Lea devait montrer "les 3 plus grosses commandes de Lyon". Elle a joint plus tard ; ici elle a d'abord `ORDER BY total DESC LIMIT 3` sur un extrait filtre. Max a mis LIMIT 3 sans ORDER et a cru que c'etait "les plus importantes". Sam a relance avec ORDER : la liste a change. Message recu.

## Erreur classique

Croire que LIMIT remplace WHERE. Ou trier sur une colonne absente du SELECT (parfois OK, parfois non selon le moteur - reste simple : trie sur ce que tu comprends). Autre piege : `ORDER BY 1` (numero de colonne) : court, opaque. Prefere le nom.

:::attention
Sans `ORDER BY`, `LIMIT` ne garantit pas un "meilleur" resultat - seulement un morceau.
:::

## En vrai

```sql
SELECT nom, ville FROM clients ORDER BY nom ASC LIMIT 10;
```

Puis change en `ORDER BY ville DESC, nom ASC`. Observe. Sur `commandes`, fais le top 5 des totaux.

:::astuce
Pour un export "apercu", `LIMIT 20` protege ton ecran et ta patience.
:::

## A toi

Ecris trois requetes : (1) clients tries par ville, (2) top 5 commandes, (3) top 5 apres un WHERE `total >= 50`. Explique en une phrase la difference entre (2) et (3). Chez DanielCraft, le tri sans filtre et le tri filtre ne racontent pas la meme histoire.
