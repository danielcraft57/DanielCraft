# Modules et heritage

## Heritage

```ruby
class Chien < Animal
  def parler
    "Wouf !"
  end
end
```

## Modules (mixins)

```ruby
module Affichable
  def afficher
    puts to_s
  end
end

class Produit
  include Affichable
end
```

## A retenir

- `< Parent` pour heriter.
- `module` + `include` pour partager du comportement.
- Ruby : heritage simple + mixins.
