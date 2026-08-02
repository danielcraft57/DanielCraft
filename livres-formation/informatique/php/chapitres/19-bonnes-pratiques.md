# Bonnes pratiques

## Style de code

- **PSR-12** : le standard de style PHP.
- camelCase pour les methodes et variables.
- PascalCase pour les classes.
- 4 espaces pour l'indentation.

## Typage strict

```php
declare(strict_types=1);

function calculerTtc(float $ht, float $tva = 0.20): float {
    return $ht * (1 + $tva);
}
```

`declare(strict_types=1)` en haut de chaque fichier force la verification des types.

> **Astuce DanielCraft** - Active toujours `strict_types`. Ca detecte les bugs tot.

## Securite

- `htmlspecialchars()` pour l'affichage.
- `filter_input()` pour la validation.
- Requetes preparees (PDO) pour les bases de donnees.
- Ne jamais faire confiance aux donnees utilisateur.

## Organisation

```php
// 1. declare + namespace
declare(strict_types=1);
namespace App;

// 2. use
use App\Service\MailService;

// 3. Classe
class ContactController {
    // ...
}
```

## Outils

- **Composer** : gestionnaire de dependances.
- **PHPStan / Psalm** : analyse statique.
- **PHP CS Fixer** : formatage automatique.

## A retenir

- `declare(strict_types=1)` dans chaque fichier.
- PSR-12 pour le style.
- PHPStan pour detecter les erreurs avant l'execution.
