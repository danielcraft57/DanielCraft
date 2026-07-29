# Streams : pipeline sur les donnees

```java
List<Integer> pairs = nombres.stream()
  .filter(n -> n % 2 == 0)
  .map(n -> n * 2)
  .toList();
```

## Operations

- Intermediaires : `filter`, `map`, `sorted`.
- Terminales : `toList`, `forEach`, `reduce`, `collect`.

> **Astuce DanielCraft** - Un stream court et lisible bat une boucle opaque de 40 lignes.

## A retenir

- Stream = declaration du quoi, pas du comment detaille.
