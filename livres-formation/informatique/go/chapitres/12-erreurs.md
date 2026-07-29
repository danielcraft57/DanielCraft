# Gerer les erreurs

## Pas de try/catch en Go

Go n'a pas d'exceptions. Les erreurs sont des valeurs retournees.

```go
fichier, err := os.Open("data.txt")
if err != nil {
    fmt.Println("Erreur :", err)
    return
}
defer fichier.Close()
```

## Creer ses propres erreurs

```go
import "errors"

func retirer(solde, montant float64) (float64, error) {
    if montant > solde {
        return 0, errors.New("solde insuffisant")
    }
    return solde - montant, nil
}
```

## fmt.Errorf pour formater

```go
func diviser(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("division par zero : %f / %f", a, b)
    }
    return a / b, nil
}
```

## defer

`defer` reporte l'execution d'une instruction a la fin de la fonction. Pratique pour fermer des ressources.

```go
func lireFichier(nom string) error {
    f, err := os.Open(nom)
    if err != nil {
        return err
    }
    defer f.Close() // Ferme quoi qu'il arrive

    // ... lire le fichier
    return nil
}
```

> **Astuce DanielCraft** - `defer` s'execute dans l'ordre LIFO (dernier defer = premier execute).

## Petite histoire

Max ouvre un fichier, oublie de le fermer. Le programme garde la ressource ouverte. Il ajoute `defer f.Close()` et le probleme disparait.

## A retenir

- Erreurs = valeurs, pas d'exceptions.
- `if err != nil` : le pattern central.
- `defer` pour nettoyer les ressources.
- `errors.New()` et `fmt.Errorf()` pour creer des erreurs.
