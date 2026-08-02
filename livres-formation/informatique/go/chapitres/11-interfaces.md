# Les interfaces

## C'est quoi une interface ?

Une interface definit un ensemble de methodes. Toute struct qui implemente ces methodes satisfait l'interface automatiquement (pas de mot-cle `implements`).

```go
type Presentable interface {
    SePresenter() string
}
```

N'importe quelle struct avec une methode `SePresenter() string` est un `Presentable`.

```go
type Personne struct {
    Nom string
}

func (p Personne) SePresenter() string {
    return "Je suis " + p.Nom
}

func afficher(p Presentable) {
    fmt.Println(p.SePresenter())
}

afficher(Personne{Nom: "Lea"})
```

## L'interface vide

```go
func afficherTout(v interface{}) {
    fmt.Println(v)
}
// Ou avec la syntaxe moderne :
func afficherTout2(v any) {
    fmt.Println(v)
}
```

`any` (alias de `interface{}`) accepte n'importe quel type.

> **Astuce DanielCraft** - Les interfaces en Go sont implicites. C'est ce qui les rend puissantes et flexibles.

## Interfaces courantes

| Interface | Methode | Package |
|-----------|---------|---------|
| `Stringer` | `String() string` | `fmt` |
| `Reader` | `Read([]byte) (int, error)` | `io` |
| `Writer` | `Write([]byte) (int, error)` | `io` |
| `Error` | `Error() string` | `builtin` |

## Petite histoire

Nora cree une interface `Forme` avec `Aire() float64`. Elle l'implemente pour `Cercle` et `Rectangle`. Une seule fonction `afficherAire(f Forme)` fonctionne pour les deux.

## A retenir

- Interface = contrat de methodes.
- Satisfaction implicite (pas de `implements`).
- `any` = interface vide, accepte tout.
