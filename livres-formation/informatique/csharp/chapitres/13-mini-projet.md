# Mini-projet : gestionnaire de taches

## L'objectif

On cree un programme console qui permet d'ajouter, lister, marquer comme fait et supprimer des taches. Ce projet combine classes, listes, methodes, boucles, conditions et fichiers.

## Structure

```csharp
using System.Text.Json;

var taches = Charger();
bool quitter = false;

while (!quitter)
{
    Console.WriteLine("\n1. Ajouter  2. Lister  3. Terminer  4. Supprimer  5. Quitter");
    switch (Console.ReadLine())
    {
        case "1": Ajouter(); break;
        case "2": Lister(); break;
        case "3": Terminer(); break;
        case "4": Supprimer(); break;
        case "5": quitter = true; break;
    }
}

void Ajouter()
{
    Console.Write("Tache : ");
    string titre = Console.ReadLine() ?? "";
    taches.Add(new Tache(titre));
    Sauvegarder();
    Console.WriteLine("Ajoutee.");
}

void Lister()
{
    if (taches.Count == 0) { Console.WriteLine("Aucune tache."); return; }
    for (int i = 0; i < taches.Count; i++)
    {
        var t = taches[i];
        string statut = t.Fait ? "[x]" : "[ ]";
        Console.WriteLine($"  {i + 1}. {statut} {t.Titre}");
    }
}

void Terminer()
{
    Console.Write("Numero : ");
    if (int.TryParse(Console.ReadLine(), out int n) && n > 0 && n <= taches.Count)
    {
        taches[n - 1].Fait = true;
        Sauvegarder();
    }
}

void Supprimer()
{
    Console.Write("Numero : ");
    if (int.TryParse(Console.ReadLine(), out int n) && n > 0 && n <= taches.Count)
    {
        taches.RemoveAt(n - 1);
        Sauvegarder();
    }
}

List<Tache> Charger()
{
    if (!File.Exists("taches.json")) return new();
    string json = File.ReadAllText("taches.json");
    return JsonSerializer.Deserialize<List<Tache>>(json) ?? new();
}

void Sauvegarder()
{
    string json = JsonSerializer.Serialize(taches, new JsonSerializerOptions { WriteIndented = true });
    File.WriteAllText("taches.json", json);
}

class Tache
{
    public string Titre { get; set; } = "";
    public bool Fait { get; set; }
    public Tache() { }
    public Tache(string titre) => Titre = titre;
}
```

## Ce que tu apprends

- `System.Text.Json` pour la persistance.
- Top-level statements avec methodes locales.
- `List<T>` et manipulation d'index.
- Boucle principale avec menu.

> **Astuce DanielCraft** - Commence par le squelette (menu + methodes vides), puis remplis une a une.

## A retenir

- Un projet = assemblage de notions.
- Decouper en methodes rend le code lisible.
- JSON pour sauvegarder des donnees structurees.
