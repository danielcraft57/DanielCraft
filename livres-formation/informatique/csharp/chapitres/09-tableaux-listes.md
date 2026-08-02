# Tableaux et listes

## Les tableaux (Array)

Un tableau a une taille fixe, definie a la creation.

```csharp
int[] notes = { 14, 17, 11, 19, 8 };
Console.WriteLine(notes[0]);   // 14
Console.WriteLine(notes.Length); // 5
```

## Parcourir un tableau

```csharp
foreach (int note in notes)
{
    Console.WriteLine(note);
}
```

## Les listes (List<T>)

Une liste est redimensionnable. C'est le conteneur le plus utilise.

```csharp
List<string> fruits = new() { "pomme", "banane" };
fruits.Add("cerise");
fruits.Remove("banane");
Console.WriteLine(fruits.Count); // 2
```

## Methodes utiles de List

| Methode | Role |
|---------|------|
| `.Add(x)` | Ajoute a la fin |
| `.Remove(x)` | Supprime par valeur |
| `.Contains(x)` | Verifie la presence |
| `.Sort()` | Trie |
| `.Count` | Nombre d'elements |

> **Astuce DanielCraft** - Utilise `List<T>` par defaut. Les tableaux sont utiles quand la taille est connue et fixe.

## Petite histoire

Nora stocke les prenoms de sa classe dans une `List<string>`. Elle trie avec `.Sort()` et affiche avec `foreach`.

## A retenir

- Tableau = taille fixe, acces par index.
- `List<T>` = taille variable, methodes pratiques.
- `foreach` pour parcourir sans index.
