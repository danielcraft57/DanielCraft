# Les conditions

## if / else

```php
$age = 17;
if ($age >= 18) {
    echo "Majeur";
} else {
    echo "Mineur";
}
```

## if / elseif / else

```php
$note = 14;
if ($note >= 16) {
    echo "Tres bien";
} elseif ($note >= 12) {
    echo "Bien";
} elseif ($note >= 10) {
    echo "Passable";
} else {
    echo "Insuffisant";
}
```

## Operateur ternaire

```php
$statut = ($age >= 18) ? "Majeur" : "Mineur";
```

## Null coalescing

```php
$nom = $_GET['nom'] ?? "Inconnu";
```

`??` retourne la valeur de gauche si elle existe et n'est pas null, sinon celle de droite.

> **Astuce DanielCraft** - `??` est tres utile pour les parametres GET/POST optionnels.

## Switch

```php
$jour = "lundi";
switch ($jour) {
    case "lundi":
    case "mardi":
        echo "Debut de semaine";
        break;
    case "vendredi":
        echo "Presque le weekend";
        break;
    default:
        echo "Autre jour";
}
```

## Match (PHP 8+)

```php
$resultat = match($jour) {
    "lundi", "mardi" => "Debut de semaine",
    "vendredi" => "Presque le weekend",
    default => "Autre jour",
};
```

## Petite histoire

Max remplace un switch de 20 lignes par un match de 5 lignes. PHP 8 simplifie le code.

## A retenir

- `if / elseif / else` pour decider.
- `??` pour les valeurs par defaut.
- `match` (PHP 8+) remplace souvent `switch`.
