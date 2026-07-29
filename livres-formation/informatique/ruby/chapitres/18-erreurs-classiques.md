# Erreurs classiques

## 1. Oublier end

Chaque `def`, `class`, `if`, `do` necessite un `end`.

## 2. Confondre symbole et string

```ruby
hash = { nom: "Lea" }
hash["nom"]   # nil !
hash[:nom]    # "Lea"
```

## 3. Modifier un array en iteration

```ruby
arr = [1, 2, 3]
arr.each { |x| arr.delete(x) }  # Comportement inattendu
```

## 4. nil implicite

```ruby
resultat = hash[:absent]
resultat.upcase  # NoMethodError sur nil
```

Utilise `&.` (safe navigation) ou verifie nil.

> **Piege** - Ruby est permissif. Teste souvent en console (`irb`).
