# Atelier : classes

## Objectif

Modeliser des objets du monde reel avec des classes.

## Exercice 1 : classe Produit

```csharp
class Produit
{
    public string Nom { get; set; }
    public decimal Prix { get; set; }

    public Produit(string nom, decimal prix)
    {
        Nom = nom;
        Prix = prix;
    }

    public string Afficher() => $"{Nom} - {Prix:F2} EUR";
}

var p = new Produit("Clavier", 49.99m);
Console.WriteLine(p.Afficher());
```

## Exercice 2 : panier d'achat

```csharp
class Panier
{
    private List<Produit> _produits = new();

    public void Ajouter(Produit p) => _produits.Add(p);
    public decimal Total() => _produits.Sum(p => p.Prix);
    public void Afficher()
    {
        foreach (var p in _produits)
            Console.WriteLine($"  {p.Afficher()}");
        Console.WriteLine($"Total : {Total():F2} EUR");
    }
}

var panier = new Panier();
panier.Ajouter(new Produit("Souris", 29.99m));
panier.Ajouter(new Produit("Ecran", 249.00m));
panier.Afficher();
```

## Exercice 3 : heritage Vehicule

```csharp
class Vehicule
{
    public string Marque { get; set; } = "";
    public virtual double Consommation() => 0;
}

class Voiture : Vehicule
{
    public override double Consommation() => 6.5;
}

class Moto : Vehicule
{
    public override double Consommation() => 4.0;
}
```

> **Astuce DanielCraft** - Pense "est-un" pour l'heritage. Une Voiture "est un" Vehicule. Un Panier "a des" Produits (composition).

## A retenir

- Constructeur pour initialiser.
- `private` pour proteger les donnees internes.
- Heritage quand la relation "est un" est naturelle.
