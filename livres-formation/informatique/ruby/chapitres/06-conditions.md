# Les conditions

```ruby
if age >= 18
  puts "Majeur"
elsif age >= 12
  puts "Adolescent"
else
  puts "Enfant"
end
```

## Modificateur if

```ruby
puts "Majeur" if age >= 18
```

## case (switch)

```ruby
case jour
when "lundi", "mardi"
  puts "Debut de semaine"
when "vendredi"
  puts "Weekend proche"
else
  puts "Autre"
end
```

## A retenir

- `if` / `elsif` / `else` / `end`.
- `case` / `when` / `else` / `end`.
- Modificateurs postfixe possibles.
