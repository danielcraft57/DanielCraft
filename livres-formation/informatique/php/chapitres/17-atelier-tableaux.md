# Atelier : tableaux

## Exercice 1 : filtrer les pairs

```php
$nombres = [3, 8, 1, 12, 7, 4, 15, 2];
$pairs = array_filter($nombres, fn($n) => $n % 2 === 0);
print_r(array_values($pairs));
```

## Exercice 2 : compteur de mots

```php
$phrase = "le chat dort le chat mange le chat joue";
$mots = explode(" ", $phrase);
$compteur = array_count_values($mots);
print_r($compteur);
```

## Exercice 3 : transformer un tableau

```php
$noms = ["lea", "max", "sam"];
$majuscules = array_map('ucfirst', $noms);
print_r($majuscules); // [Lea, Max, Sam]
```

## Exercice 4 : panier d'achat

```php
$panier = [
    ["nom" => "Pain", "prix" => 1.20],
    ["nom" => "Lait", "prix" => 0.95],
    ["nom" => "Oeufs", "prix" => 2.50],
];
$total = array_sum(array_column($panier, "prix"));
echo "Total : " . number_format($total, 2) . " EUR\n";
```

> **Astuce DanielCraft** - `array_column()` extrait une colonne d'un tableau multidimensionnel. Tres pratique.

## A retenir

- `array_filter()`, `array_map()`, `array_column()`.
- `array_count_values()` pour compter les occurrences.
- `explode()` pour decouper une chaine en tableau.
