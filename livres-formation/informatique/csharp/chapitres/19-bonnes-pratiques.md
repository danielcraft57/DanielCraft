# Bonnes pratiques

## Conventions de nommage

- Classes, methodes, proprietes : `PascalCase`.
- Variables locales, parametres : `camelCase`.
- Champs prives : `_camelCase` (prefixe underscore).
- Constantes : `PascalCase` (pas de UPPER_CASE en C#).

## Structure d'un fichier

```csharp
using System;
using System.Collections.Generic;

namespace MonApp;

public class MaClasse
{
    private readonly List<string> _items = new();

    public void AjouterItem(string item)
    {
        if (string.IsNullOrWhiteSpace(item))
            throw new ArgumentException("Item vide");
        _items.Add(item);
    }
}
```

## Principes

- **Une classe = une responsabilite.**
- **Methodes courtes** : si ca depasse 20 lignes, decoupe.
- **Immutabilite** : prefere `readonly` et `init` quand possible.
- **Nullable** : active les nullable reference types et gere les `?`.

## Documentation

```csharp
/// <summary>
/// Calcule le prix TTC a partir du HT.
/// </summary>
decimal CalculerTtc(decimal prixHt, decimal tva = 0.20m)
    => prixHt * (1 + tva);
```

> **Astuce DanielCraft** - Installe un analyseur (Roslyn, SonarLint) pour detecter les problemes automatiquement.

## A retenir

- PascalCase partout sauf variables locales.
- Le compilateur + analyseur = filet de securite.
- Petites methodes, noms explicites, tests.
