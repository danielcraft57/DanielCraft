# Chapitre 12 - Fonctions fenetre (idee)

`ROW_NUMBER`, `RANK`, `SUM() OVER (...)` calculent sur un partitionnement **sans ecraser** les lignes (contrairement a un GROUP BY qui agrege). Chez DanielCraft : idee pour top N par groupe. Lea numeroote les commandes par client. Sam dit "fenetre = regarder les voisins".

:::retenir
Fenetre = calcul sur un groupe de lignes, en gardant le detail.
:::

## A toi

Decris : "rang de chaque commande par montant dans le mois".

:::astuce
Apprends `ROW_NUMBER` avant les fenetres complexes.
:::
