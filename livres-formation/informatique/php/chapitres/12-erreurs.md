# Gerer les erreurs

## Les exceptions

```php
try {
    $nombre = intval(readline("Un nombre : "));
    if ($nombre === 0) {
        throw new InvalidArgumentException("Zero interdit");
    }
    echo 10 / $nombre;
} catch (InvalidArgumentException $e) {
    echo "Erreur : " . $e->getMessage();
} catch (DivisionByZeroError $e) {
    echo "Division par zero !";
} finally {
    echo "\nFin du bloc.";
}
```

## Erreurs courantes

| Erreur | Cause |
|--------|-------|
| `Warning` | Variable non definie, fichier absent |
| `Fatal error` | Appel de methode sur null |
| `TypeError` | Mauvais type d'argument |
| `ParseError` | Erreur de syntaxe |

## Configurer le reporting

```php
error_reporting(E_ALL);
ini_set('display_errors', '1');
```

> **Astuce DanielCraft** - Active `E_ALL` en developpement. Desactive `display_errors` en production.

## Lever une exception

```php
function retirer(float $solde, float $montant): float {
    if ($montant > $solde) {
        throw new RuntimeException("Solde insuffisant");
    }
    return $solde - $montant;
}
```

## Petite histoire

Max oublie un point-virgule. PHP affiche `ParseError`. Il lit le message, corrige, relance. En PHP 8, les messages d'erreur sont clairs.

## A retenir

- `try/catch/finally` pour les exceptions.
- `throw` pour lever ses erreurs.
- `error_reporting(E_ALL)` en dev.
