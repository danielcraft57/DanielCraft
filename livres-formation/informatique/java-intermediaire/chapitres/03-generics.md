# Generics : typer sans caster

Les **generics** evitent les cast et les erreurs a l'execution.

```java
Box<String> b = new Box<>();
b.set("ok");
String s = b.get(); // pas de cast
```

## Wildcards (idee)

- `List<? extends Number>` : lecture de nombres.
- `List<? super Integer>` : ecriture d'entiers.

> **Piege** - `List<Object>` n'est pas un `List<String>`.

## A retenir

- Generics = securite de type a la compilation.
