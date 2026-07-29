# Premier programme

## Hello World en PHP

```php
<?php
echo "Bonjour le monde !";
```

Cree un fichier `bonjour.php`, lance `php bonjour.php` dans le terminal (ou via le serveur integre dans le navigateur).

## Les balises PHP

```php
<!DOCTYPE html>
<html>
<body>
  <h1><?php echo "Titre dynamique"; ?></h1>
  <p>Texte statique HTML</p>
</body>
</html>
```

PHP s'integre dans le HTML avec `<?php ... ?>`. Le serveur execute le PHP et envoie du HTML au navigateur.

## echo vs print

```php
echo "Bonjour";      // Plus courant
echo "A", " ", "B";  // Accepte plusieurs arguments
print("Bonjour");    // Retourne 1 (rarement utile)
```

> **Astuce DanielCraft** - Utilise `echo` partout. C'est la convention.

## Les commentaires

```php
// Commentaire sur une ligne
# Aussi un commentaire
/* Commentaire
   sur plusieurs lignes */
```

## Petite histoire

Nora cree `index.php` avec un titre dynamique qui affiche la date du jour. Elle ouvre le navigateur et voit le resultat changer chaque jour.

## A retenir

- `<?php ... ?>` pour le code PHP.
- `echo` pour afficher.
- PHP genere du HTML envoye au navigateur.
