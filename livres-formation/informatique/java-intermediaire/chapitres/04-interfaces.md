# Interfaces et classes abstraites

Une **interface** definit un contrat. Une **classe abstraite** peut partager du code.

```java
interface Payable {
  double montant();
}

abstract class Personne {
  String nom;
  abstract String role();
}
```

## Default methods

Depuis Java 8, une interface peut avoir des methodes `default`.

## A retenir

- Interface = comportement ; abstraite = famille avec code commun.
