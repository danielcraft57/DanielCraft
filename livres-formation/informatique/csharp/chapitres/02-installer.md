# Installer C#

## Ce qu'il te faut

Pour coder en C# tu as besoin du SDK .NET (gratuit) et d'un editeur. On recommande Visual Studio Code avec l'extension C# Dev Kit, ou Visual Studio Community (gratuit, Windows/Mac).

## Installer le SDK .NET

1. Va sur dotnet.microsoft.com, telecharge le SDK .NET (derniere version LTS).
2. Lance l'installeur.
3. Ouvre un terminal et tape `dotnet --version`.
4. Si un numero de version s'affiche, c'est bon.

> **Astuce DanielCraft** - Le SDK inclut le compilateur et le runtime. Un seul telechargement suffit.

## Creer un premier projet

```bash
dotnet new console -n MonPremierProjet
cd MonPremierProjet
dotnet run
```

Tu verras "Hello, World!" dans le terminal.

## Installer VS Code

Telecharge VS Code sur code.visualstudio.com. Installe l'extension "C# Dev Kit" de Microsoft. Elle apporte IntelliSense, le debug et la gestion de projet.

## Petite histoire

Max installe .NET en 3 minutes. Il tape `dotnet new console` et son premier programme fonctionne immediatement. Pas de configuration complexe.

## A retenir

- Telecharge le SDK .NET sur dotnet.microsoft.com.
- Verifie avec `dotnet --version`.
- `dotnet new console` cree un projet pret a l'emploi.
- VS Code + C# Dev Kit = environnement leger et efficace.
