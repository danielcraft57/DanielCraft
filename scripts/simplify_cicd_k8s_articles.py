#!/usr/bin/env python3
"""Simplifie titres + corps CI/CD et Kubernetes, ajoute schemas SVG + figures."""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from add_series3_extra_schemas import (  # noqa: E402
    SCHEMAS,
    compare2,
    esc,
    flow_row,
    grid3,
    stack_layers,
    svg_wrap,
)

ROOT = Path(__file__).resolve().parent.parent
ARTICLES = ROOT / "blog" / "content" / "articles"


def write_svg(fname: str, title: str, desc: str, body: str) -> None:
    SCHEMAS.mkdir(parents=True, exist_ok=True)
    (SCHEMAS / fname).write_text(svg_wrap(title, desc, body), encoding="utf-8")


def fig(fname: str, alt: str, caption: str) -> str:
    return f'''<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/{fname}" alt="{esc(alt)}" class="schema-inline" width="640" />
  <figcaption>{esc(caption)}</figcaption>
</figure>'''


def patch_frontmatter(raw: str, title: str, excerpt: str) -> tuple[str, str]:
    end = raw.find("\n---", 3)
    fm, body = raw[: end + 4], raw[end + 4 :]
    fm = re.sub(r'^title:\s*".*?"', f'title: "{title}"', fm, count=1, flags=re.M)
    fm = re.sub(
        r'^excerpt:\s*".*?"',
        f'excerpt: "{excerpt.replace(chr(34), chr(92)+chr(34))}"',
        fm,
        count=1,
        flags=re.M,
    )
    return fm, body


# ---------- SVGs ----------
SVGS = [
    ("cicd-pipeline-simple.svg", "Pipeline CI/CD", "Du commit au deploiement",
     flow_row(["Commit", "Tests", "Build", "Controle", "Deploy"],
              "A chaque etape, une machine verifie a ta place")),
    ("cicd-quality-gates.svg", "Gates qualite", "Ce qui bloque un mauvais deploiement",
     flow_row(["Lint", "Tests", "Secu", "OK ?", "Prod"],
              "Si une porte est fermee, on ne livre pas")),
    ("cicd-secrets.svg", "Secrets CI/CD", "Mots de passe hors du code",
     compare2("A ne pas faire", ["Secret dans Git", "Dans un .env committe", "Dans les logs"],
              "Mieux", ["Coffre CI", "Variables masquees", "Rotation"],
              "Un secret dans Git, c'est un secret public")),
    ("cicd-docker-build.svg", "Build image CI", "Construire et pousser une image",
     flow_row(["Code", "Dockerfile", "Build", "Tag", "Registry"],
              "Meme image en test et en prod = moins de surprises")),
    ("cicd-github-actions.svg", "GitHub Actions", "Workflow simple",
     stack_layers([
         ("Declencheur", "push / pull request"),
         ("Jobs", "test, build, deploy"),
         ("Artefacts", "image, rapport"),
         ("Environnements", "staging puis prod"),
     ], "Un fichier YAML = la recette automatique")),
    ("cicd-gitlab-ci.svg", "GitLab CI", "Stages en chaine",
     flow_row(["build", "test", "package", "deploy"],
              "Des stages clairs valent mieux qu'un monstre de 200 lignes")),
    ("cicd-k8s-strategies.svg", "Strategies deploy", "Rolling, blue/green, canary",
     grid3([
         ("Rolling", "Remplace peu a peu"),
         ("Blue/Green", "Bascule d'un coup"),
         ("Canary", "Petit % d'abord"),
         ("Rollback", "Revenir vite"),
         ("Health", "Sondes vivantes"),
         ("Traffic", "Repartition"),
     ], "Choisis selon ton risque et ton trafic")),
    ("cicd-gitops.svg", "GitOps", "Git comme source de verite",
     flow_row(["Git", "CI build", "Manifest", "Argo/Flux", "Cluster"],
              "Le cluster suit Git, pas l'inverse")),
    ("cicd-versioning.svg", "Versions et rollback", "Semver, tags, revenir en arriere",
     flow_row(["Tag", "Release", "Deploy", "Probleme ?", "Rollback"],
              "Sans version claire, le retour arriere est la loterie")),
    ("cicd-observabilite.svg", "Apres le deploy", "Voir si ca va bien",
     grid3([
         ("Logs", "Ce qui s'est passe"),
         ("Mesures", "CPU, erreurs, latence"),
         ("Alertes", "Seuils utiles"),
         ("Dashboards", "Vue d'ensemble"),
         ("SLO", "Objectif simple"),
         ("On-call", "Qui reagit"),
     ], "Deployer sans regarder = conduire les yeux fermes")),
    ("k8s-pods-nodes.svg", "Pods et nodes", "Boites dans des machines",
     compare2("Node", ["Une machine", "CPU / RAM", "Fait tourner des pods"],
              "Pod", ["Plus petite unite", "1+ conteneurs", "Vit sur un node"],
              "Kubernetes place les pods sur les nodes pour toi")),
    ("k8s-architecture.svg", "Architecture cluster", "Qui decide, qui execute",
     stack_layers([
         ("Toi / CI", "Demandes (YAML)"),
         ("API server", "La porte d'entree"),
         ("etcd", "La memoire du cluster"),
         ("Scheduler", "Choisit le node"),
         ("Nodes + kubelet", "Executent les pods"),
     ], "Le plan de controle decide, les nodes executent")),
    ("k8s-deploy-service.svg", "Deployment et Service", "Copies + adresse stable",
     flow_row(["Image", "Deployment", "Pods", "Service", "Utilisateurs"],
              "Le Service garde une adresse meme si les pods changent")),
    ("k8s-config-secrets.svg", "ConfigMaps et Secrets", "Reglages hors image",
     compare2("ConfigMap", ["Reglages non secrets", "URL, flags", "Modifiable"],
              "Secret", ["Mots de passe / cles", "Acces limite", "Pas dans Git clair"],
              "Ne mets pas tes secrets dans l'image")),
    ("k8s-observabilite.svg", "Observabilite K8s", "Voir le cluster",
     flow_row(["Pods", "Logs", "Mesures", "Alertes", "Action"],
              "Sans logs et mesures, le cluster est une boite noire")),
    ("k8s-cicd.svg", "CI/CD vers K8s", "Du commit au cluster",
     flow_row(["Commit", "Build image", "Manifest", "Apply/GitOps", "Sondes"],
              "Meme chemin a chaque fois = moins de stress")),
]
for item in SVGS:
    write_svg(*item)


