# Atelier : variables et types

## Exercice 1 : carte d'identite

```php
$prenom = "Sam";
$age = 22;
$ville = "Nantes";
echo "Je suis $prenom, $age ans, je vis a $ville.\n";
```

## Exercice 2 : convertisseur EUR -> USD

```php
$euros = (float) readline("Montant en EUR : ");
$dollars = $euros * 1.08;
echo number_format($euros, 2) . " EUR = " . number_format($dollars, 2) . " USD\n";
```

## Exercice 3 : comparaison stricte

```php
var_dump("0" == false);   // true (type juggling)
var_dump("0" === false);  // false (comparaison stricte)
var_dump(0 == "abc");     // true en PHP 7, false en PHP 8
```

## Defi : temperature C -> F

```php
$c = (float) readline("Celsius : ");
$f = $c * 9 / 5 + 32;
echo "$c°C = " . number_format($f, 1) . "°F\n";
```

> **Astuce DanielCraft** - `number_format()` pour un affichage propre des nombres.

## A retenir

- `$` devant chaque variable.
- `===` pour la comparaison stricte.
- `number_format()` pour formater.
