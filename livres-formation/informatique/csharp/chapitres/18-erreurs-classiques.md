# Erreurs classiques en C#

## Les pieges des debutants

## 1. NullReferenceException

```csharp
string? nom = null;
Console.WriteLine(nom.Length); // NullReferenceException
```

Verifie toujours si une variable peut etre null.

## 2. Oublier break dans switch

```csharp
switch (x)
{
    case 1:
        Console.WriteLine("Un");
        // Oubli de break -> erreur de compilation en C#
        break;
}
```

En C#, le compilateur exige un `break` (pas de "fall-through" implicite).

## 3. Comparer des strings avec ==

En C#, `==` sur les strings compare les valeurs (contrairement a Java). Donc `==` fonctionne correctement. Piege evite !

## 4. Modifier une collection en iterant

```csharp
foreach (var item in liste)
{
    liste.Remove(item); // InvalidOperationException !
}
```

Solution : creer une copie ou utiliser `RemoveAll`.

## 5. Index hors limites

```csharp
int[] tab = { 1, 2, 3 };
Console.WriteLine(tab[3]); // IndexOutOfRangeException
```

## 6. Oublier le point-virgule

```csharp
Console.WriteLine("Oups") // Erreur CS1002
```

## 7. Confondre = et ==

```csharp
if (x = 5) // Erreur : = assigne, == compare
```

Le compilateur C# refuse cette ecriture (contrairement a C/C++).

> **Astuce DanielCraft** - Le compilateur C# est strict. La plupart des erreurs sont detectees avant meme l'execution.

## A retenir

- Le compilateur est ton allie : lis ses messages.
- Null est le piege numero 1.
- Ne modifie pas une collection pendant son iteration.
