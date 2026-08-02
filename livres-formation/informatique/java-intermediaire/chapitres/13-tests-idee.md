# Tests (idee JUnit)

```java
@Test
void addition() {
  assertEquals(4, Calc.add(2, 2));
}
```

## Pourquoi

- Regresser moins.
- Documenter le comportement attendu.

> **Astuce DanielCraft** - Un test sur la regle metier bat dix commentaires flous.

## A retenir

- Tester le comportement, pas l'implementation privee.
