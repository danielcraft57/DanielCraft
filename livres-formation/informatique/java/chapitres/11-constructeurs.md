# Chapitre 11 - Constructeurs

Le **constructeur** prepare l'objet a la creation.

```java
public Client(String prenom) {
  this.prenom = prenom;
  this.points = 0;
}
```

`new Client("Max")` appelle le constructeur. Chez DanielCraft, Lea initialise proprement. Max laisse des champs a null et trébuche plus tard.

:::retenir
Constructeur = etat de depart coherent.
:::

## A toi

Constructeur `Produit(String nom, double prix)`.

:::attention
Oublier d'assigner un champ : valeurs par defaut / null.
:::
