# Gerer les erreurs

## Les exceptions

En C#, les erreurs a l'execution sont des exceptions. On les attrape avec `try/catch`.

```csharp
try
{
    int nombre = int.Parse(Console.ReadLine()!);
    Console.WriteLine(10 / nombre);
}
catch (FormatException)
{
    Console.WriteLine("Ce n'est pas un nombre.");
}
catch (DivideByZeroException)
{
    Console.WriteLine("Division par zero impossible.");
}
```

## Les exceptions courantes

| Exception | Cause |
|-----------|-------|
| `NullReferenceException` | Acces a un objet null |
| `IndexOutOfRangeException` | Index hors limites |
| `FormatException` | Conversion invalide |
| `DivideByZeroException` | Division par zero |
| `FileNotFoundException` | Fichier introuvable |
| `InvalidOperationException` | Operation non valide |

## finally

```csharp
try
{
    // Code risque
}
catch (Exception ex)
{
    Console.WriteLine($"Erreur : {ex.Message}");
}
finally
{
    Console.WriteLine("Toujours execute");
}
```

## Lever une exception

```csharp
void Retirer(decimal solde, decimal montant)
{
    if (montant > solde)
        throw new InvalidOperationException("Solde insuffisant");
}
```

> **Astuce DanielCraft** - N'attrape que ce que tu sais gerer. Laisser remonter aide au debug.

## Petite histoire

Max demande un nombre. L'utilisateur tape "abc". Sans `try/catch` le programme plante. Avec, il redemande poliment.

## A retenir

- `try/catch` pour attraper les exceptions.
- Precise le type d'exception.
- `throw` pour lever tes propres erreurs.
- `finally` s'execute toujours.
