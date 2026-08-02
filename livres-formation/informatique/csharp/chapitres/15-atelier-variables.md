# Atelier : variables et types

## Objectif

Pratiquer les declarations, conversions et interpolations.

## Exercice 1 : carte d'identite

```csharp
string prenom = "Sam";
int age = 22;
string ville = "Nantes";
Console.WriteLine($"Je suis {prenom}, {age} ans, je vis a {ville}.");
```

## Exercice 2 : convertisseur EUR -> USD

```csharp
Console.Write("Montant en EUR : ");
decimal euros = decimal.Parse(Console.ReadLine()!);
decimal dollars = euros * 1.08m;
Console.WriteLine($"{euros} EUR = {dollars:F2} USD");
```

## Exercice 3 : temperature

Convertir Celsius en Fahrenheit : `F = C * 9/5 + 32`.

```csharp
Console.Write("Celsius : ");
double c = double.Parse(Console.ReadLine()!);
double f = c * 9.0 / 5.0 + 32.0;
Console.WriteLine($"{c}°C = {f:F1}°F");
```

## Defi : aire et perimetre

```csharp
Console.Write("Rayon : ");
double rayon = double.Parse(Console.ReadLine()!);
Console.WriteLine($"Perimetre : {2 * Math.PI * rayon:F2}");
Console.WriteLine($"Aire : {Math.PI * rayon * rayon:F2}");
```

> **Astuce DanielCraft** - `:F2` formate avec 2 decimales. Pratique pour l'affichage.

## A retenir

- `$"..."` pour l'interpolation.
- `decimal` pour l'argent, `double` pour les calculs scientifiques.
- `:F2` pour formater les nombres.
