# Erreurs classiques en PHP

## 1. Oublier le $ devant une variable

```php
echo nom;  // Constante "nom" non definie
echo $nom; // Correct
```

## 2. Confondre = et ==

```php
if ($x = 5) { }   // Assigne ! Toujours vrai.
if ($x == 5) { }   // Compare
if ($x === 5) { }  // Compare strictement
```

## 3. Type juggling surprenant

```php
var_dump("0" == false);  // true
var_dump("" == false);   // true
var_dump("abc" == 0);    // true en PHP 7 !
```

Utilise `===` pour eviter les surprises.

## 4. Oublier htmlspecialchars

```php
echo $_GET['nom'];  // Faille XSS !
echo htmlspecialchars($_GET['nom'], ENT_QUOTES, 'UTF-8'); // Securise
```

## 5. Tableau non initialise

```php
$items[] = "test";  // Warning si $items n'existe pas
$items = [];        // Initialise d'abord
$items[] = "test";
```

## 6. Point-virgule oublie

```php
echo "Bonjour"  // ParseError !
echo "Bonjour"; // Correct
```

> **Astuce DanielCraft** - Active `error_reporting(E_ALL)` et `display_errors` en dev. En production, logge les erreurs.

## A retenir

- `$` obligatoire, `;` obligatoire.
- `===` plutot que `==`.
- `htmlspecialchars()` pour toute sortie.
