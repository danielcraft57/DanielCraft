# Les boucles

## Repeter du code

Une boucle execute un bloc plusieurs fois. C# propose `for`, `while`, `do-while` et `foreach`.

## La boucle for

```csharp
for (int i = 0; i < 5; i++)
{
    Console.WriteLine(i);
}
// Affiche 0, 1, 2, 3, 4
```

## La boucle foreach

```csharp
string[] fruits = { "pomme", "banane", "cerise" };
foreach (string fruit in fruits)
{
    Console.WriteLine(fruit);
}
```

`foreach` parcourt chaque element sans index.

## La boucle while

```csharp
int compteur = 0;
while (compteur < 3)
{
    Console.WriteLine(compteur);
    compteur++;
}
```

> **Piege** - Oublier `compteur++` = boucle infinie. Ctrl+C pour arreter.

## break et continue

```csharp
for (int i = 0; i < 10; i++)
{
    if (i == 5) break;
    if (i % 2 == 0) continue;
    Console.WriteLine(i); // 1, 3
}
```

> **Astuce DanielCraft** - `foreach` quand tu parcours une collection. `for` quand tu as besoin de l'index.

## Petite histoire

Sam affiche les tables de multiplication avec deux boucles imbriquees. 4 lignes pour un resultat que recopier prendrait des heures.

## A retenir

- `for` : nombre d'iterations connu.
- `foreach` : parcourir une collection.
- `while` : condition d'arret.
- `break` sort, `continue` passe au suivant.
