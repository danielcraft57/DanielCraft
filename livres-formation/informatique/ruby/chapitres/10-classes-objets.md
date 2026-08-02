# Classes et objets

```ruby
class Animal
  def initialize(nom, age)
    @nom = nom
    @age = age
  end

  def se_presenter
    "Je suis #{@nom}, #{@age} ans."
  end
end

chat = Animal.new("Felix", 3)
puts chat.se_presenter
```

## Attributs

```ruby
class Produit
  attr_reader :nom
  attr_accessor :prix

  def initialize(nom, prix)
    @nom = nom
    @prix = prix
  end
end
```

## A retenir

- `class` / `def initialize` / `end`.
- `@variable` = variable d'instance.
- `attr_reader`, `attr_accessor`.
