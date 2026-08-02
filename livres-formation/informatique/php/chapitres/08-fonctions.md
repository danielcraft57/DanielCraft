# Les fonctions

## Declarer une fonction

```php
function saluer(string $prenom): void {
    echo "Bonjour $prenom !\n";
}

saluer("Nora");
```

## Retourner une valeur

```php
function additionner(int $a, int $b): int {
    return $a + $b;
}

$resultat = additionner(3, 7);
echo $resultat; // 10
```

## Parametres optionnels

```php
function presenter(string $nom, string $langue = "francais"): string {
    return "$nom parle $langue";
}

echo presenter("Lea");            // Lea parle francais
echo presenter("Tom", "anglais"); // Tom parle anglais
```

## Types de retour (PHP 8+)

```php
function diviser(float $a, float $b): float|false {
    if ($b == 0) return false;
    return $a / $b;
}
```

> **Astuce DanielCraft** - Depuis PHP 8, utilise les types dans les signatures. Ca documente et protege.

## Fonctions anonymes et fleches

```php
$doubler = fn($x) => $x * 2;
echo $doubler(5); // 10

$filtrer = array_filter([1,2,3,4,5], fn($n) => $n > 3);
// [4, 5]
```

## Petite histoire

Max ecrit 3 fois le meme calcul de TVA. Sam lui montre `calculerTtc($prixHt)`. Le code passe de 15 lignes a 5.

## A retenir

- `function nom(params): typeRetour { ... }`
- Types dans les signatures (PHP 8+).
- `fn($x) => expr` pour les fonctions fleches.
