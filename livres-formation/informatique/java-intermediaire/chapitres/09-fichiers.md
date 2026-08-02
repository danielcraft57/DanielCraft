# Fichiers et NIO.2

```java
Path p = Path.of("notes.txt");
Files.writeString(p, "Bonjour");
String contenu = Files.readString(p);
```

## Idees utiles

- `Files.lines(path)` + stream pour gros fichiers.
- try-with-resources pour fermer automatiquement.

```java
try (var reader = Files.newBufferedReader(p)) {
  // ...
}
```

## A retenir

- Path + Files = API moderne preferée a File legacy.
