# Heritage et polymorphisme

Le **polymorphisme** : une reference de type parent pointe vers un enfant.

```java
Animal a = new Chat();
a.crier(); // version Chat
```

## Regles utiles

- `@Override` systematiquement.
- Preferer composition quand l'heritage devient un labyrinthe.
- `final` sur classe / methode pour figer.

## A retenir

- Polymorphisme = meme appel, comportement adapte.
