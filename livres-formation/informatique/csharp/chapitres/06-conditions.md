# Les conditions

## Prendre une decision

```csharp
int age = 17;
if (age >= 18)
{
    Console.WriteLine("Majeur");
}
else
{
    Console.WriteLine("Mineur");
}
```

## if / else if / else

```csharp
int note = 14;
if (note >= 16)
    Console.WriteLine("Tres bien");
else if (note >= 12)
    Console.WriteLine("Bien");
else if (note >= 10)
    Console.WriteLine("Passable");
else
    Console.WriteLine("Insuffisant");
```

> **Astuce DanielCraft** - Les accolades sont facultatives pour une seule instruction, mais recommandees pour la lisibilite.

## Operateurs de comparaison

| Operateur | Signification |
|-----------|---------------|
| `==` | Egal |
| `!=` | Different |
| `<` `>` | Inferieur / superieur |
| `<=` `>=` | Inferieur ou egal / superieur ou egal |

## Operateurs logiques

```csharp
if (age >= 18 && permis)
    Console.WriteLine("Peut conduire");

if (estEtudiant || estSenior)
    Console.WriteLine("Tarif reduit");
```

## Switch

```csharp
string jour = "lundi";
switch (jour)
{
    case "lundi":
    case "mardi":
        Console.WriteLine("Debut de semaine");
        break;
    case "vendredi":
        Console.WriteLine("Presque le weekend");
        break;
    default:
        Console.WriteLine("Autre jour");
        break;
}
```

## Petite histoire

Max ecrit un programme qui verifie l'age et le permis avant d'afficher "Acces autorise". Deux conditions, un `&&`, et c'est fait.

## A retenir

- `if / else if / else` pour decider.
- `switch` pour comparer une valeur a plusieurs cas.
- `&&` (et), `||` (ou), `!` (non).
