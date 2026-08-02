# Collections : List, Set, Map

Les **collections** remplacent les tableaux quand la taille change.

```java
List<String> noms = new ArrayList<>();
noms.add("Lea");
noms.add("Max");

Set<Integer> ids = new HashSet<>();
Map<String, Integer> ages = new HashMap<>();
ages.put("Sam", 28);
```

## Choisir

| Type | Usage |
|------|-------|
| List | Ordre, doublons possibles |
| Set | Unicite |
| Map | Cle → valeur |

## A retenir

- Preferer les interfaces (`List`) aux implementations dans les signatures.