def article(slug: str, title: str, excerpt: str, body_md: str) -> None:
    path = ARTICLES / f"{slug}.md"
    raw = path.read_text(encoding="utf-8")
    fm, _ = patch_frontmatter(raw, title, excerpt)
    # keep series etc from fm; replace body entirely after H1 handled in body_md
    path.write_text(fm + "\n\n" + body_md.lstrip() + "\n", encoding="utf-8")
    print(f"[OK] {slug}")


# ===================== CI/CD =====================
article(
    "ci-cd-fondamentaux-pipelines",
    "CI/CD : du commit a la mise en ligne, automatiquement",
    "Une chaine qui teste et publie ton code a ta place — pour livrer plus souvent, sans trembler.",
    f"""# CI/CD : du commit a la mise en ligne, automatiquement

Imagine une **chaine de montage**. Tu poses une piece (ton code). Des machines verifient, emballent, puis envoient le produit. La **CI/CD**, c'est ca pour un site ou une appli.

Tu n'as plus besoin de "deployer a la main le vendredi soir en croisant les doigts".

{fig("cicd-pipeline-simple.svg", "Schema d'un pipeline CI/CD simple", "Commit, tests, build, controle, deploiement : une recette repetable.")}

## CI et CD, en mots simples

La **CI** (integration continue) : a chaque changement, on verifie automatiquement que ca tient debout (tests, qualite, compilation).

La **CD** :
- **Delivery** : on prepare un paquet pret a installer (souvent une [image Docker](/blog/articles/docker-fondamentaux-images-conteneurs.html)).
- **Deployment** : on l'installe vraiment (parfois apres un clic "OK").

Beaucoup disent "CD" pour les deux. L'important : **automatiser** ce qui se repete.

## Pourquoi tu en as besoin (meme tout petit)

Sans CI/CD, tu as souvent :
- "Ca marche sur mon PC" mais pas ailleurs
- un oubli de fichier a la mise en ligne
- la peur de toucher a la prod

Avec une petite chaine, tu gagnes : **meme recettes**, **preuves** (tests verts), et un historique clair.

## Les etapes typiques

1. Declenchement (push, merge)
2. Installation des dependances
3. **Tests** et controles
4. **Build** (image, bundle)
5. Publication de l'artefact
6. Deploiement (staging puis prod)

Garde ca **simple** au debut. Une usine a gaz de 40 jobs pour 2 devs, ca fatigue tout le monde.

## Ce qu'il faut retenir

La CI/CD n'est pas un badge DevOps. C'est une **habitude** : chaque changement passe par le meme chemin. Dans la suite : tests qui bloquent, secrets bien ranges, Docker en CI, GitHub/GitLab, strategies de deploiement, et comment voir si ca s'est bien passe.
""",
)

