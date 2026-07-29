# Les methodes

```ruby
def saluer(prenom)
  puts "Bonjour #{prenom} !"
end

def additionner(a, b)
  a + b
end
```

La derniere expression est retournee automatiquement (pas de `return` obligatoire).

## Parametres par defaut

```ruby
def saluer(prenom, message = "Bonjour")
  puts "#{message} #{prenom} !"
end
```

## Blocs

```ruby
def repeter(n)
  n.times { yield }
end

repeter(3) { puts "Ruby !" }
```

> **Astuce DanielCraft** - Les blocs `{ }` ou `do..end` sont partout en Ruby. C'est une force du langage.

## A retenir

- `def nom(params)` / `end`.
- Retour implicite (derniere expression).
- Blocs avec `yield`.
