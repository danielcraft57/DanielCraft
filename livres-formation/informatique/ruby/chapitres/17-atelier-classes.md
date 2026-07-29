# Atelier : classes

```ruby
class Produit
  attr_reader :nom
  attr_accessor :prix

  def initialize(nom, prix)
    @nom = nom
    @prix = prix
  end

  def afficher
    "#{@nom} - #{@prix.round(2)} EUR"
  end
end
```