article(
    "ci-cd-tests-qualite-gates",
    "CI/CD : les portes qui bloquent un mauvais deploiement",
    "Tests, qualite et controles automatiques : ce qui doit etre vert avant d'aller en prod.",
    f"""# CI/CD : les portes qui bloquent un mauvais deploiement

Une chaine CI/CD sans **portes** (gates), c'est un tapis roulant qui envoie n'importe quoi en prod. Les portes disent : "si ce n'est pas OK, on s'arrete".

{fig("cicd-quality-gates.svg", "Schema des portes qualite CI/CD", "Lint, tests, secu : si une porte est fermee, on ne livre pas.")}

## Quoi bloquer (le minimum utile)

- **Style / lint** : code trop sale ou dangereux
- **Tests unitaires** : les petites regles metier
- **Tests d'integration** : les pieces qui doivent s'assembler
- Controles **securite** basiques (dependances connues, secrets detectes)

Tu n'as pas besoin de tout le catalogue. Tu as besoin de portes qui **veulent dire quelque chose**.

## Trop de portes = personne ne les ecoute

Si tout est "bloquant", l'equipe contourne. Mieux vaut :
- **bloquer** le critique (tests metier, build casse, secret detecte)
- **avertir** le reste (couverture un peu basse, lint mineur)

## Une regle simple

Avant la prod : "est-ce qu'on oserait deployer ca un vendredi a 17h ?" Si non, la porte doit etre rouge. Ensuite, regarde l'article sur les [secrets](/blog/articles/ci-cd-secrets-variables-environnement.html) et le [build Docker](/blog/articles/ci-cd-build-images-docker.html).
""",
)

article(
    "ci-cd-secrets-variables-environnement",
    "CI/CD : cacher les mots de passe (sans les coller dans Git)",
    "Ou mettre cles API et mots de passe pour que la chaine fonctionne sans fuite.",
    f"""# CI/CD : cacher les mots de passe (sans les coller dans Git)

Un **secret**, c'est un truc qu'on ne montre pas : mot de passe, cle API, certificat. Si tu le mets dans Git, considere-le **public**.

{fig("cicd-secrets.svg", "Schema bons et mauvais usages des secrets", "Coffre CI et variables masquees : jamais de secret dans le code.")}

## Les mauvais reflexes

- Fichier `.env` committe "juste pour tester"
- Secret dans un script
- Secret imprime dans les **logs** de la CI

## Les bons reflexes

- Coffre de la CI (GitHub Secrets, variables GitLab masquees…)
- Droits **limites** : chaque job n'a que ce dont il a besoin
- **Rotation** : changer une cle compromise rapidement
- Pas de secret dans l'[image Docker](/blog/articles/docker-production-registry-securite.html)

## Variables vs secrets

Les variables (URL d'API, mode debug) peuvent etre visibles. Les secrets, non. Separe-les clairement. C'est aussi vrai sur [Kubernetes](/blog/articles/kubernetes-configmaps-secrets.html).
""",
)

