# Premier programme

## Hello World moderne

Depuis C# 10, un programme minimal tient en une ligne :

```csharp
Console.WriteLine("Bonjour le monde !");
```

Cree un projet avec `dotnet new console`, remplace le contenu de `Program.cs`, puis `dotnet run`.

## La version classique

```csharp
namespace MonApp;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Bonjour le monde !");
    }
}
```

Les deux versions produisent le meme resultat. La version courte utilise les "top-level statements".

> **Astuce DanielCraft** - Commence avec la version courte. Tu comprendras les namespaces et classes plus tard.

## Afficher plusieurs lignes

```csharp
Console.WriteLine("Ligne 1");
Console.WriteLine("Ligne 2");
Console.Write("Sans retour ");
Console.Write("a la ligne");
```

`WriteLine` ajoute un retour a la ligne, `Write` non.

## Les commentaires

```csharp
// Commentaire sur une ligne
/* Commentaire
   sur plusieurs lignes */
Console.WriteLine("Code execute");
```

## Petite histoire

Nora cree son premier projet. Elle modifie le message, relance `dotnet run`, et voit son texte. Premier programme en 2 minutes.

## A retenir

- `Console.WriteLine()` affiche du texte.
- `dotnet run` compile et execute.
- Top-level statements = code minimal.
