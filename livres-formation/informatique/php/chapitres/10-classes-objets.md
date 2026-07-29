# Classes et objets

## C'est quoi une classe ?

```php
class Animal {
    public string $nom;
    public int $age;

    public function __construct(string $nom, int $age) {
        $this->nom = $nom;
        $this->age = $age;
    }

    public function sePresenter(): string {
        return "Je suis {$this->nom}, {$this->age} ans.";
    }
}

$chat = new Animal("Felix", 3);
echo $chat->sePresenter();
```

## Constructeur promu (PHP 8+)

```php
class Personne {
    public function __construct(
        public readonly string $nom,
        public readonly int $age,
    ) {}
}

$p = new Personne("Lea", 28);
echo $p->nom;
```

> **Astuce DanielCraft** - Les constructeurs promus (PHP 8) reduisent le boilerplate. Utilise-les.

## Visibilite

- `public` : accessible partout.
- `protected` : accessible dans la classe et ses enfants.
- `private` : accessible uniquement dans la classe.

## Heritage

```php
class Chat extends Animal {
    public function miauler(): string {
        return "{$this->nom} fait Miaou !";
    }
}
```

## Petite histoire

Max modele un `Produit` avec nom et prix. Il cree un tableau d'objets et calcule le total avec `array_sum(array_map(...))`.

## A retenir

- `class` + `new` pour creer des objets.
- `$this->` pour acceder aux proprietes.
- Constructeur promu (PHP 8+) pour simplifier.