article(
    "ci-cd-build-images-docker",
    "CI/CD : fabriquer et envoyer une image Docker",
    "Construire la meme boite a chaque fois, la taguer, la pousser dans un registry.",
    f"""# CI/CD : fabriquer et envoyer une image Docker

La CI fabrique souvent une **image** : une boite prete a demarrer partout pareil. Ensuite elle l'envoie dans un **registry** (etagere d'images).

{fig("cicd-docker-build.svg", "Schema build et push d'image Docker en CI", "Code, Dockerfile, build, tag, registry.")}

## Les idees cles

- **Tag** clair : `1.4.2` ou le hash du commit — pas seulement `latest`
- **Cache** de build pour aller plus vite
- Image **legere** (voir [optimisation Docker](/blog/articles/docker-build-optimisation-images.html))
- Scan simple des failles avant prod

## Pourquoi c'est bien

Tu testes **la meme boite** que tu mets en prod. Moins de "mais ca marchait en local". Enchaine avec [GitHub Actions](/blog/articles/ci-cd-github-actions-workflow-complet.html) ou [GitLab CI](/blog/articles/ci-cd-gitlab-ci-pipeline-complet.html).
""",
)

article(
    "ci-cd-github-actions-workflow-complet",
    "GitHub Actions : une recette automatique pour ton projet",
    "Un workflow simple : tester, construire, deployer — explique sans jargon.",
    f"""# GitHub Actions : une recette automatique pour ton projet

**GitHub Actions**, c'est le robot de GitHub. Tu ecris une recette (YAML). A chaque push, il execute.

{fig("cicd-github-actions.svg", "Schema d'un workflow GitHub Actions", "Declencheur, jobs, artefacts, environnements.")}

## En pratique

1. Un evenement (push sur `main`, pull request)
2. Des **jobs** : test, build, deploy
3. Des secrets ranges dans les reglages du repo
4. Souvent : staging d'abord, prod ensuite

Garde un workflow **lisible**. Si personne ne comprend le fichier, personne ne l'entretient. Pour une alternative, vois [GitLab CI](/blog/articles/ci-cd-gitlab-ci-pipeline-complet.html).
""",
)

article(
    "ci-cd-gitlab-ci-pipeline-complet",
    "GitLab CI : des etapes claires jusqu'au deploiement",
    "Stages, cache et deploiement : une pipeline GitLab simple a suivre.",
    f"""# GitLab CI : des etapes claires jusqu'au deploiement

Avec **GitLab CI**, tu decris des **stages** (etapes) : build, test, package, deploy. Chaque job appartient a une etape.

{fig("cicd-gitlab-ci.svg", "Schema des stages GitLab CI", "build, test, package, deploy : une chaine lisible.")}

## Conseils simples

- Nomme les jobs pour un humain
- Mets du **cache** sur les dependances (sans casser les builds)
- Separe staging et prod
- Range les [secrets](/blog/articles/ci-cd-secrets-variables-environnement.html) correctement

Le but : la meme histoire a chaque merge. Ensuite, tu peux viser [Kubernetes](/blog/articles/ci-cd-kubernetes-deploiement-strategies.html) ou le [GitOps](/blog/articles/ci-cd-gitops-argo-flux.html).
""",
)

article(
    "ci-cd-kubernetes-deploiement-strategies",
    "CI/CD sur Kubernetes : changer de version sans tout casser",
    "Rolling, blue/green, canary : comment remplacer une version en douceur.",
    f"""# CI/CD sur Kubernetes : changer de version sans tout casser

Sur [Kubernetes](/blog/articles/kubernetes-concepts-pods-nodes.html), tu ne "copies" pas un fichier sur un serveur. Tu remplaces des **pods** (petites boites) pendant que le service continue.

{fig("cicd-k8s-strategies.svg", "Schema strategies de deploiement Kubernetes", "Rolling, blue/green, canary et rollback.")}

## Trois strategies en francais

- **Rolling** : on remplace peu a peu. Simple et courant.
- **Blue/Green** : deux versions cote a cote, on bascule le trafic d'un coup.
- **Canary** : on envoie un petit pourcentage d'utilisateurs sur la nouveaute.

Toujours prevoir un **rollback** (revenir en arriere) et des **sondes** (est-ce que l'app repond ?). Voir aussi [Deployments et Services](/blog/articles/kubernetes-deployments-services.html).
""",
)

