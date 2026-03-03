---
title: "CI/CD : tests, qualité et 'gates' (ce qui bloque un déploiement)"
date: 2026-02-04
excerpt: "Comment organiser lint, typecheck, tests unitaires et intégration pour sécuriser tes releases. Les quality gates qui empêchent de casser la prod."
type: article
tags: [CI/CD, tests, qualité, DevOps, automatisation]
series: ci-cd-serie
series_order: 2
og_image: ci-cd-tests-1200x630.jpg
---

# CI/CD : tests, qualité et 'gates' (ce qui bloque un déploiement)

Un pipeline CI/CD, c'est un filtre. Il doit bloquer ce qui est risqué, et laisser passer ce qui est propre.

Le problème, c'est qu'on a souvent deux extrêmes :

- trop strict -> tout le monde râle et contourne,
- pas assez -> ça casse en prod.

Ici on va construire un setup équilibré.

---

## Les trois couches de qualité

### 1) Qualité "statique"

Rapide et pas chère :

- lint (ESLint, Ruff, etc.)
- format (Prettier, Black)
- typecheck (TypeScript, mypy)

Objectif : attraper 60 % des problèmes en quelques secondes.

### 2) Tests unitaires

Ils valident :

- les règles métiers,
- les fonctions pures,
- les cas limites.

Objectif : un feedback rapide, fiable.

### 3) Tests d'intégration / end-to-end

Ils valident :

- API + base,
- migrations,
- workflows complets,
- éventuellement UI.

Objectif : éviter les surprises "ça marche chez moi".

---

## Un pipeline équilibré (ordre conseillé)

1. Lint + format + typecheck (fast)
2. Unit tests (fast)
3. Build (medium)
4. Integration tests (medium/slow)
5. Packaging (image Docker, artefact)
6. Déploiement staging
7. Smoke tests staging
8. Déploiement prod (manuel ou auto)

Cette structure évite de faire du "build Docker" si la base est déjà cassée.

---

## Gates : ce qui doit bloquer

### Bloquant (presque toujours)

- Lint en erreur
- Typecheck KO
- Tests unitaires KO
- Build KO

### Bloquant selon le projet

- Couverture de tests minimale (attention à ne pas tricher)
- SAST (analyse sécurité statique)
- Scan dépendances (ex: vuln critique)
- Lint sur IaC (Terraform, Kubernetes)

### Non bloquant mais visible

Certaines alertes peuvent être non bloquantes au début :

- vuln low/medium,
- warnings de perf,
- duplication de code.

L'idée : afficher, suivre, puis durcir progressivement.

---

## Stratégies de tests utiles

### Tests rapides en priorité

Le meilleur pipeline est celui qui te dit "non" en 30 secondes.

- lint + typecheck
- unit tests

### Intégration en parallèle

Si ta CI le permet :

- unit tests d'un côté,
- integration tests de l'autre.

### Flaky tests : le vrai poison

Un test flaky (parfois vert, parfois rouge) détruit la confiance.

Réflexes :

- isoler les dépendances réseau,
- utiliser des fixtures,
- figer l'heure (fake timers),
- stabiliser la base de test (containers, migrations).

---

## Exemple concret (Node/TS)

Dans `package.json` :

```json
{
  "scripts": {
    "lint": "eslint .",
    "typecheck": "tsc -p tsconfig.json --noEmit",
    "test": "vitest run",
    "test:integration": "vitest run -c vitest.integration.config.ts",
    "build": "tsc -p tsconfig.build.json"
  }
}
```

Ton pipeline appelle ces commandes, rien de plus magique.

---

## Ce qu'on fait ensuite

Dans l'article suivant, on passe à un sujet central : **builder des images Docker** proprement en CI (tags, cache, multi-stage).
