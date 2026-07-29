# Symboles et hashes

## Symboles

```ruby
statut = :actif
puts statut.class  # Symbol
```

Un symbole est immutable et unique en memoire. Ideal pour les cles.

## Hashes

```ruby
ages = { lea: 28, sam: 22, nora: 30 }
puts ages[:lea]     # 28
ages[:max] = 25
```

## Syntaxe moderne

```ruby
personne = { nom: "Lea", ville: "Paris" }
personne.each { |cle, val| puts "#{cle} = #{val}" }
```

> **Astuce DanielCraft** - `:{cle}` cree un symbole. Les hashes sont omnipresents en Ruby (surtout Rails).

## A retenir

- `:symbole` = identifiant immutable.
- `{ cle: valeur }` = hash.
- Acces avec `[:cle]`.