article(
    "ci-cd-gitops-argo-flux",
    "GitOps : le cluster suit Git (pas l'inverse)",
    "Argo CD ou Flux : deployer en declarant l'etat souhaite dans un depot Git.",
    f"""# GitOps : le cluster suit Git (pas l'inverse)

Le **GitOps**, c'est une idee simple : Git decrit **ce qui doit tourner**. Un outil (Argo CD, Flux) regarde Git et aligne le cluster.

{fig("cicd-gitops.svg", "Schema GitOps avec Argo ou Flux", "Git, build, manifest, synchronisation cluster.")}

## Pourquoi c'est rassurant

- Historique clair (qui a change quoi)
- Moins de `kubectl` a la main a 23h
- Un ecart ? On le voit

Ca demande de la discipline : les manifests (fichiers de description) doivent etre **propres** et versionnes. Branche avec la [CI/CD Kubernetes](/blog/articles/ci-cd-kubernetes-deploiement-strategies.html).
""",
)

article(
    "ci-cd-versioning-releases-rollbacks",
    "Versions et retours arriere : livrer sans paniquer",
    "Tags, releases et rollback : savoir exactement ce qui tourne, et revenir vite.",
    f"""# Versions et retours arriere : livrer sans paniquer

Sans **version** claire, "revenir en arriere" devient un jeu de piste. Avec un tag et une release, tu sais **quoi** est en prod.

{fig("cicd-versioning.svg", "Schema versioning release rollback", "Tag, release, deploy, probleme, rollback.")}

## Habitudes utiles

- Versions lisibles (ex. `1.4.2`) ou commit hash
- Une **release** = notes + artefact
- Rollback teste (pas seulement imagine)
- Ne jamais ecraser un tag deja livre

C'est le filet de securite de toute la [serie CI/CD](/blog/series/ci-cd-serie.html).
""",
)

article(
    "ci-cd-observabilite-deploiements",
    "Apres le deploiement : voir si ca va vraiment bien",
    "Logs, mesures et alertes utiles pour savoir si la nouvelle version tient la route.",
    f"""# Apres le deploiement : voir si ca va vraiment bien

Deployer sans regarder, c'est comme livrer un colis sans confirmer qu'il est arrive. L'**observabilite**, c'est voir ce qui se passe.

{fig("cicd-observabilite.svg", "Schema observabilite apres deploiement", "Logs, mesures, alertes, dashboards.")}

## Le trio de base

- **Logs** : l'histoire ecrite
- **Mesures** : erreurs, latence, CPU
- **Alertes** : seulement ce qui merite un reveil

Apres chaque deploiement : une checklist de 5 minutes. Sur Kubernetes, vois aussi [l'observabilite cluster](/blog/articles/kubernetes-observabilite-logs-metrics.html).
""",
)

# ===================== Kubernetes =====================
article(
    "kubernetes-concepts-pods-nodes",
    "Kubernetes : des boites (pods) sur des machines (nodes)",
    "Le vocabulaire de base pour comprendre un cluster sans se noyer.",
    f"""# Kubernetes : des boites (pods) sur des machines (nodes)

[Docker](/blog/articles/docker-fondamentaux-images-conteneurs.html) fait tourner une boite sur **une** machine. **Kubernetes** gere plein de boites sur **plein** de machines.

{fig("k8s-pods-nodes.svg", "Schema pods et nodes Kubernetes", "Node = machine. Pod = plus petite unite qui tourne dessus.")}

## Les mots a connaitre

- **Cluster** : l'ensemble (cerveau + machines)
- **Node** : une machine du cluster
- **Pod** : la plus petite unite (souvent 1 conteneur)
- **Namespace** : un tiroir pour ranger (prod, staging…)

Tu demandes un etat ("je veux 3 copies de mon site"). Kubernetes se debrouille pour y arriver. Ensuite : [architecture](/blog/articles/kubernetes-architecture-cluster.html) et [Deployments](/blog/articles/kubernetes-deployments-services.html).
""",
)

article(
    "kubernetes-architecture-cluster",
    "Kubernetes : qui decide, qui execute",
    "Le plan de controle et les nodes : le cerveau et les bras du cluster.",
    f"""# Kubernetes : qui decide, qui execute

Un cluster a un **cerveau** (plan de controle) et des **bras** (nodes).

{fig("k8s-architecture.svg", "Schema architecture cluster Kubernetes", "API, etcd, scheduler, puis nodes qui executent.")}

## En image mentale

1. Tu parles a l'**API** (la reception)
2. **etcd** se souvient de l'etat voulu
3. Le **scheduler** choisit sur quelle machine placer un pod
4. Les **nodes** executent

Tu n'as pas besoin de tout reconstruire a la main pour comprendre. Garde cette carte mentale, puis passe aux [Deployments et Services](/blog/articles/kubernetes-deployments-services.html).
""",
)

