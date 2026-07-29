# Optional : finir avec null

```java
Optional<User> u = findUser(id);
String name = u.map(User::getName).orElse("inconnu");
```

## Regles

- Retour de methode : OK.
- Champ / parametre : en general non.
- Eviter `get()` sans `isPresent` / `orElse`.

## A retenir

- Optional = intention "peut etre absent".
