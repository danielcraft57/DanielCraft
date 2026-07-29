# Les boucles

## each (idiome principal)

```ruby
(0..4).each { |i| puts i }

fruits = ["pomme", "banane"]
fruits.each { |f| puts f }
```

## while / until

```ruby
n = 0
while n < 5
  puts n
  n += 1
end
```

## times

```ruby
5.times { |i| puts i }
```

## break et next

```ruby
(0..10).each do |i|
  break if i == 5
  next if i.even?
  puts i
end
```

> **Astuce DanielCraft** - Prefere `.each` aux boucles `for`. C'est l'idiome Ruby.

## A retenir

- `.each` pour parcourir.
- `(0..n)` pour les ranges inclusives.
- `break` / `next` comme continue.