article(
    "kubernetes-deployments-services",
    "Kubernetes : copies de ton app + adresse stable",
    "Deployment pour gerer les pods, Service pour les joindre facilement.",
    f"""# Kubernetes : copies de ton app + adresse stable

Un **Deployment** dit : "garde N copies de mon appli a jour". Un **Service** donne une **adresse stable**, meme si les pods changent.

{fig("k8s-deploy-service.svg", "Schema Deployment et Service", "Image, Deployment, pods, Service, utilisateurs.")}

## Pourquoi c'est pratique

- Une copie tombe ? Kubernetes en relance une
- Tu mets a jour ? Rolling update
- Les utilisateurs passent par le Service, pas par l'IP d'un pod

Ensuite : [config et secrets](/blog/articles/kubernetes-configmaps-secrets.html), puis [CI/CD](/blog/articles/kubernetes-ci-cd-deploiement-continu.html).
""",
)

article(
    "kubernetes-configmaps-secrets",
    "Kubernetes : reglages et secrets hors de l'image",
    "ConfigMaps pour la config visible, Secrets pour ce qui doit rester cache.",
    f"""# Kubernetes : reglages et secrets hors de l'image

Ne colle pas tes mots de passe dans l'**image**. Mets la config a part.

{fig("k8s-config-secrets.svg", "Schema ConfigMaps et Secrets", "Config non secrete vs secrets proteges.")}

## Deux tiroirs

- **ConfigMap** : reglages (URL, options)
- **Secret** : cles, mots de passe (acces limite)

Meme regle qu'en [CI/CD](/blog/articles/ci-cd-secrets-variables-environnement.html) : ce qui est dans Git en clair n'est plus secret.
""",
)

article(
    "kubernetes-observabilite-logs-metrics",
    "Kubernetes : voir ce qui se passe dans le cluster",
    "Logs, mesures et alertes pour ne pas piloter a l'aveugle.",
    f"""# Kubernetes : voir ce qui se passe dans le cluster

Un cluster sans **observabilite**, c'est un immeuble sans fenetres. Tu entends du bruit, tu ne vois rien.

{fig("k8s-observabilite.svg", "Schema observabilite Kubernetes", "Pods, logs, mesures, alertes, action.")}

## Le minimum

- Logs des pods
- Mesures (CPU, memoire, erreurs)
- Alertes rares mais utiles
- Une idee de "normal" vs "casse"

Ca complete l'[observabilite des deploiements](/blog/articles/ci-cd-observabilite-deploiements.html).
""",
)

article(
    "kubernetes-ci-cd-deploiement-continu",
    "Kubernetes et CI/CD : publier sans stress",
    "Du commit a l'image, puis au cluster, avec les memes etapes a chaque fois.",
    f"""# Kubernetes et CI/CD : publier sans stress

La bonne chaine : **commit → tests → image → description (YAML) → cluster**. Toujours pareil.

{fig("k8s-cicd.svg", "Schema CI/CD vers Kubernetes", "Commit, build image, manifest, apply ou GitOps, sondes.")}

## Deux styles

- La CI applique les manifests
- Ou le [GitOps](/blog/articles/ci-cd-gitops-argo-flux.html) synchronise depuis Git

Ajoute des sondes et un plan de [rollback](/blog/articles/ci-cd-versioning-releases-rollbacks.html). C'est ca, un deploiement "propre".
""",
)

# collections
for path, title, desc in [
    (
        ROOT / "blog/content/collections/ci-cd-serie.json",
        "Série CI/CD : livrer du code sans trembler",
        "Pipelines, tests, secrets, Docker, GitHub/GitLab, Kubernetes et observabilite — expliques simplement.",
    ),
    (
        ROOT / "blog/content/collections/kubernetes-serie.json",
        "Série Kubernetes : orchestrer des boites sans panique",
        "Pods, nodes, deployments, secrets et observabilite — le cluster explique avec des mots du quotidien.",
    ),
]:
    import json
    data = json.loads(path.read_text(encoding="utf-8"))
    data["title"] = title
    data["description"] = desc
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"[OK] collection {path.name}")

print("done")
