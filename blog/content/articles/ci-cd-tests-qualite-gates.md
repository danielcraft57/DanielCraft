---
title: "CI/CD : les portes qui bloquent un mauvais deploiement"
date: 2025-03-06
excerpt: "Tests, qualite et controles automatiques : ce qui doit etre vert avant d'aller en prod."
type: article
tags: [CI/CD, tests, qualité, DevOps, automatisation]
series: ci-cd-serie
series_order: 2
og_image: ci-cd-tests-1200x630.jpg
---

# CI/CD : les portes qui bloquent un mauvais deploiement

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/cicd-quality-gates.svg" alt="Schema des portes qualite CI/CD" class="schema-inline" width="640" />
  <figcaption>Lint, tests, secu : si une porte est fermee, on ne livre pas.</figcaption>
</figure>

Un pipeline CI/CD, c’est un filtre. Il doit bloquer ce qui est risqué, et laisser passer ce qui est propre. Le problème, c’est qu’on bascule souvent entre deux extrêmes : trop strict (tout le monde râle et contourne) ou pas assez (ça casse en prod).

Ici, on construit un setup équilibré, accessible même si tu débutes. Pour le cadre général des pipelines, tu peux lire d’abord les [fondamentaux CI/CD](/blog/articles/ci-cd-fondamentaux-pipelines.html).

---

## Les trois couches de qualité

### 1) Qualité « statique »

Rapide et peu coûteuse :

- lint (ESLint, Ruff, etc.),
- format (Prettier, Black),
- typecheck (TypeScript, mypy).

Objectif : attraper une grosse partie des problèmes en quelques secondes — oubli d’import, typo de type, style incohérent.

### 2) Tests unitaires

Ils valident :

- les règles métiers,
- les fonctions pures,
- les cas limites (liste vide, montant négatif, timezone bizarre).

Objectif : un feedback rapide et fiable, sans dépendre d’un serveur distant.

### 3) Tests d’intégration / end-to-end

Ils valident :

- API + base,
- migrations,
- workflows complets,
- éventuellement l’UI.

Objectif : éviter le classique « ça marche chez moi ».

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

Cette structure évite de lancer un [build Docker](/blog/articles/ci-cd-build-images-docker.html) si le lint est déjà rouge. Tu paies le coût lourd seulement quand les bases sont saines.

---

## Gates : ce qui doit bloquer

### Bloquant (presque toujours)

- Lint en erreur
- Typecheck KO
- Tests unitaires KO
- Build KO

### Bloquant selon le projet

- Couverture de tests minimale (attention à ne pas « tricher » avec des tests vides)
- SAST (analyse sécurité statique)
- Scan de dépendances (vuln critique)
- Lint IaC (Terraform, manifests Kubernetes)

### Non bloquant mais visible

Au début, certaines alertes peuvent rester informatives :

- vulnérabilités low/medium,
- warnings de perf,
- duplication de code.

L’idée : afficher, suivre, puis durcir progressivement. Une porte trop sévère jour 1 devient une porte contournée jour 15.

---

## Stratégies de tests utiles

### Tests rapides en priorité

Le meilleur pipeline est celui qui te dit « non » en 30 secondes :

- lint + typecheck,
- unit tests sur le diff ou le cœur métier.

### Intégration en parallèle

Si ta CI le permet (ex. [GitHub Actions](/blog/articles/ci-cd-github-actions-workflow-complet.html) ou [GitLab CI](/blog/articles/ci-cd-gitlab-ci-pipeline-complet.html)) :

- unit tests d’un côté,
- integration tests de l’autre.

### Flaky tests : le vrai poison

Un test flaky (parfois vert, parfois rouge) détruit la confiance. L’équipe finit par relancer le job « jusqu’à ce que ça passe » — et là, ta porte qualité n’existe plus.

Réflexes :

- isoler les dépendances réseau (mocks, stubs),
- utiliser des fixtures stables,
- figer l’heure (fake timers),
- stabiliser la base de test (containers, migrations reproductibles).

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

Ton pipeline appelle ces commandes, dans cet ordre. Rien de magique : la CI exécute ce que tu as déjà validé en local.

### Mini-checklist avant de fusionner

- [ ] `lint` et `typecheck` verts en local
- [ ] unit tests verts
- [ ] pas de `skip` / `xit` oublié sur un test critique
- [ ] smoke staging prévu après déploiement
- [ ] si breaking change : note dans le changelog / SemVer (voir [versioning et rollbacks](/blog/articles/ci-cd-versioning-releases-rollbacks.html))

---

## Pièges fréquents

- Faire des gates bloquantes sur tout dès le jour 1 → contournements (`--no-verify`, jobs skippés).
- Couverture à 90 % exigée… avec des tests qui ne testent rien.
- Intégration E2E trop lente sur chaque commit (réserve-les à `main` ou au nightly).
- Ignorer les flaky tests « parce que ça finit par passer ».
- Déployer en prod alors que seul le lint a tourné (les autres jobs sont `continue-on-error`).

---

## Comment durcir sans frustrer

1. Commence bloquant sur lint + unit.
2. Ajoute le typecheck bloquant.
3. Mets le scan sécu en warning, puis bloque sur les critiques.
4. Ajoute smoke staging avant toute promo prod.

Tu obtiens un filet qui grandit avec la maturité de l’équipe — pas un mur qui tombe le premier sprint.

---

## En résumé

- Trois couches : statique, unitaire, intégration/E2E.
- Ordonne le pipeline du plus rapide au plus lent.
- Bloque le vraiment dangereux ; affiche le reste avant de durcir.
- Traite les flaky tests comme des bugs de confiance.

Ensuite dans la série : [builder des images Docker](/blog/articles/ci-cd-build-images-docker.html) proprement en CI (tags, cache, multi-stage).
