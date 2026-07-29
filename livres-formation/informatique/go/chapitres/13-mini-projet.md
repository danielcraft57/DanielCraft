# Mini-projet : outil CLI de notes

## L'objectif

On cree un outil en ligne de commande qui permet d'ajouter, lister et chercher des notes. Le tout sauvegarde dans un fichier JSON.

## Structure

```go
package main

import (
    "encoding/json"
    "fmt"
    "os"
    "strings"
)

type Note struct {
    Titre   string `json:"titre"`
    Contenu string `json:"contenu"`
}

const fichier = "notes.json"

func charger() []Note {
    data, err := os.ReadFile(fichier)
    if err != nil {
        return []Note{}
    }
    var notes []Note
    json.Unmarshal(data, &notes)
    return notes
}

func sauvegarder(notes []Note) {
    data, _ := json.MarshalIndent(notes, "", "  ")
    os.WriteFile(fichier, data, 0644)
}

func main() {
    notes := charger()
    for {
        fmt.Println("\n1. Ajouter  2. Lister  3. Chercher  4. Quitter")
        var choix string
        fmt.Scanln(&choix)
        switch choix {
        case "1":
            var titre, contenu string
            fmt.Print("Titre : ")
            fmt.Scanln(&titre)
            fmt.Print("Contenu : ")
            fmt.Scanln(&contenu)
            notes = append(notes, Note{Titre: titre, Contenu: contenu})
            sauvegarder(notes)
            fmt.Println("Ajoutee.")
        case "2":
            for i, n := range notes {
                fmt.Printf("  %d. %s - %s\n", i+1, n.Titre, n.Contenu)
            }
        case "3":
            fmt.Print("Recherche : ")
            var terme string
            fmt.Scanln(&terme)
            for _, n := range notes {
                if strings.Contains(
                    strings.ToLower(n.Titre),
                    strings.ToLower(terme),
                ) {
                    fmt.Printf("  %s - %s\n", n.Titre, n.Contenu)
                }
            }
        case "4":
            fmt.Println("A bientot !")
            return
        }
    }
}
```

## Ce que tu apprends

- `encoding/json` pour la serialisation.
- Struct avec tags JSON.
- Boucle principale avec switch.
- Lecture/ecriture de fichiers.

> **Astuce DanielCraft** - Commence par le menu, puis ajoute une fonction a la fois.

## A retenir

- Un projet = assemblage de notions.
- JSON + structs = persistance simple.
- `os.ReadFile` / `os.WriteFile` pour les fichiers.
