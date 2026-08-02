# Erreurs classiques

## 1. Force unwrap avec !

```swift
let nom: String? = nil
print(nom!.count)  // Crash !
```

## 2. Confondre struct et class

Les structs sont copiees, les classes sont referencees.

## 3. Oublier break dans switch

Swift n'a pas de fallthrough implicite, mais attention aux cas vides.

## 4. Mutable vs immutable collection

```swift
let liste = [1, 2, 3]
liste.append(4)  // Erreur : let = immutable
```

## 5. Optional non deballe

```swift
let n: Int? = 42
print(n + 1)  // Erreur : deballe avec if let ou ??
```

> **Astuce DanielCraft** - Lis les messages du compilateur Xcode. Ils sont tres clairs.
