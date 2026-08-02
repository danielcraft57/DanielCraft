# Les tableaux

## Tableaux indexes

```php
$fruits = ["pomme", "banane", "cerise"];
echo $fruits[0];   // pomme
echo count($fruits); // 3
```

## Ajouter et supprimer

```php
$fruits[] = "kiwi";           // Ajoute a la fin
array_push($fruits, "mangue");
array_splice($fruits, 1, 1);  // Supprime l'index 1
unset($fruits[0]);             // Supprime l'index 0
```

## Tableaux associatifs

```php
$personne = [
    "nom" => "Lea",
    "age" => 28,
    "ville" => "Bordeaux",
];
echo $personne["nom"]; // Lea
```

## Parcourir

```php
foreach ($personne as $cle => $valeur) {
    echo "$cle: $valeur\n";
}
```

## Fonctions utiles

| Fonction | Role |
|----------|------|
| `count()` | Nombre d'elements |
| `in_array()` | Verifie la presence |
| `array_keys()` | Les cles |
| `array_values()` | Les valeurs |
| `sort()` | Trie (modifie) |
| `array_map()` | Applique une fonction |
| `array_filter()` | Filtre les elements |

> **Astuce DanielCraft** - En PHP, les tableaux servent de liste ET de dictionnaire. Un seul type pour tout.

## Petite histoire

Nora stocke les prix dans un tableau associatif. Elle calcule le total avec `array_sum(array_values($prix))`.

## A retenir

- `[]` pour creer, `$tab[]` pour ajouter.
- `=>` pour les paires cle-valeur.
- `foreach` pour parcourir.
