#!/usr/bin/env python3
"""Glossaire de mots-cles -> articles, pour liens internes (1e occurrence hors liens/code)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES = ROOT / "blog" / "content" / "articles"

# Plus long / plus specifique d'abord
GLOSSARY: list[tuple[str, str]] = [
    # Cyber
    (r"Zero\s*Trust", "iam-mfa-principes-zero-trust"),
    (r"double\s+authentification|authentification\s+a\s+deux\s+facteurs|\bMFA\b|\b2FA\b", "iam-mfa-principes-zero-trust"),
    (r"\bIAM\b", "iam-mfa-principes-zero-trust"),
    (r"\bSecOps\b|\bSOC\b", "secops-soc-fonctions-process"),
    (r"\bSIEM\b", "siem-log-management-detection"),
    (r"\bXDR\b|\bEDR\b", "edr-xdr-endpoint-detection-response"),
    (r"vulnerabilit[eé]s?|\bCVE\b|patching", "gestion-vulnerabilites-cve-patching"),
    (r"r[eé]ponse\s+a\s+incident|post[\s\-]?mortem|runbook", "incident-response-runbook-postmortem"),
    (r"\bCSPM\b|\bCWPP\b", "securite-cloud-cspm-cwpp"),
    (r"\bDevSecOps\b|\bSAST\b|\bDAST\b|\bSBOM\b", "devsecops-sast-dast-sbom"),
    (r"\bRGPD\b|\bNIS2\b|ISO\s*27001", "conformite-rgpd-nis2-iso27001"),
    (r"cybers[eé]curit[eé]|menaces?|ransomware|phishing", "cybersecurite-fondamentaux-menaces-risques"),
    # API
    (r"\bGraphQL\b", "graphql-fondamentaux-schema-queries"),
    (r"\bREST\b", "api-rest-bonnes-pratiques-conception"),
    (r"benchmark|performances?\s+(REST|GraphQL|API)", "api-rest-graphql-performances-benchmarks"),
    (r"choisir\s+entre\s+REST|REST\s+ou\s+GraphQL", "choisir-rest-graphql-quand-et-comment"),
    # UX
    (r"heuristiques?\s+de\s+Nielsen|ergonomie", "ergonomie-heuristiques-nielsen"),
    (r"wireframes?|prototypage|fid[eé]lit[eé]", "wireframes-prototypage-fidelite"),
    (r"recherche\s+utilisateur|tests?\s+utilisateurs?", "ux-recherche-utilisateur-interviews-tests"),
    (r"parcours\s+utilisateur|journey\s+map|\bJTBD\b", "parcours-utilisateur-mapping-jtbd"),
    (r"design\s+system|tokens?", "design-system-composants-tokens"),
    (r"accessibilit[eé]|\bWCAG\b", "accessibilite-wcag-checklist"),
    (r"typographie|grille\s+(UI|visuelle)", "ui-typographie-couleurs-grille"),
    (r"micro[\s\-]?interactions?", "micro-interactions-feedback-etats"),
    (r"A/B\s*testing|KPIs?\s+UX|mesurer\s+l['']UX", "mesurer-ux-kpis-analytics-ab-testing"),
    (r"\bUX\b|\bUI\b", "ux-ui-fondamentaux-differences"),
    # Docker
    (r"Docker\s+Compose|Compose", "docker-compose-environnements-local"),
    (r"volumes?\s+Docker|r[eé]seaux?\s+Docker", "docker-volumes-reseaux"),
    (r"optimiser?\s+(une\s+)?image|multi[\s\-]?stage|Dockerfile", "docker-build-optimisation-images"),
    (r"registry|s[eé]curit[eé]\s+(en\s+)?prod(uction)?", "docker-production-registry-securite"),
    (r"\bDocker\b|conteneurs?|images?\s+Docker", "docker-fondamentaux-images-conteneurs"),
    # AWS
    (r"\bEC2\b|\bLambda\b|\bECS\b|\bEKS\b", "aws-compute-ec2-lambda-ecs-eks"),
    (r"\bS3\b|\bEBS\b|\bEFS\b", "aws-stockage-s3-ebs-efs"),
    (r"\bRDS\b|\bDynamoDB\b|\bAurora\b", "aws-bases-donnees-rds-dynamodb-aurora"),
    (r"\bVPC\b|Route\s*53|CloudFront", "aws-reseaux-vpc-route53-cloudfront"),
    (r"\bKMS\b|\bWAF\b", "aws-securite-iam-kms-waf"),
    (r"CloudWatch|X[\s\-]?Ray|CloudTrail", "aws-observabilite-cloudwatch-xray-cloudtrail"),
    (r"multi[\s\-]?AZ|haute\s+disponibilit[eé]|scalabilit[eé]", "aws-architectures-ha-scalabilite"),
    (r"Savings\s+Plans?|\bSpot\b|co[uû]ts?\s+AWS", "aws-optimisation-couts-reserved-savings-spot"),
    (r"CodePipeline|CodeBuild|CI/CD\s+(sur\s+)?AWS", "aws-devops-ci-cd-codepipeline-codebuild"),
    (r"\bAWS\b|cloud\s+AWS", "aws-fondamentaux-cloud-aws-services"),
]


def href(slug: str) -> str:
    return f"/blog/articles/{slug}.html"


def linkify(body: str, current_slug: str) -> str:
    """Ajoute des liens markdown sur la 1re occurrence de chaque motif (hors liens/code/figures)."""
    # Proteger blocs a ne pas toucher
    protected: list[str] = []

    def stash(m: re.Match) -> str:
        protected.append(m.group(0))
        return f"\x00P{len(protected)-1}\x00"

    work = body
    work = re.sub(r"```[\s\S]*?```", stash, work)
    work = re.sub(r"`[^`]+`", stash, work)
    work = re.sub(r"<figure[\s\S]*?</figure>", stash, work, flags=re.I)
    work = re.sub(r"\[[^\]]*\]\([^)]+\)", stash, work)
    work = re.sub(r"<a\s[^>]*>[\s\S]*?</a>", stash, work, flags=re.I)

    used_slugs: set[str] = set()
    for pattern, slug in GLOSSARY:
        if slug == current_slug or slug in used_slugs:
            continue
        # Skip if already linking to this slug somewhere
        if href(slug) in body:
            used_slugs.add(slug)
            continue

        def repl(m: re.Match, _slug=slug) -> str:
            return f"[{m.group(0)}]({href(_slug)})"

        new_work, n = re.subn(pattern, repl, work, count=1, flags=re.I)
        if n:
            work = new_work
            used_slugs.add(slug)

    def unstash(m: re.Match) -> str:
        return protected[int(m.group(1))]

    return re.sub(r"\x00P(\d+)\x00", unstash, work)


def process_file(path: Path) -> bool:
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith("---"):
        return False
    end = raw.find("\n---", 3)
    if end < 0:
        return False
    fm, body = raw[: end + 4], raw[end + 4 :]
    slug = path.stem
    new_body = linkify(body, slug)
    if new_body == body:
        return False
    path.write_text(fm + new_body, encoding="utf-8")
    return True


def main() -> None:
    import json
    man = json.loads((ROOT / "scripts" / "_blog_og_series3_manifest.json").read_text(encoding="utf-8"))
    slugs = [x["slug"] for x in man]
    slugs += [p.stem for p in ARTICLES.glob("docker-*.md")]
    slugs += [p.stem for p in ARTICLES.glob("aws-*.md")]
    n = 0
    for slug in slugs:
        p = ARTICLES / f"{slug}.md"
        if p.is_file() and process_file(p):
            n += 1
            print(f"[OK] {slug}")
    print(f"linkified={n}")


if __name__ == "__main__":
    main()
