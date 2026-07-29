# Les conditions

## if / else

```go
age := 17
if age >= 18 {
    fmt.Println("Majeur")
} else {
    fmt.Println("Mineur")
}
```

Pas de parentheses autour de la condition. Les accolades sont obligatoires.

## if / else if / else

```go
note := 14
if note >= 16 {
    fmt.Println("Tres bien")
} else if note >= 12 {
    fmt.Println("Bien")
} else if note >= 10 {
    fmt.Println("Passable")
} else {
    fmt.Println("Insuffisant")
}
```

## if avec initialisation

```go
if err := faireQuelqueChose(); err != nil {
    fmt.Println("Erreur :", err)
}
```

On peut declarer une variable dans le `if`. Elle n'existe que dans ce bloc.

> **Astuce DanielCraft** - Le pattern `if err != nil` est la facon idiomatique de gerer les erreurs en Go.

## Switch

```go
jour := "lundi"
switch jour {
case "lundi", "mardi":
    fmt.Println("Debut de semaine")
case "vendredi":
    fmt.Println("Presque le weekend")
default:
    fmt.Println("Autre jour")
}
```

Pas besoin de `break` en Go : chaque case s'arrete automatiquement.

## Petite histoire

Max ecrit un switch pour afficher le tarif selon l'age. Enfant, adulte, senior. Trois cas, zero `break`, code propre.

## A retenir

- Pas de parentheses, accolades obligatoires.
- `if err != nil` pour les erreurs.
- `switch` sans `break` (arret automatique).
