# Enums riches

```java
enum Statut {
  OUVERT, FERME, ARCHIVE;

  boolean estActif() {
    return this == OUVERT;
  }
}
```

## Usages

- Etats finis (workflow).
- Remplacer les constantes String magiques.

## A retenir

- Enum = ensemble ferme de valeurs nommees.
