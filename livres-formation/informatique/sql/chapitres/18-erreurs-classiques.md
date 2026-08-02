# Chapitre 18 - Erreurs classiques

Oublier `WHERE` sur un `UPDATE` / `DELETE`. Comparer avec `=` a `NULL` au lieu de `IS NULL`. Joindre sur le mauvais champ. Faire confiance a un total sans regarder 3 lignes. Mettre des prix en texte. Chez DanielCraft, ces pieges reviennent plus souvent que les "gros bugs savants".

Lea a failli vider une table de test sans WHERE. Max a joint sur `prenom`. Sam a somme des NULL sans comprendre.

## Petite histoire

Un ami de Max montre un dashboard "CA du mois". Lea demande la requete. Il y a un JOIN en trop. Le chiffre etait beau. Faux.

## A toi

Coche les pieges que tu as deja froles (meme sur papier).

:::retenir
Les erreurs SQL classiques sont humaines : WHERE, NULL, JOIN, types.
:::

:::attention
Un beau chiffre ne prouve pas une bonne requete.
:::

:::astuce
Garde une checklist : WHERE? cle? echantillon? type?
:::
