# Structs et classes

## Struct (type valeur)

```swift
struct Animal {
    var nom: String
    var age: Int

    func sePresenter() -> String {
        "Je suis \(nom), \(age) ans."
    }
}

let chat = Animal(nom: "Felix", age: 3)
print(chat.sePresenter())
```

## Class (type reference)

```swift
class Compte {
    var solde: Double
    init(solde: Double) { self.solde = solde }
    func depot(_ montant: Double) { solde += montant }
}
```

## Quand choisir ?

- **Struct** : donnees simples, copie par valeur (prefere en Swift).
- **Class** : heritage, identite partagee, reference.

> **Astuce DanielCraft** - Swift prefere les structs. Utilise une class seulement si tu as besoin d'heritage ou de reference.

## A retenir

- Struct = valeur, Class = reference.
- Swift prefere les structs.
- `init` pour le constructeur.
