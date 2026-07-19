#!/usr/bin/env python3
"""Schemas Docker (6) + AWS (10) : generation SVG + insertion mid-article."""
from __future__ import annotations

import re
import sys
from pathlib import Path

# Reuse helpers from series3 script
sys.path.insert(0, str(Path(__file__).resolve().parent))
from add_series3_extra_schemas import (  # noqa: E402
    ARTICLES,
    SCHEMAS,
    compare2,
    esc,
    flow_row,
    grid3,
    insert_figure,
    stack_layers,
    svg_wrap,
)

SPECS = [
    # Docker — 1 schema each
    (
        "docker-fondamentaux-images-conteneurs",
        "docker-image-vs-conteneur.svg",
        "Image vs conteneur",
        "Image = plan figé, conteneur = instance vivante",
        compare2(
            "Image",
            ["Plan fige", "Layers lecture seule", "Registry / tag", "Ne tourne pas"],
            "Conteneur",
            ["Instance vivante", "RW layer", "PID / reseau", "Start / stop / rm"],
            "Une image, N conteneurs. L'etat vit dans le conteneur.",
        ),
        0,
        "Image = plan. Conteneur = instance. Ne les confonds plus.",
        "Schema Docker image versus conteneur",
    ),
    (
        "docker-installation-bonnes-pratiques",
        "docker-install-hygiene.svg",
        "Hygiene Docker locale",
        "Daemon, contextes, utilisateurs, prune",
        flow_row(
            ["Install", "User docker", "Context", "Prune", "Update"],
            "Un Docker mal configure = surprises en CI et en prod",
        ),
        1,
        "Installer ne suffit pas : user, contextes et prune font l'hygiene.",
        "Schema bonnes pratiques installation Docker",
    ),
    (
        "docker-volumes-reseaux",
        "docker-volumes-reseaux.svg",
        "Volumes et reseaux",
        "Bind, named volume, bridge, network alias",
        compare2(
            "Stockage",
            ["Named volume", "Bind mount", "tmpfs", "Backup / persist"],
            "Reseau",
            ["bridge", "host / none", "Alias DNS", "Multi-service"],
            "Donnees et reseau : les deux pieges du 'ca marche en local'",
        ),
        0,
        "Volumes pour persister, reseaux pour composer — pas l'inverse.",
        "Schema Docker volumes et reseaux",
    ),
    (
        "docker-compose-environnements-local",
        "docker-compose-stack.svg",
        "Stack Compose",
        "Services, networks, volumes, env files",
        stack_layers(
            [
                ("App / API", "service web"),
                ("Workers / jobs", "service worker"),
                ("DB / cache", "postgres, redis"),
                ("Networks + volumes", "isole et persiste"),
                (".env / overrides", "dev vs staging"),
            ],
            "Compose = contrat local reproductible, pas une usine a gaz",
        ),
        0,
        "Compose aligne services, reseaux et volumes sur un seul fichier.",
        "Schema d'une stack Docker Compose",
    ),
    (
        "docker-build-optimisation-images",
        "docker-build-layers.svg",
        "Build : layers et cache",
        "Ordre Dockerfile, multi-stage, .dockerignore",
        flow_row(
            [".dockerignore", "Deps d'abord", "Code ensuite", "Multi-stage", "Image slim"],
            "Le cache build se gagne dans l'ordre des instructions",
        ),
        1,
        "Deps avant le code, multi-stage a la fin : images plus petites et plus rapides.",
        "Schema optimisation build Docker layers cache",
    ),
    (
        "docker-production-registry-securite",
        "docker-prod-secu.svg",
        "Registry et secu prod",
        "Scan, signatures, non-root, secrets",
        grid3(
            [
                ("Registry prive", "Pas Hub public seul"),
                ("Scan CVE", "A chaque push"),
                ("Non-root", "USER dans image"),
                ("Secrets", "Pas dans ENV image"),
                ("Tags immuables", "Digest sha256"),
                ("Runtime", "Limits CPU/RAM"),
            ],
            "Prod = image signee, scannee, least privilege",
        ),
        1,
        "En prod : registry prive, scan, non-root, secrets hors image.",
        "Schema securite Docker en production et registry",
    ),
    # AWS — 1-2 schemas; longer articles get denser mid placement
    (
        "aws-fondamentaux-cloud-aws-services",
        "aws-shared-responsibility.svg",
        "Modele AWS",
        "Responsabilite partagee et familles de services",
        compare2(
            "AWS",
            ["Regions / AZ", "Hardware", "Hyperviseur", "Services managés"],
            "Toi",
            ["IAM / comptes", "Config VPC", "Donnees", "Apps / patch"],
            "Le cloud ne remplace pas ta gouvernance",
        ),
        0,
        "AWS gere l'infra de base. Toi : identites, config, donnees, apps.",
        "Schema responsabilite partagee AWS",
    ),
    (
        "aws-fondamentaux-cloud-aws-services",
        "aws-families-services.svg",
        "Familles de services",
        "Compute, stockage, data, reseau, securite",
        grid3(
            [
                ("Compute", "EC2, Lambda, ECS"),
                ("Stockage", "S3, EBS, EFS"),
                ("Data", "RDS, Dynamo, Aurora"),
                ("Reseau", "VPC, R53, CF"),
                ("Secu", "IAM, KMS, WAF"),
                ("Ops", "CW, X-Ray, Trail"),
            ],
            "Apprends par familles, pas par catalogue de 200 services",
        ),
        2,
        "Pense par familles de services : compute, data, reseau, secu, ops.",
        "Schema des familles de services AWS",
    ),
    (
        "aws-compute-ec2-lambda-ecs-eks",
        "aws-compute-choix.svg",
        "Choisir le compute",
        "EC2 vs Lambda vs ECS vs EKS",
        compare2(
            "Simple / controle",
            ["EC2 : VM classique", "ECS : conteneurs managés", "Peu d'ops K8s"],
            "Scale / events",
            ["Lambda : events", "EKS : orchestrateur", "Plus d'ops"],
            "Choisis selon charge, equipe et besoin d'orchestration",
        ),
        0,
        "EC2, Lambda, ECS, EKS : le bon choix suit la charge et l'equipe.",
        "Schema de choix compute AWS EC2 Lambda ECS EKS",
    ),
    (
        "aws-compute-ec2-lambda-ecs-eks",
        "aws-compute-ops.svg",
        "Ops compute",
        "Patch, scaling, couts, observabilite",
        flow_row(
            ["Workload", "Runtime", "Scale", "Observe", "Cost"],
            "Chaque runtime deplace le curseur ops / flexibilité",
        ),
        3,
        "Le runtime choisi deplace le curseur entre ops et flexibilite.",
        "Schema operations autour du compute AWS",
    ),
    (
        "aws-stockage-s3-ebs-efs",
        "aws-stockage-choix.svg",
        "S3, EBS, EFS",
        "Object, block, file storage",
        grid3(
            [
                ("S3", "Objets, HTTP, durabilite"),
                ("EBS", "Disque EC2"),
                ("EFS", "NFS partage"),
                ("Classes S3", "Standard → Glacier"),
                ("Backup", "Snapshots / versioning"),
                ("Secu", "KMS, policies"),
            ],
            "Mauvais stockage = couts et perf qui explosent",
        ),
        0,
        "S3 objet, EBS block, EFS fichier : trois jobs differents.",
        "Schema choix stockage AWS S3 EBS EFS",
    ),
    (
        "aws-bases-donnees-rds-dynamodb-aurora",
        "aws-databases-choix.svg",
        "Bases AWS",
        "RDS, Aurora, DynamoDB",
        compare2(
            "Relationnel",
            ["RDS classique", "Aurora scale", "SQL, transactions", "Migrations connues"],
            "DynamoDB",
            ["Cle-valeur / doc", "Scale massif", "Modelisation acces", "Pas de JOIN magique"],
            "Modele d'acces d'abord, moteur ensuite",
        ),
        0,
        "Relationnel ou Dynamo : le modele d'acces decide, pas la mode.",
        "Schema choix bases de donnees AWS RDS Aurora DynamoDB",
    ),
    (
        "aws-reseaux-vpc-route53-cloudfront",
        "aws-vpc-edge.svg",
        "VPC et edge",
        "VPC, subnets, Route53, CloudFront",
        stack_layers(
            [
                ("Utilisateurs", "DNS Route 53"),
                ("Edge CDN", "CloudFront"),
                ("Load balancer", "ALB / NLB"),
                ("Subnets app / data", "Public / private"),
                ("VPC + NAT / GW", "Isolation reseau"),
            ],
            "Reseau clair = blast radius limite",
        ),
        0,
        "Du DNS a la subnet privee : un chemin reseau lisible.",
        "Schema reseau AWS VPC Route53 CloudFront",
    ),
    (
        "aws-securite-iam-kms-waf",
        "aws-secu-couches.svg",
        "Securite AWS",
        "IAM, KMS, WAF, GuardDuty",
        flow_row(
            ["IAM", "KMS", "Network", "WAF", "Detect"],
            "Least privilege + chiffrement + detection",
        ),
        0,
        "IAM, KMS, reseau, WAF, detection : des couches, pas un outil unique.",
        "Schema couches securite AWS IAM KMS WAF",
    ),
    (
        "aws-observabilite-cloudwatch-xray-cloudtrail",
        "aws-observabilite.svg",
        "Observabilite AWS",
        "Metrics, logs, traces, audit",
        grid3(
            [
                ("Metrics", "CloudWatch"),
                ("Logs", "Log groups"),
                ("Traces", "X-Ray"),
                ("Audit", "CloudTrail"),
                ("Alarmes", "Seuils utiles"),
                ("Dashboards", "SLO simples"),
            ],
            "Sans Trail + alarmes, tu voles a l'aveugle",
        ),
        0,
        "Metrics, logs, traces, audit : les quatre piliers a brancher tot.",
        "Schema observabilite AWS CloudWatch X-Ray CloudTrail",
    ),
    (
        "aws-architectures-ha-scalabilite",
        "aws-ha-multi-az.svg",
        "HA multi-AZ",
        "Multi-AZ, ASG, decouplage",
        flow_row(
            ["Users", "LB", "ASG multi-AZ", "Data HA", "Failover"],
            "HA = redondance + tests de panne, pas un slide",
        ),
        0,
        "Haute dispo = multi-AZ, autoscaling, et des pannes qu'on a deja testees.",
        "Schema architecture haute disponibilite AWS multi-AZ",
    ),
    (
        "aws-optimisation-couts-reserved-savings-spot",
        "aws-cost-levers.svg",
        "Leviers de cout",
        "On-demand, Savings Plans, Reserved, Spot",
        compare2(
            "Previsible",
            ["Reserved / SP", "Baseline stable", "Engagement 1-3 ans", "Gros % economie"],
            "Flexible / batch",
            ["Spot", "Fault-tolerant", "Interruptible", "Couts bas"],
            "Mesure d'abord (Cost Explorer), optimise ensuite",
        ),
        1,
        "Baseline en Savings/Reserved, batch en Spot — apres avoir mesure.",
        "Schema leviers d'optimisation des couts AWS",
    ),
    (
        "aws-devops-ci-cd-codepipeline-codebuild",
        "aws-cicd-pipeline.svg",
        "CI/CD sur AWS",
        "Source, build, test, deploy",
        flow_row(
            ["Source", "CodeBuild", "Tests", "Artifact", "Deploy"],
            "Pipeline = qualite gates avant la prod, pas juste du deploy",
        ),
        0,
        "CodePipeline + CodeBuild : du commit au deploy avec des gates.",
        "Schema pipeline CI/CD AWS CodePipeline CodeBuild",
    ),
]


def main() -> None:
    SCHEMAS.mkdir(parents=True, exist_ok=True)
    svg_n = md_n = 0
    # Group by slug to allow multiple inserts
    for slug, fname, title, desc, body, h2i, caption, alt in SPECS:
        svg_path = SCHEMAS / fname
        svg_path.write_text(svg_wrap(title, desc, body), encoding="utf-8")
        svg_n += 1

        fig = f'''<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/{fname}" alt="{esc(alt)}" class="schema-inline" width="640" />
  <figcaption>{esc(caption)}</figcaption>
</figure>'''

        md_path = ARTICLES / f"{slug}.md"
        if not md_path.is_file():
            print(f"[MISS] {slug}")
            continue
        raw = md_path.read_text(encoding="utf-8")
        new = insert_figure(raw, h2i, fig)
        if new != raw:
            md_path.write_text(new, encoding="utf-8")
            md_n += 1
            print(f"[OK] {slug} -> {fname} @H2[{h2i}]")
        else:
            print(f"[SKIP-MD] {slug} {fname}")

    print(f"svgs={svg_n} md_updated={md_n} total_schemas={(len(list(SCHEMAS.glob('*.svg'))))}")


if __name__ == "__main__":
    main()
