# Les boucles

## for

```php
for ($i = 0; $i < 5; $i++) {
    echo $i . " ";
}
// 0 1 2 3 4
```

## foreach

```php
$fruits = ["pomme", "banane", "cerise"];
foreach ($fruits as $fruit) {
    echo $fruit . "\n";
}
```

Avec la cle :

```php
foreach ($fruits as $index => $fruit) {
    echo "$index: $fruit\n";
}
```

## while

```php
$compteur = 0;
while ($compteur < 3) {
    echo $compteur . " ";
    $compteur++;
}
```

## do-while

```php
do {
    $saisie = readline("Un nombre > 0 : ");
} while ($saisie <= 0);
```

> **Astuce DanielCraft** - `foreach` est le plus utilise en PHP. Il parcourt tableaux et objets naturellement.

## break et continue

```php
for ($i = 0; $i < 10; $i++) {
    if ($i === 5) break;
    if ($i % 2 === 0) continue;
    echo $i . " "; // 1 3
}
```

## Petite histoire

Sam affiche les articles d'un panier avec `foreach`. Index, nom, prix : tout en 3 lignes.

## A retenir

- `foreach` pour les tableaux (le plus courant).
- `for` quand tu connais le nombre d'iterations.
- `while` pour une condition d'arret.
