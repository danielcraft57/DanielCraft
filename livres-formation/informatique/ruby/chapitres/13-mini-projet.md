# Mini-projet : gestionnaire de taches CLI

```ruby
taches = []

loop do
  puts "\n1. Ajouter  2. Lister  3. Supprimer  4. Quitter"
  choix = gets.chomp

  case choix
  when "1"
    print "Tache : "
    tache = gets.chomp
    taches << tache unless tache.empty?
    puts "Ajoutee."
  when "2"
    if taches.empty?
      puts "Aucune tache."
    else
      taches.each_with_index { |t, i| puts "  #{i + 1}. #{t}" }
    end
  when "3"
    print "Numero : "
    idx = gets.to_i - 1
    taches.delete_at(idx) if idx >= 0 && idx < taches.size
  when "4"
    puts "A bientot !"
    break
  end
end
```

## A retenir

- Array + case + gets = CLI complet.
- `loop do` / `break` pour le menu.
