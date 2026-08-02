# Chapitre 17 - Atelier : jointure

Tables : `clients(id, prenom)`, `commandes(id, client_id, montant)`.

## Missions

1. INNER JOIN : prenom + montant
2. Total par prenom (JOIN + GROUP BY)
3. LEFT JOIN : clients meme sans commande
4. Compte combien de clients sans commande

Sam dessine la fleche `client_id -> id` avant d'ecrire. Lea verifie avec 2 clients connus.

## A toi

Ecris 1 et 3. Si 2 bloque, relis agregats.

:::retenir
JOIN = croiser sur une cle. Dessine avant d'ecrire.
:::

:::attention
JOIN sans condition (ou mauvaise cle) = explosion de lignes.
:::

:::astuce
Prefixe les colonnes : `clients.prenom`, `commandes.montant`.
:::
