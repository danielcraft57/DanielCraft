# Atelier : fonctions

## Exercice 1 : salutation

```php
function saluer(string $nom, int $heure): string {
    if ($heure < 12) return "Bonjour $nom !";
    if ($heure < 18) return "Bon apres-midi $nom !";
    return "Bonsoir $nom !";
}

echo saluer("Lea", 9) . "\n";
echo saluer("Max", 20) . "\n";
```

## Exercice 2 : moyenne

```php
function moyenne(array $notes): float {
    if (count($notes) === 0) return 0;
    return array_sum($notes) / count($notes);
}

echo moyenne([14, 16, 11, 18]); // 14.75
```

## Exercice 3 : mot de passe valide

```php
function mdpValide(string $mdp): bool {
    return strlen($mdp) >= 8 && preg_match('/\d/', $mdp);
}

var_dump(mdpValide("abc"));       // false
var_dump(mdpValide("PHP8rocks!")); // true
```

## Exercice 4 : fonction fleche

```php
$ttc = fn(float $ht) => $ht * 1.20;
echo $ttc(100); // 120
```

> **Astuce DanielCraft** - `array_sum()`, `count()`, `preg_match()` : PHP a des fonctions pour presque tout.

## A retenir

- Types dans les signatures pour la clarte.
- Fonctions fleches `fn()` pour les expressions courtes.
- La bibliotheque standard PHP est enorme.
