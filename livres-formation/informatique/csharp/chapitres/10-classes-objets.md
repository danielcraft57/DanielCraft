# Classes et objets

## C'est quoi une classe ?

Une classe est un plan. Un objet est une instance de ce plan. La classe definit les proprietes et methodes ; l'objet les utilise.

```csharp
class Animal
{
    public string Nom { get; set; }
    public int Age { get; set; }

    public void SePresenter()
    {
        Console.WriteLine($"Je suis {Nom}, {Age} ans.");
    }
}

var chat = new Animal { Nom = "Felix", Age = 3 };
chat.SePresenter(); // Je suis Felix, 3 ans.
```

## Constructeur

```csharp
class Personne
{
    public string Nom { get; }
    public int Age { get; }

    public Personne(string nom, int age)
    {
        Nom = nom;
        Age = age;
    }
}

var p = new Personne("Lea", 28);
```

> **Astuce DanielCraft** - PascalCase pour les classes et proprietes. camelCase pour les variables locales.

## Encapsulation

```csharp
class CompteBancaire
{
    public decimal Solde { get; private set; }

    public void Deposer(decimal montant)
    {
        if (montant > 0) Solde += montant;
    }
}
```

`private set` empeche la modification directe depuis l'exterieur.

## Petite histoire

Max modele un `Produit` avec un nom et un prix. Il cree une liste de produits et calcule le total avec LINQ (qu'il decouvrira au niveau intermediaire).

## A retenir

- Classe = plan. Objet = exemplaire.
- Proprietes avec `{ get; set; }`.
- Constructeur pour initialiser.
- Encapsulation : controler l'acces aux donnees.
