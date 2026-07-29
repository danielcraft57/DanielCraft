# Records : donnees immuables

```java
public record Point(int x, int y) {}
Point p = new Point(3, 4);
System.out.println(p.x());
```

## Interet

- Moins de boilerplate (equals, hashCode, toString).
- Ideal DTO / resultats intermediaires.

## A retenir

- Record = porteur de donnees, pas logique lourde.
