#!/usr/bin/env python3
"""Simplifie title + H1 des articles series3 / docker / aws."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES = ROOT / "blog" / "content" / "articles"

# slug -> (title, excerpt optionnel ou None pour ne pas toucher)
TITLES: dict[str, tuple[str, str | None]] = {
    # Cyber
    "cybersecurite-fondamentaux-menaces-risques": (
        "Cybersécurité : ce qui peut te faire mal (et comment te protéger)",
        "Comme pour une maison : menaces, faiblesses, risques, et les gestes simples pour se protéger sans paniquer.",
    ),
    "secops-soc-fonctions-process": (
        "SecOps et SOC : qui surveille quoi (expliqué simplement)",
        "Qui regarde les alertes, comment on trie, et comment on s'améliore après un raté — sans jargon inutile.",
    ),
    "siem-log-management-detection": (
        "SIEM : lire les traces de ton système sans te noyer",
        "Les journaux d'activité, comment les rassembler, et repérer le vrai signal sans mille fausses alertes.",
    ),
    "edr-xdr-endpoint-detection-response": (
        "EDR et XDR : protéger les ordinateurs et réagir vite",
        "Des outils qui surveillent PCs et serveurs, isolent en cas de souci, et aident à répondre sans panique.",
    ),
    "gestion-vulnerabilites-cve-patching": (
        "Les failles à réparer : trouver, trier, corriger",
        "Comment prioriser les trous de sécurité et les corriger sans tout patcher dans le désordre.",
    ),
    "iam-mfa-principes-zero-trust": (
        "Accès, double verrou et confiance zéro (expliqués simplement)",
        "Qui a le droit d'ouvrir quoi, pourquoi le double verrou compte, et l'idée de ne jamais faire confiance par défaut.",
    ),
    "incident-response-runbook-postmortem": (
        "Quand ça casse : quoi faire, puis quoi apprendre",
        "Une fiche simple pour réagir sous stress, puis un débrief pour ne pas refaire la même erreur.",
    ),
    "securite-cloud-cspm-cwpp": (
        "Sécurité cloud : les mauvais réglages qui coûtent cher",
        "Le cloud n'est pas magique : erreurs de config, partage des responsabilités, et outils pour vérifier.",
    ),
    "devsecops-sast-dast-sbom": (
        "Sécurité dans le code : contrôler avant de publier",
        "Vérifier le code, les dépendances et les images avant la mise en ligne — sans freiner toute l'équipe.",
    ),
    "conformite-rgpd-nis2-iso27001": (
        "RGPD, NIS2, ISO : se mettre en règle sans paniquer",
        "Ce que ces cadres demandent vraiment : des contrôles, des preuves, et du bon sens — pas un classeur poussiéreux.",
    ),
    # API
    "api-rest-graphql-fondamentaux-comparaison": (
        "API : deux façons de faire parler un site et un serveur",
        "REST et GraphQL, c'est quoi ? Deux styles pour demander des infos à un serveur — on pose le décor.",
    ),
    "api-rest-bonnes-pratiques-conception": (
        "REST : bien organiser ses portes et ses règles",
        "Ressources, verbes HTTP, pagination, sécurité : les bases pour une API claire et durable.",
    ),
    "graphql-fondamentaux-schema-queries": (
        "GraphQL : demander exactement ce qu'il te faut",
        "Un schéma, des questions précises, et ce qui change vraiment pour l'équipe derrière.",
    ),
    "api-rest-graphql-performances-benchmarks": (
        "REST ou GraphQL : lequel va plus vite (et pour qui)",
        "Écran simple, dashboard chargé, mobile, cache : où chacun gagne vraiment.",
    ),
    "choisir-rest-graphql-quand-et-comment": (
        "REST ou GraphQL : comment choisir (ou combiner)",
        "Une grille simple selon ton contexte — et comment mixer les deux sans se perdre.",
    ),
    # UX
    "ux-ui-fondamentaux-differences": (
        "UX et UI : la sensation contre le look",
        "L'expérience vécue vs l'interface visible — et comment les faire marcher ensemble.",
    ),
    "ergonomie-heuristiques-nielsen": (
        "Ergonomie : 10 règles simples pour moins frustrer",
        "Les heuristiques de Nielsen en français clair, avec des exemples du quotidien.",
    ),
    "wireframes-prototypage-fidelite": (
        "Maquettes : du croquis au prototype",
        "Low-fi, mid-fi, high-fi : choisir le bon niveau de détail selon la question à tester.",
    ),
    "ux-recherche-utilisateur-interviews-tests": (
        "Écouter les utilisateurs : interviews et tests",
        "Poser les bonnes questions, tester tôt, et transformer un insight en décision produit.",
    ),
    "parcours-utilisateur-mapping-jtbd": (
        "Le chemin de l'utilisateur : étapes et freins",
        "User flows, journey map et JTBD — pour voir où ça coince vraiment.",
    ),
    "design-system-composants-tokens": (
        "Design system : les briques pour rester cohérent",
        "Composants, tokens et adoption : une bibliothèque vivante, pas un dossier fantôme.",
    ),
    "accessibilite-wcag-checklist": (
        "Accessibilité : pour que tout le monde puisse utiliser",
        "Une checklist WCAG utile : contraste, clavier, labels — et des tests qui comptent.",
    ),
    "ui-typographie-couleurs-grille": (
        "Textes, couleurs et alignement : rendre clair",
        "Hiérarchie visuelle simple : ce que l'œil comprend en deux secondes.",
    ),
    "micro-interactions-feedback-etats": (
        "Petits signaux : dire à l'utilisateur ce qui se passe",
        "Hover, chargement, erreur, succès : le timing du feedback crée la confiance.",
    ),
    "mesurer-ux-kpis-analytics-ab-testing": (
        "Mesurer l'expérience : chiffres utiles (pas de vanité)",
        "KPIs, analytics et A/B testing : une boucle pour apprendre, pas pour se mentir.",
    ),
    # Docker
    "docker-fondamentaux-images-conteneurs": (
        "Docker : la recette et le gâteau (image vs conteneur)",
        "Image = plan figé. Conteneur = instance qui tourne. Les bases sans jargon.",
    ),
    "docker-installation-bonnes-pratiques": (
        "Docker : bien l'installer et le garder propre",
        "Installation, droits, contextes et nettoyage : l'hygiène locale qui évite les surprises.",
    ),
    "docker-volumes-reseaux": (
        "Docker : garder ses fichiers et connecter les boîtes",
        "Volumes pour persister, réseaux pour faire parler les services — sans magie noire.",
    ),
    "docker-compose-environnements-local": (
        "Docker Compose : plusieurs boîtes qui travaillent ensemble",
        "Un fichier pour lancer site, base et cache comme une petite équipe locale.",
    ),
    "docker-build-optimisation-images": (
        "Docker : des images plus légères et plus rapides",
        "Ordre du Dockerfile, cache, multi-stage : construire mieux sans se compliquer.",
    ),
    "docker-production-registry-securite": (
        "Docker en prod : ranger et protéger ses boîtes",
        "Registry privé, scan, non-root, secrets hors image : les bases sérieuses.",
    ),
    # AWS
    "aws-fondamentaux-cloud-aws-services": (
        "AWS : le cloud Amazon expliqué simplement",
        "Qui fait quoi (toi vs Amazon), et les familles de services sans te noyer dans le catalogue.",
    ),
    "aws-compute-ec2-lambda-ecs-eks": (
        "AWS : où faire tourner ton programme",
        "EC2, Lambda, ECS, EKS : choisir selon ta charge et ton équipe, pas la mode.",
    ),
    "aws-stockage-s3-ebs-efs": (
        "AWS : où ranger tes fichiers",
        "S3, EBS, EFS : trois façons de stocker, trois jobs différents.",
    ),
    "aws-bases-donnees-rds-dynamodb-aurora": (
        "AWS : où garder tes données",
        "RDS, Aurora, DynamoDB : choisir selon comment tu lis et écris vraiment.",
    ),
    "aws-reseaux-vpc-route53-cloudfront": (
        "AWS : routes, adresses et accélération web",
        "VPC, Route 53, CloudFront : du chemin réseau clair, du DNS au serveur.",
    ),
    "aws-securite-iam-kms-waf": (
        "AWS : qui a le droit d'ouvrir quoi",
        "IAM, clés, pare-feu applicatif : des couches de protection simples à comprendre.",
    ),
    "aws-observabilite-cloudwatch-xray-cloudtrail": (
        "AWS : voir ce qui se passe (et ce qui casse)",
        "Mesures, journaux, traces et audit : les quatre piliers pour ne pas voler à l'aveugle.",
    ),
    "aws-architectures-ha-scalabilite": (
        "AWS : rester en ligne même si une machine tombe",
        "Multi-AZ, autoscaling et tests de panne : la haute dispo sans slide marketing.",
    ),
    "aws-optimisation-couts-reserved-savings-spot": (
        "AWS : payer moins sans casser le service",
        "On-demand, Savings Plans, Spot : les leviers après avoir mesuré la facture.",
    ),
    "aws-devops-ci-cd-codepipeline-codebuild": (
        "AWS : publier du code automatiquement",
        "Du commit au déploiement avec des contrôles qualité — pas juste un bouton magique.",
    ),
}


def update(path: Path, title: str, excerpt: str | None) -> bool:
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith("---"):
        return False
    end = raw.find("\n---", 3)
    if end < 0:
        return False
    fm, body = raw[: end + 4], raw[end + 4 :]

    def repl_title(m: re.Match) -> str:
        return f'title: "{title}"'

    new_fm = re.sub(r'^title:\s*".*?"', repl_title, fm, count=1, flags=re.M)
    if excerpt is not None:
        esc = excerpt.replace('"', '\\"')
        new_fm = re.sub(
            r'^excerpt:\s*".*?"',
            f'excerpt: "{esc}"',
            new_fm,
            count=1,
            flags=re.M,
        )

    # H1 = même titre
    new_body, n = re.subn(r"^# .+$", f"# {title}", body, count=1, flags=re.M)
    if new_fm == fm and n == 0:
        return False
    path.write_text(new_fm + new_body, encoding="utf-8")
    return True


def main() -> None:
    n = 0
    for slug, (title, excerpt) in TITLES.items():
        path = ARTICLES / f"{slug}.md"
        if not path.is_file():
            print(f"[MISS] {slug}")
            continue
        if update(path, title, excerpt):
            n += 1
            print(f"[OK] {slug}")
        else:
            print(f"[SKIP] {slug}")
    print(f"updated={n}/{len(TITLES)}")


if __name__ == "__main__":
    main()
