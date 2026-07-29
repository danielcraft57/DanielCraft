# Atelier : methodes

## Objectif

Creer des methodes avec differents types de retour et parametres.

## Exercice 1 : salutation

```csharp
string Saluer(string nom, int heure)
{
    if (heure < 12) return $"Bonjour {nom} !";
    if (heure < 18) return $"Bon apres-midi {nom} !";
    return $"Bonsoir {nom} !";
}

Console.WriteLine(Saluer("Lea", 9));
Console.WriteLine(Saluer("Max", 20));
```

## Exercice 2 : moyenne

```csharp
double Moyenne(int[] notes)
{
    if (notes.Length == 0) return 0;
    return notes.Average();
}

Console.WriteLine(Moyenne(new[] { 14, 16, 11, 18 }));
```

## Exercice 3 : mot de passe valide

```csharp
bool MdpValide(string mdp)
{
    return mdp.Length >= 8 && mdp.Any(char.IsDigit);
}

Console.WriteLine(MdpValide("abc"));       // False
Console.WriteLine(MdpValide("CSharp3!")); // True
```

## Exercice 4 : factorielle

```csharp
long Factorielle(int n)
{
    if (n <= 1) return 1;
    return n * Factorielle(n - 1);
}

Console.WriteLine(Factorielle(5)); // 120
```

> **Astuce DanielCraft** - Teste chaque methode avec des cas normaux et des cas limites (0, vide, negatif).

## A retenir

- Bien choisir le type de retour.
- Expression-bodied (`=>`) pour les methodes courtes.
- LINQ (`.Any()`, `.Average()`) simplifie le code.
