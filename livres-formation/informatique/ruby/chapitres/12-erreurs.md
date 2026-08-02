# Gerer les erreurs

```ruby
begin
  resultat = 10 / 0
rescue ZeroDivisionError => e
  puts "Erreur : #{e.message}"
ensure
  puts "Toujours execute"
end
```

## Lever une erreur

```ruby
def retirer(solde, montant)
  raise "Solde insuffisant" if montant > solde
  solde - montant
end
```

## A retenir

- `begin` / `rescue` / `ensure` / `end`.
- `raise` pour lever une exception.
- `rescue => e` pour attraper.
