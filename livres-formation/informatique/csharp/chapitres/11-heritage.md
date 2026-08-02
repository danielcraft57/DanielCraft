# L'heritage

## Reutiliser du code

L'heritage permet a une classe enfant de reprendre les membres d'une classe parent et d'en ajouter ou modifier.

```csharp
class Animal
{
    public string Nom { get; set; }
    public virtual void Crier()
    {
        Console.WriteLine("...");
    }
}

class Chat : Animal
{
    public override void Crier()
    {
        Console.WriteLine("Miaou !");
    }
}

var felix = new Chat { Nom = "Felix" };
felix.Crier(); // Miaou !
```

## virtual et override

- `virtual` dans le parent : autorise la redefinition.
- `override` dans l'enfant : remplace le comportement.

## Le mot-cle base

```csharp
class Chien : Animal
{
    public override void Crier()
    {
        base.Crier(); // Appelle la version parent
        Console.WriteLine("Wouf !");
    }
}
```

> **Astuce DanielCraft** - N'abuse pas de l'heritage. Prefere la composition quand la relation "est un" n'est pas claire.

## Classes abstraites

```csharp
abstract class Forme
{
    public abstract double Aire();
}

class Cercle : Forme
{
    public double Rayon { get; set; }
    public override double Aire() => Math.PI * Rayon * Rayon;
}
```

Une classe abstraite ne peut pas etre instanciee directement.

## Petite histoire

Nora cree une hierarchie `Vehicule` -> `Voiture` / `Moto`. Chaque sous-classe a ses propres regles de consommation.

## A retenir

- `: ParentClass` pour heriter.
- `virtual` + `override` pour le polymorphisme.
- `abstract` pour forcer l'implementation.
- Composition > heritage quand le doute existe.
