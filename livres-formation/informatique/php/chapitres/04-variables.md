# Les variables

## Declarer une variable

En PHP, toute variable commence par `$`. Pas besoin de declarer le type : PHP est a typage dynamique.

```php
$prenom = "Max";
$age = 24;
$prix = 19.99;
$actif = true;
```

## Regles de nommage

- Commence par `$` suivi d'une lettre ou underscore.
- Sensible a la casse : `$nom` et `$Nom` sont differents.
- Convention : camelCase (`$monScore`) ou snake_case (`$mon_score`).

> **Astuce DanielCraft** - En PHP, `$` est obligatoire. Sans lui, c'est une constante ou un mot-cle.

## Affichage

```php
$ville = "Lyon";
echo "Je vis a $ville";          // Interpolation (guillemets doubles)
echo 'Je vis a ' . $ville;      // Concatenation (point)
echo "Prix : {$prix} EUR";      // Accolades pour les expressions
```

## Constantes

```php
define("TVA", 0.20);
const PAYS = "France";
echo TVA;   // 0.2
echo PAYS;  // France
```

## Petite histoire

Sam stocke `$salaire = 1800` et `$loyer = 650`. Il affiche `$salaire - $loyer`. PHP repond 1150.

## Erreur classique

```php
echo $prnom;  // Warning : variable non definie (faute de frappe)
```

PHP affiche un warning mais continue. Active `error_reporting(E_ALL)` pour tout voir.

## A retenir

- `$` obligatoire devant chaque variable.
- Guillemets doubles pour l'interpolation.
- Point `.` pour la concatenation.
