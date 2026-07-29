# Bonnes pratiques

- **RuboCop** : linter et formateur standard.
- Prefere `.each` a `for`.
- Methodes courtes, une responsabilite.
- Noms expressifs : `utilisateur_actif?` (le `?` indique un booleen).
- Tests avec **RSpec** ou Minitest.

```ruby
def utilisateur_majeur?(age)
  age >= 18
end
```

## A retenir

- Code idiomatique Ruby, pas du Java traduit.
- RuboCop + tests = qualite.
