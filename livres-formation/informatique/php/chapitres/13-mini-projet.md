# Mini-projet : page de contacts

## L'objectif

On cree une page web PHP qui permet d'ajouter et lister des contacts. Les donnees sont stockees dans un fichier JSON. Ce projet combine formulaires, tableaux, fonctions, fichiers et HTML.

## Structure

```php
<?php
$fichier = 'contacts.json';

function charger(string $f): array {
    if (!file_exists($f)) return [];
    $json = file_get_contents($f);
    return json_decode($json, true) ?? [];
}

function sauvegarder(string $f, array $contacts): void {
    file_put_contents($f, json_encode($contacts, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE));
}

$contacts = charger($fichier);

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $nom = trim($_POST['nom'] ?? '');
    $tel = trim($_POST['tel'] ?? '');
    if ($nom !== '' && $tel !== '') {
        $contacts[] = ['nom' => $nom, 'tel' => $tel];
        sauvegarder($fichier, $contacts);
    }
}
?>
<!DOCTYPE html>
<html lang="fr">
<head><meta charset="UTF-8"><title>Contacts</title></head>
<body>
<h1>Mes contacts</h1>
<form method="POST">
    <input name="nom" placeholder="Nom" required>
    <input name="tel" placeholder="Telephone" required>
    <button type="submit">Ajouter</button>
</form>
<ul>
<?php foreach ($contacts as $c): ?>
    <li><?= htmlspecialchars($c['nom']) ?> - <?= htmlspecialchars($c['tel']) ?></li>
<?php endforeach; ?>
</ul>
</body>
</html>
```

## Ce que tu apprends

- `json_encode` / `json_decode` pour la persistance.
- Traitement de formulaire POST.
- `htmlspecialchars` pour la securite.
- Syntaxe alternative `foreach ... endforeach` dans le HTML.

> **Astuce DanielCraft** - Commence par le formulaire HTML, puis ajoute le PHP progressivement.

## A retenir

- Un projet = assemblage de notions.
- JSON pour persister sans base de donnees.
- Toujours echapper les sorties HTML.
