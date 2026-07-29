# Mini-projet : liste de courses CLI

## Objectif

Programme en ligne de commande pour ajouter, lister et supprimer des articles.

```swift
import Foundation

var courses: [String] = []

while true {
    print("\n1. Ajouter  2. Lister  3. Supprimer  4. Quitter")
    guard let choix = readLine()?.trimmingCharacters(in: .whitespaces) else { continue }

    switch choix {
    case "1":
        print("Article : ", terminator: "")
        if let article = readLine()?.trimmingCharacters(in: .whitespaces), !article.isEmpty {
            courses.append(article)
            print("Ajoute.")
        }
    case "2":
        if courses.isEmpty { print("Liste vide.") }
        else { for (i, a) in courses.enumerated() { print("  \(i + 1). \(a)") } }
    case "3":
        print("Numero : ", terminator: "")
        if let idx = Int(readLine() ?? ""), idx >= 1, idx <= courses.count {
            courses.remove(at: idx - 1)
            print("Supprime.")
        }
    case "4":
        print("A bientot !")
        exit(0)
    default:
        break
    }
}
```

## A retenir

- Array + switch + readLine = CLI complet.
- `guard let` pour valider les entrees.
