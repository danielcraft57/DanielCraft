# Les methodes

## Pourquoi des methodes ?

Une methode regroupe du code reutilisable sous un nom. En C# tout code vit dans une methode (meme implicitement avec les top-level statements).

```csharp
void Saluer(string prenom)
{
    Console.WriteLine($"Bonjour {prenom} !");
}

Saluer("Nora");
Saluer("Max");
```

## Retourner une valeur

```csharp
int Additionner(int a, int b)
{
    return a + b;
}

int resultat = Additionner(3, 7);
Console.WriteLine(resultat); // 10
```

## Parametres optionnels

```csharp
void Presenter(string nom, string langue = "francais")
{
    Console.WriteLine($"{nom} parle {langue}");
}

Presenter("Lea");            // Lea parle francais
Presenter("Tom", "anglais"); // Tom parle anglais
```

> **Astuce DanielCraft** - Une methode = une responsabilite. Si elle fait trop de choses, decoupe-la.

## Expression-bodied

```csharp
double CalculerTtc(double ht) => ht * 1.20;
```

Pour les methodes courtes, la fleche `=>` remplace les accolades et le `return`.

## Petite histoire

Max ecrit 3 fois le meme calcul de TVA. Sam lui montre `CalculerTtc()`. Le code passe de 15 lignes a 5.

## A retenir

- `void` si pas de retour, sinon le type retourne.
- Parametres optionnels avec `= valeur`.
- `=>` pour les methodes d'une expression.
- Une methode = une responsabilite.
