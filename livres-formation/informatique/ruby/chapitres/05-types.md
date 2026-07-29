# Les types

Ruby est dynamique : pas de declaration de type.

| Type | Exemple |
|------|---------|
| Integer | `42` |
| Float | `3.14` |
| String | `"Bonjour"` |
| Boolean | `true`, `false` |
| nil | `nil` (absence de valeur) |

## Verifier un type

```ruby
42.class          # Integer
"texte".is_a?(String)  # true
```

## Conversion

```ruby
"42".to_i         # 42
42.to_s           # "42"
```

## A retenir

- Typage dynamique.
- `nil` = absence de valeur.
- `.to_i`, `.to_s`, `.to_f` pour convertir.
