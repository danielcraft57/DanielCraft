# Chapitre 10 - DELETE : retirer des lignes

`DELETE` enleve des **lignes**. Pas la table entiere (ca serait `DROP`, hors focus ici). Chez DanielCraft, DELETE est le chapitre du frein a main. Lea n'efface qu'apres SELECT. Max a failli vider `commandes`. Sam ecrit en gros : WHERE.

```sql
DELETE FROM commandes
WHERE id = 42;
```

:::retenir
DELETE retire des lignes. SELECT d'abord. WHERE presque toujours.
:::

## Le reflexe SELECT miroir

```sql
SELECT * FROM commandes WHERE id = 42;
-- si la ligne est la bonne :
DELETE FROM commandes WHERE id = 42;
```

Pour un lot :

```sql
SELECT * FROM commandes WHERE total = 0 AND cree_le < '2025-01-01';
-- puis seulement si le compte est attendu :
DELETE FROM commandes WHERE total = 0 AND cree_le < '2025-01-01';
```

Compte les lignes du SELECT. Si tu en vois 8000 et tu en attendais 8, tu stops.

## DELETE sans WHERE

```sql
-- Tres dangereux
-- DELETE FROM commandes;
```

Selon le moteur / droits, tu peux vider la table. Ne le fais pas "pour tester" hors bac a sable.

## Petite histoire

Lea devait retirer des commandes de test a total 0. Elle a SELECT, vu 12 lignes, DELETE avec le meme WHERE, re-SELECT, zero reste. Max a lance un DELETE avec une faute de frappe dans le WHERE qui matchait trop large. Heureusement, environnement de stage. Sam raconte cette histoire a chaque promo. Elle marche.

## Erreur classique

DELETE sans WHERE. Confondre DELETE (lignes) et DROP (objet). Effacer avant de comprendre les cles etrangeres (une commande peut etre liee ; la base peut refuser ou cascade selon schema).

:::attention
Une fois commit / hors transaction, DELETE peut etre definitif. Verifie deux fois.
:::

## En vrai

En test : inserer une ligne jetable, la SELECT, la DELETE, SELECT encore (zero ligne). Note le rythme.

:::astuce
Si tu hesites, exporte d'abord les lignes visees (`SELECT ...`). Tu pourras re-INSERT si besoin.
:::

## A toi

Ecris le duo SELECT + DELETE pour supprimer une commande d'id connu. Ajoute une phrase "je n'execute en vrai que si...". Chez DanielCraft, la phrase frein fait partie de la competence.
