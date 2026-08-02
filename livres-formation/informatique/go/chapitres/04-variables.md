# Les variables

## Declarer une variable

Go est fortement type. Plusieurs facons de declarer :

```go
var nom string = "Max"     // Type explicite
var age int = 24           // Type explicite
ville := "Lyon"            // Type deduit (raccourci)
```

Le raccourci `:=` est le plus utilise a l'interieur des fonctions.

## Regles de nommage

- camelCase : `monScore`, `prixTotal`.
- Majuscule initiale = exporte (visible hors du package).
- Minuscule initiale = prive au package.
- Pas de underscores dans les noms (convention Go).

> **Astuce DanielCraft** - En Go, une variable declaree mais non utilisee provoque une erreur de compilation. Pas de code mort.

## Modifier une variable

```go
score := 0
score = score + 10
score += 5
fmt.Println(score) // 15
```

## Affichage formate

```go
nom := "Lea"
age := 28
fmt.Printf("Je suis %s, %d ans\n", nom, age)
```

`%s` pour les strings, `%d` pour les entiers, `%f` pour les flottants.

## Constantes

```go
const TVA = 0.20
const Pays = "France"
```

## Petite histoire

Sam declare `budget := 1800` et `loyer := 650`. Il affiche `budget - loyer`. Go lui repond 1150.

## A retenir

- `:=` pour declarer et initialiser (dans une fonction).
- Variables non utilisees = erreur de compilation.
- `fmt.Printf` pour l'affichage formate.
