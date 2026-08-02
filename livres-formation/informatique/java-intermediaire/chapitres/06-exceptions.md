# Exceptions : gerees proprement

```java
try {
  Files.readString(Path.of("data.txt"));
} catch (IOException e) {
  System.err.println("Lecture impossible");
} finally {
  // nettoyage si besoin
}
```

## Bonnes pratiques

- Ne pas avaler l'exception (`catch` vide).
- Exceptions **checked** = le compilateur t'oblige a gerer.
- Creer des exceptions metier si le message compte.

## A retenir

- Exception = signal, pas flux normal.
