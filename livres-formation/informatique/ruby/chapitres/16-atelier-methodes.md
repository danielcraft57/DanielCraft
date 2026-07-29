# Atelier : methodes

```ruby
def saluer(nom, heure)
  if heure < 12
    "Bonjour #{nom} !"
  elsif heure < 18
    "Bon apres-midi #{nom} !"
  else
    "Bonsoir #{nom} !"
  end
end

def moyenne(notes)
  return 0 if notes.empty?
  notes.sum.to_f / notes.size
end
```
