# Les fonctions

## Declarer une fonction

```go
func saluer(prenom string) {
    fmt.Printf("Bonjour %s !\n", prenom)
}

saluer("Nora")
```

## Retourner une valeur

```go
func additionner(a, b int) int {
    return a + b
}

resultat := additionner(3, 7)
```

## Retours multiples

C'est une specificite de Go : une fonction peut retourner plusieurs valeurs.

```go
func diviser(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("division par zero")
    }
    return a / b, nil
}

resultat, err := diviser(10, 3)
if err != nil {
    fmt.Println(err)
}
```

> **Astuce DanielCraft** - Le pattern "valeur, erreur" est central en Go. Toujours verifier `err`.

## Fonctions comme valeurs

```go
doubler := func(x int) int { return x * 2 }
fmt.Println(doubler(5)) // 10
```

## Petite histoire

Max ecrit une fonction qui retourne un quotient et une erreur. Nora trouve ca plus clair qu'un try/catch : pas de surprise, on sait toujours ce qu'on recoit.

## A retenir

- `func nom(params) typeRetour { ... }`
- Retours multiples : `(valeur, erreur)`.
- Toujours verifier `err != nil`.
