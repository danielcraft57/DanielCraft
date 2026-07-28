# Chapitre 11 - Cles primaires et etrangeres

Une **cle primaire** identifie une ligne de facon unique (souvent `id`). Une **cle etrangere** pointe vers la cle d'une autre table. Chez DanielCraft, on les lit comme des etiquettes et des fils : sans etiquette claire, les jointures deviennent du bricolage.

Exemple invente : table `clients` avec `id` unique. Table `commandes` avec `client_id` qui pointe vers `clients.id`. Max joint ainsi. Sam oublie la cle et croise n'importe comment : resultats absurdes.

## Ce que ce n'est pas

Ce n'est pas "un id magique qui reparte tout". Ce n'est pas obligatoire de tout comprendre en DBA des le jour 1. C'est le contrat minimal pour croiser sans mentir.

## Petite histoire

Lea cree `produits(id, nom)`. Puis `lignes_commande(commande_id, produit_id, qte)`. Elle explique a Max : "la cle dit qui est qui". Max arrete de joindre sur le prenom.

## Erreur classique

Joindre sur une colonne non unique (prenom, ville). Ou croire que deux tables "se comprennent" sans cle.

## En vrai

Dessine deux boites `clients` et `commandes`. Fleche de `client_id` vers `id`.

## A toi

Ecris la cle primaire et la cle etrangere de ton mini schema perso.

:::retenir
Cle primaire = identite. Cle etrangere = lien vers une autre table.
:::

:::attention
Joindre sans cle claire = resultats qui mentent gentiment.
:::

:::astuce
Nomme `quelquechose_id` pour rendre le lien visible.
:::
