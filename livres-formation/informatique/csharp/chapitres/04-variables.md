# Les variables

## C'est quoi une variable ?

Une variable est un espace memoire nomme qui contient une valeur. En C#, on declare le type ou on laisse le compilateur le deviner avec `var`.

```csharp
string prenom = "Max";
int age = 24;
var ville = "Lyon"; // Le compilateur deduit string
```

## Regles de nommage

- camelCase pour les variables locales : `monScore`, `prixTotal`.
- Pas de mots reserves (`int`, `class`, `if`...).
- Commence par une lettre ou underscore.
- Sensible a la casse : `nom` et `Nom` sont differents.

> **Astuce DanielCraft** - Utilise `var` quand le type est evident. Explicit quand ca aide a la lisibilite.

## Modifier une variable

```csharp
int score = 0;
score = score + 10;
score += 5;
Console.WriteLine(score); // 15
```

## Interpolation de chaines

```csharp
string ville = "Paris";
Console.WriteLine($"Je vis a {ville}");
```

Le `$` avant les guillemets active l'interpolation (comme f-string en Python).

## Constantes

```csharp
const double TVA = 0.20;
// TVA = 0.25; // Erreur ! Une constante ne change pas.
```

## Petite histoire

Sam stocke `salaire = 1800` et `loyer = 650`. Il affiche `reste = salaire - loyer`. C# lui repond 1150, sans surprise.

## Erreur classique

```csharp
Console.WriteLine(prnom); // Erreur CS0103 : variable inexistante
```

Le compilateur refuse immediatement. Pas d'attente jusqu'a l'execution.

## A retenir

- Declarer avec un type ou `var`.
- camelCase pour les variables locales.
- `$"..."` pour l'interpolation.
- `const` pour les valeurs qui ne changent pas.
