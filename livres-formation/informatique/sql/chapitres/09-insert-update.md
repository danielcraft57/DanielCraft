# Chapitre 9 - INSERT et UPDATE

Jusqu'ici tu lisais. Maintenant tu **ecris** dans la base. `INSERT` ajoute une ligne. `UPDATE` modifie des lignes existantes. Chez DanielCraft, ecrire est un geste serieux : tu changes la realite partagee. Lea double-check avant. Max a mis a jour sans WHERE une fois - histoire courte, lecon longue. Sam impose : "SELECT d'abord, ecriture ensuite".

```sql
INSERT INTO clients (nom, ville)
VALUES ('Ines', 'Nantes');
```

```sql
UPDATE clients
SET ville = 'Lyon'
WHERE id = 3;
```

:::retenir
INSERT ajoute. UPDATE modifie. Toujours cibler avec WHERE pour UPDATE.
:::

## UPDATE : le WHERE obligatoire mentalement

```sql
-- Dangereux : touche potentiellement toute la table
-- UPDATE clients SET ville = 'Lyon';

-- Sain : une cible claire
UPDATE clients
SET ville = 'Lyon'
WHERE id = 3;
```

Reflexe : ecris d'abord le SELECT equivalent (`SELECT * FROM clients WHERE id = 3`), verifie, puis remplace SELECT par UPDATE ... SET.

## Plusieurs colonnes

```sql
UPDATE commandes
SET total = 120, cree_le = '2026-07-28'
WHERE id = 42;
```

```sql
INSERT INTO produits (nom, prix)
VALUES ('Joint silicone', 4.50);
```

Les colonnes et les valeurs doivent s'aligner (nombre et ordre). Respecte les types (chapitre 12) et les cles (chapitre 11).

## Petite histoire

Max voulait corriger une ville. Il a oublie WHERE. Tous les clients sont devenus "Lyon". Sauvegarde ou transaction selon l'outil l'a sauve ; la sueur aussi. Lea insere toujours une ligne de test puis SELECT pour verifier. Sam chronometre le "SELECT miroir" avant tout UPDATE en atelier. DanielCraft : la lenteur de verification bat la vitesse de catastrophe.

## Erreur classique

UPDATE sans WHERE. INSERT avec mauvais nombre de valeurs. Mettre un texte dans une colonne nombre. Croire que INSERT "remplace" une ligne existante (non : ca ajoute ; le remplacement propre passe souvent par UPDATE ou regles specifiques).

:::attention
Sur une base partagee, un UPDATE large peut casser le travail de tout le monde. Cible etroitement.
:::

## En vrai

Dans un environnement de test seulement : INSERT un client fictif, SELECT-le, UPDATE sa ville, SELECT encore. Ne joue pas ca sur la prod.

:::astuce
Garde une transaction / un backup mental : "puis-je annuler ?" Si non, n'execute pas encore.
:::

## A toi

Ecris sur papier (sans executer en prod) : (1) un INSERT clients, (2) un UPDATE avec WHERE id, (3) le SELECT de verification avant UPDATE. Chez DanielCraft, le papier avant le clic sauve des soirees.
