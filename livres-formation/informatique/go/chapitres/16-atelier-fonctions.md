# Atelier : fonctions

## Objectif

Creer des fonctions avec retours simples et multiples.

## Exercice 1 : salutation

```go
func saluer(nom string, heure int) string {
    if heure < 12 {
        return fmt.Sprintf("Bonjour %s !", nom)
    }
    if heure < 18 {
        return fmt.Sprintf("Bon apres-midi %s !", nom)
    }
    return fmt.Sprintf("Bonsoir %s !", nom)
}
```

## Exercice 2 : moyenne

```go
func moyenne(notes []float64) float64 {
    if len(notes) == 0 {
        return 0
    }
    total := 0.0
    for _, n := range notes {
        total += n
    }
    return total / float64(len(notes))
}
```

## Exercice 3 : mot de passe valide

```go
import "unicode"

func mdpValide(mdp string) bool {
    if len(mdp) < 8 {
        return false
    }
    for _, c := range mdp {
        if unicode.IsDigit(c) {
            return true
        }
    }
    return false
}
```

## Exercice 4 : division securisee

```go
func diviser(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("division par zero")
    }
    return a / b, nil
}
```

> **Astuce DanielCraft** - Teste chaque fonction avec des cas normaux et limites.

## A retenir

- Retours multiples pour les erreurs.
- `fmt.Sprintf` pour formater sans afficher.
- `range` sur les strings donne des runes.
