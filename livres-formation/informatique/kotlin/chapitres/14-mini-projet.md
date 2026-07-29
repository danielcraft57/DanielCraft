# Mini-projet : liste de courses CLI

## L'objectif

Creer un programme en ligne de commande qui permet d'ajouter, lister et supprimer des articles d'une liste de courses.

## Structure

```kotlin
fun main() {
    val courses = mutableListOf<String>()

    while (true) {
        println("\n1. Ajouter  2. Lister  3. Supprimer  4. Quitter")
        when (readln().trim()) {
            "1" -> {
                print("Article : ")
                val article = readln().trim()
                if (article.isNotEmpty()) {
                    courses.add(article)
                    println("Ajoute.")
                }
            }
            "2" -> {
                if (courses.isEmpty()) println("Liste vide.")
                else courses.forEachIndexed { i, a -> println("  ${i + 1}. $a") }
            }
            "3" -> {
                print("Numero : ")
                val idx = readln().toIntOrNull()?.minus(1)
                if (idx != null && idx in courses.indices) {
                    courses.removeAt(idx)
                    println("Supprime.")
                }
            }
            "4" -> { println("A bientot !"); break }
        }
    }
}
```

## Ce que tu apprends

- `mutableListOf` pour une collection modifiable.
- `when` pour le menu.
- `readln()` pour lire l'entree utilisateur.
- Null safety avec `toIntOrNull()`.

> **Astuce DanielCraft** - Commence par le menu, puis ajoute une commande a la fois.

## A retenir

- Collections mutables + when + readln = CLI complet.
- `toIntOrNull()` evite les crash sur entree invalide.
