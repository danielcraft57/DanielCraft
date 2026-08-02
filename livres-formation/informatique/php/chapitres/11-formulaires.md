# Les formulaires

## Recevoir des donnees

PHP excelle dans le traitement de formulaires HTML.

```html
<form method="POST" action="traiter.php">
    <input type="text" name="prenom">
    <button type="submit">Envoyer</button>
</form>
```

```php
// traiter.php
$prenom = $_POST['prenom'] ?? '';
echo "Bonjour $prenom !";
```

## GET vs POST

| Methode | Usage | Donnees visibles |
|---------|-------|-----------------|
| GET | Recherche, filtres | Oui (dans l'URL) |
| POST | Formulaires, creation | Non |

## Valider les entrees

```php
$email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
if ($email === false) {
    echo "Email invalide";
}
```

## Securiser les sorties

```php
$nom = htmlspecialchars($_POST['nom'] ?? '', ENT_QUOTES, 'UTF-8');
echo "Bonjour $nom";
```

> **Piege** - Ne jamais afficher une donnee utilisateur sans `htmlspecialchars()`. Sinon : faille XSS.

## Petite histoire

Nora cree un formulaire de contact. Elle valide l'email, echappe le nom, et envoie les donnees par mail. Securise des le debut.

## A retenir

- `$_GET` et `$_POST` pour recevoir les donnees.
- `filter_input()` pour valider.
- `htmlspecialchars()` pour securiser l'affichage.
