#!/usr/bin/env python3
"""Genere un 2e schema SVG par article series3 + insertion mid-article.

Style aligne sur assets/images/blog/schemas/*.svg (800x420, palette DanielCraft).
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCHEMAS = ROOT / "assets" / "images" / "blog" / "schemas"
ARTICLES = ROOT / "blog" / "content" / "articles"
MANIFEST = ROOT / "scripts" / "_blog_og_series3_manifest.json"

FONT = "Segoe UI, Arial, sans-serif"
BG, INK, BLUE, LIGHT, RED, WHITE = (
    "#f5f7fb",
    "#0f172a",
    "#2563eb",
    "#60a5fa",
    "#dc2626",
    "#fff",
)


def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def svg_wrap(title: str, desc: str, body: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" role="img" aria-labelledby="title desc">
  <title id="title">{esc(title)}</title>
  <desc id="desc">{esc(desc)}</desc>
  <rect width="800" height="420" fill="{BG}"/>
  <text x="400" y="36" text-anchor="middle" font-family="{FONT}" font-size="18" font-weight="700" fill="{INK}">{esc(title)}</text>
{body}
  <defs>
    <marker id="a" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill="{INK}"/>
    </marker>
  </defs>
</svg>
'''


def flow_row(steps: list[str], footer: str) -> str:
    n = len(steps)
    gap = 16
    w = (760 - gap * (n - 1)) // n
    y = 140
    parts = []
    for i, label in enumerate(steps):
        x = 20 + i * (w + gap)
        stroke = RED if i == n - 1 else (LIGHT if i % 2 else BLUE)
        parts.append(
            f'  <rect x="{x}" y="{y}" width="{w}" height="70" rx="8" fill="{WHITE}" stroke="{stroke}" stroke-width="2"/>\n'
            f'  <text x="{x + w/2}" y="{y + 42}" text-anchor="middle" font-family="{FONT}" font-size="13" font-weight="600" fill="{INK}">{esc(label)}</text>'
        )
        if i < n - 1:
            ax1 = x + w + 2
            ax2 = x + w + gap - 2
            parts.append(
                f'  <path d="M{ax1} {y+35} H{ax2}" stroke="{INK}" stroke-width="2" fill="none" marker-end="url(#a)"/>'
            )
    parts.append(
        f'  <text x="400" y="390" text-anchor="middle" font-family="{FONT}" font-size="12" fill="{INK}">{esc(footer)}</text>'
    )
    return "\n".join(parts)


def compare2(left_title: str, left_items: list[str], right_title: str, right_items: list[str], footer: str) -> str:
    parts = [
        f'  <rect x="40" y="70" width="340" height="280" rx="10" fill="{WHITE}" stroke="{BLUE}" stroke-width="2"/>',
        f'  <text x="210" y="105" text-anchor="middle" font-family="{FONT}" font-size="16" font-weight="700" fill="{BLUE}">{esc(left_title)}</text>',
        f'  <rect x="420" y="70" width="340" height="280" rx="10" fill="{WHITE}" stroke="{RED}" stroke-width="2"/>',
        f'  <text x="590" y="105" text-anchor="middle" font-family="{FONT}" font-size="16" font-weight="700" fill="{RED}">{esc(right_title)}</text>',
    ]
    for side, items, cx, bx in (
        ("L", left_items, 210, 70),
        ("R", right_items, 590, 450),
    ):
        for i, it in enumerate(items[:5]):
            y = 130 + i * 40
            parts.append(
                f'  <rect x="{bx}" y="{y}" width="280" height="32" rx="6" fill="{BG}" stroke="{LIGHT}"/>\n'
                f'  <text x="{cx}" y="{y+21}" text-anchor="middle" font-family="{FONT}" font-size="12" fill="{INK}">{esc(it)}</text>'
            )
    parts.append(
        f'  <text x="400" y="390" text-anchor="middle" font-family="{FONT}" font-size="12" fill="{INK}">{esc(footer)}</text>'
    )
    return "\n".join(parts)


def stack_layers(layers: list[tuple[str, str]], footer: str) -> str:
    parts = []
    colors = [BLUE, LIGHT, BLUE, RED, LIGHT]
    for i, (label, sub) in enumerate(layers[:5]):
        y = 70 + i * 58
        c = colors[i % len(colors)]
        parts.append(
            f'  <rect x="120" y="{y}" width="560" height="48" rx="8" fill="{WHITE}" stroke="{c}" stroke-width="2"/>\n'
            f'  <text x="400" y="{y+22}" text-anchor="middle" font-family="{FONT}" font-size="14" font-weight="700" fill="{INK}">{esc(label)}</text>\n'
            f'  <text x="400" y="{y+40}" text-anchor="middle" font-family="{FONT}" font-size="11" fill="{INK}">{esc(sub)}</text>'
        )
    parts.append(
        f'  <text x="400" y="390" text-anchor="middle" font-family="{FONT}" font-size="12" fill="{INK}">{esc(footer)}</text>'
    )
    return "\n".join(parts)


def grid3(items: list[tuple[str, str]], footer: str) -> str:
    parts = []
    for i, (t, s) in enumerate(items[:6]):
        col, row = i % 3, i // 3
        x, y = 40 + col * 250, 80 + row * 130
        stroke = RED if i == 2 else (LIGHT if i % 2 else BLUE)
        parts.append(
            f'  <rect x="{x}" y="{y}" width="230" height="110" rx="10" fill="{WHITE}" stroke="{stroke}" stroke-width="2"/>\n'
            f'  <text x="{x+115}" y="{y+40}" text-anchor="middle" font-family="{FONT}" font-size="14" font-weight="700" fill="{INK}">{esc(t)}</text>\n'
            f'  <text x="{x+115}" y="{y+70}" text-anchor="middle" font-family="{FONT}" font-size="12" fill="{INK}">{esc(s)}</text>'
        )
    parts.append(
        f'  <text x="400" y="390" text-anchor="middle" font-family="{FONT}" font-size="12" fill="{INK}">{esc(footer)}</text>'
    )
    return "\n".join(parts)


# slug -> (filename, title, desc, body_fn_result, h2_index_0based, caption, alt)
# h2_index: where to insert (after 2 paras of that H2)
EXTRA: dict[str, dict] = {}


def define_extras() -> None:
    global EXTRA
    specs = [
        # API
        (
            "api-rest-graphql-fondamentaux-comparaison",
            "rest-graphql-ou-briller.svg",
            "Ou chacun brille",
            "REST pour CRUD stable, GraphQL pour vues composees",
            compare2(
                "REST",
                ["CRUD clair", "Cache HTTP simple", "Clients heterogenes", "Contrats stables"],
                "GraphQL",
                ["Ecrans composites", "Mobile data-light", "Evolution client rapide", "Un graphe metier"],
                "Choisis selon le pattern d'acces, pas la mode",
            ),
            3,
            "REST et GraphQL ne se battent pas sur le meme terrain : pattern d'acces d'abord.",
            "Schema ou REST et GraphQL excellent chacun",
        ),
        (
            "api-rest-bonnes-pratiques-conception",
            "rest-versioning-secu.svg",
            "Versioning et secu API",
            "Couches authentification, autorisation, version, monitoring",
            stack_layers(
                [
                    ("Clients", "Web, mobile, partenaires"),
                    ("AuthN / AuthZ", "OAuth2, scopes, least privilege"),
                    ("Version de contrat", "/v1 ou header Accept"),
                    ("Ressources + HTTP", "Verbes, codes, pagination"),
                    ("Observabilite", "Logs, rate limit, quotas"),
                ],
                "Securite et versioning = couches, pas un patch de derniere minute",
            ),
            3,
            "Securite et versioning : des couches stables autour du contrat HTTP.",
            "Schema des couches securite et versioning d'une API REST",
        ),
        (
            "graphql-fondamentaux-schema-queries",
            "graphql-n1-resolvers.svg",
            "N+1 et DataLoader",
            "Probleme N+1 resolvers vs batching DataLoader",
            compare2(
                "N+1 naif",
                ["1 query User", "N resolvers Orders", "N requetes SQL", "Latence qui explose"],
                "Avec batching",
                ["1 query User", "DataLoader", "1 requete batch", "Latence sous controle"],
                "Le schema est gratuit. Les resolvers, non.",
            ),
            2,
            "Sans batching, chaque champ peut devenir une requete : le piege N+1.",
            "Schema du probleme N+1 GraphQL et du batching DataLoader",
        ),
        (
            "api-rest-graphql-performances-benchmarks",
            "api-cache-layers.svg",
            "Caches API",
            "Couches de cache client, CDN, API, base",
            flow_row(
                ["Client", "CDN / edge", "API cache", "Base / store"],
                "Mesurer ou ca coute vraiment (CPU, egress, cold start), pas juste le TTFB",
            ),
            3,
            "Le perf game se joue souvent dans les caches, pas dans le framework.",
            "Schema des couches de cache cote API",
        ),
        (
            "choisir-rest-graphql-quand-et-comment",
            "rest-graphql-mix.svg",
            "Architecture mixte",
            "REST interne et GraphQL en facade BFF",
            stack_layers(
                [
                    ("Clients (web / mobile)", "Besoins d'ecrans differents"),
                    ("GraphQL BFF / gateway", "Compose les vues"),
                    ("Services REST internes", "CRUD stables, contrats clairs"),
                    ("Donnees", "SQL, search, object storage"),
                ],
                "Mixer : GraphQL en facade, REST la ou le domaine est stable",
            ),
            3,
            "Le mix gagnant : REST en interne, GraphQL en facade quand les ecrans le demandent.",
            "Schema d'architecture mixte REST interne et GraphQL facade",
        ),
        # Cyber
        (
            "cybersecurite-fondamentaux-menaces-risques",
            "cyber-pddr.svg",
            "Prevenir, detecter, repondre",
            "Trois boucles de posture securite",
            grid3(
                [
                    ("Prevenir", "MFA, patch, least privilege"),
                    ("Detecter", "Logs, EDR, alertes utiles"),
                    ("Repondre", "Contain, restore, post-mortem"),
                    ("Mesurer", "MFA %, RTO teste"),
                    ("Prioriser", "Actifs critiques d'abord"),
                    ("Iterer", "Chaque incident = lecon"),
                ],
                "Zero incident = mythe. Reactivity propre = objectif realiste",
            ),
            3,
            "Les trois boucles : prevenir, detecter, repondre — et mesurer pour ne pas se mentir.",
            "Schema prevenir detecter repondre en cybersécurité",
        ),
        (
            "secops-soc-fonctions-process",
            "secops-triage-severite.svg",
            "Triage SOC",
            "Entonnoir alertes vers incidents prioritaires",
            flow_row(
                ["Alertes", "Triage", "Investigation", "Incident", "Posture+"],
                "Sans triage strict, le SOC se noie dans le bruit",
            ),
            2,
            "Le triage decide si tu gagnes la journee ou si tu cours apres le bruit.",
            "Schema entonnoir de triage SOC des alertes aux incidents",
        ),
        (
            "siem-log-management-detection",
            "siem-faux-positifs.svg",
            "Signal vs bruit",
            "Equilibre detections, faux positifs et fatigue",
            compare2(
                "Trop sensible",
                ["1000 alertes/jour", "Fatigue analyste", "Vrai signal ignore", "Outil desactive"],
                "Juste assez",
                ["Regles ciblees", "Contexte enrichi", "Playbooks courts", "Tuning hebdo"],
                "Un SIEM utile = peu d'alertes, mais actionnables",
            ),
            4,
            "La vraie bataille du SIEM : moins d'alertes, plus d'actions.",
            "Schema signal versus bruit dans un SIEM",
        ),
        (
            "edr-xdr-endpoint-detection-response",
            "edr-containment.svg",
            "Containment EDR",
            "Isoler, tuer process, collecter preuves, remedier",
            flow_row(
                ["Detect", "Isoler host", "Kill / quarantine", "Forensics", "Remedier"],
                "Containment d'abord : arreter la saignee avant l'autopsie",
            ),
            4,
            "Repondre = containment d'abord, analyse ensuite.",
            "Schema des etapes de containment EDR",
        ),
        (
            "gestion-vulnerabilites-cve-patching",
            "vuln-priorisation.svg",
            "Prioriser les CVE",
            "CVSS, exposition, exploitabilite, actif critique",
            grid3(
                [
                    ("CVSS", "Score de base"),
                    ("Exposition", "Internet-facing ?"),
                    ("Exploit", "PoC / mass scan ?"),
                    ("Actif", "Prod critique ?"),
                    ("Compensations", "WAF, isolation"),
                    ("SLA patch", "P0 / P1 / P2"),
                ],
                "Pas de patching alphabetique : risque x contexte",
            ),
            2,
            "Prioriser = CVSS + exposition + exploit + criticite metier.",
            "Schema de priorisation des vulnerabilites CVE",
        ),
        (
            "iam-mfa-principes-zero-trust",
            "iam-mfa-facteurs.svg",
            "Facteurs MFA",
            "Quelque chose que tu sais, as, es",
            grid3(
                [
                    ("Sais", "Mot de passe / PIN"),
                    ("As", "Cle FIDO / TOTP"),
                    ("Es", "Biometrie"),
                    ("Contexte", "Device, lieu, risque"),
                    ("Session", "TTL court, step-up"),
                    ("Admin", "MFA obligatoire"),
                ],
                "MFA partout ou ca compte : mail, cloud, Git, VPN",
            ),
            2,
            "MFA = au moins deux facteurs. Zero Trust = verifier en continu.",
            "Schema des facteurs d'authentification MFA",
        ),
        (
            "incident-response-runbook-postmortem",
            "incident-postmortem.svg",
            "Post-mortem utile",
            "Timeline, causes, actions, owners, dates",
            flow_row(
                ["Timeline", "Causes", "Actions", "Owners", "Suivi"],
                "Blameless : chercher le systeme, pas le coupable",
            ),
            3,
            "Un post-mortem sans actions datees, c'est du theatre.",
            "Schema du deroule d'un post-mortem d'incident",
        ),
        (
            "securite-cloud-cspm-cwpp",
            "cloud-shared-responsibility.svg",
            "Responsabilite partagee",
            "Provider vs client sur IaaS PaaS SaaS",
            compare2(
                "Provider",
                ["Hardware / datacenter", "Hyperviseur", "Service managé", "Dispo region"],
                "Toi (client)",
                ["Identites IAM", "Config reseaux", "Donnees / chiffrement", "Patch apps / images"],
                "CSPM trouve tes erreurs de config. CWPP protege ce qui tourne.",
            ),
            2,
            "Le cloud n'efface pas ta part : identites, config, donnees.",
            "Schema du modele de responsabilite partagee cloud",
        ),
        (
            "devsecops-sast-dast-sbom",
            "devsecops-shift-left.svg",
            "Security gates CI/CD",
            "SAST, deps, secrets, DAST, SBOM dans le pipeline",
            flow_row(
                ["Code", "SAST", "Deps/SBOM", "Image", "DAST"],
                "Shift-left : trouver tot, bloquer seulement le critique",
            ),
            2,
            "Des gates progressives : signal tot, blocage seulement sur le critique.",
            "Schema des gates securite dans un pipeline DevSecOps",
        ),
        (
            "conformite-rgpd-nis2-iso27001",
            "conformite-preuves.svg",
            "Preuves de conformite",
            "Politique, controle, preuve, audit",
            flow_row(
                ["Politique", "Controle", "Preuve", "Audit", "Ameliorer"],
                "Sans preuve (logs, tickets, tests), la politique ne compte pas",
            ),
            2,
            "Conformite pragmatique = controle + preuve, pas binder poussiereux.",
            "Schema boucle politique controle preuve audit",
        ),
        # UX
        (
            "ux-ui-fondamentaux-differences",
            "ux-ui-livrables.svg",
            "Livrables UX et UI",
            "Recherche, flows, wireframes vs maquettes et design system",
            compare2(
                "UX",
                ["Interviews", "Parcours / JTBD", "Wireframes", "Tests utilisateurs"],
                "UI",
                ["Maquettes HI-FI", "Composants", "Tokens / DS", "Specs visuelles"],
                "Deux jobs, des livrables qui se branchent",
            ),
            2,
            "UX produit des decisions ; UI les rend visibles et coherentes.",
            "Schema des livrables UX versus UI",
        ),
        (
            "ergonomie-heuristiques-nielsen",
            "nielsen-severite.svg",
            "Severite UX",
            "Cotation 0 a 4 des problemes d'ergonomie",
            flow_row(
                ["0 Cosmetique", "1 Mineur", "2 Majeur", "3 Critique", "4 Bloquant"],
                "Prioriser par impact x frequence, pas par gout perso",
            ),
            2,
            "Noter la severite evite de tout traiter comme urgent.",
            "Schema des niveaux de severite des problemes UX Nielsen",
        ),
        (
            "wireframes-prototypage-fidelite",
            "wireframe-quand-monter.svg",
            "Quand monter en fidelite",
            "Low-fi pour structure, mid pour flow, hi-fi pour polish",
            flow_row(
                ["Idee", "Low-fi", "Test flow", "Mid/Hi-fi", "Dev"],
                "Monter en fidelite seulement quand la question l'exige",
            ),
            2,
            "La fidelite suit la question : structure, flow, puis polish.",
            "Schema de montee en fidelite wireframe vers prototype",
        ),
        (
            "ux-recherche-utilisateur-interviews-tests",
            "ux-insight-action.svg",
            "De l'insight a l'action",
            "Observation, insight, hypothese, experiment",
            flow_row(
                ["Observer", "Insight", "Hypothese", "Prototype", "Mesurer"],
                "Un insight sans decision = une belle note de meeting",
            ),
            2,
            "Recherche utile = insight branche sur une decision produit.",
            "Schema du passage insight recherche UX a action produit",
        ),
        (
            "parcours-utilisateur-mapping-jtbd",
            "parcours-emotion.svg",
            "Journey : etapes et frictions",
            "Etapes du parcours avec pics de friction",
            flow_row(
                ["Declencheur", "Recherche", "Action", "Friction", "Resultat"],
                "Mapper les emotions pour savoir ou reparer d'abord",
            ),
            2,
            "Le journey map sert a voir ou ca fait mal — pas a faire joli.",
            "Schema parcours utilisateur avec points de friction",
        ),
        (
            "design-system-composants-tokens",
            "design-system-adoption.svg",
            "Adoption design system",
            "Documenter, migrer, gouverner, mesurer",
            stack_layers(
                [
                    ("Gouvernance", "RFC, owners, changelog"),
                    ("Composants", "API stable, accessibilite"),
                    ("Tokens", "Couleur, type, espace"),
                    ("Docs + playground", "Storybook / exemples"),
                    ("Adoption produit", "% ecrans migres"),
                ],
                "Un DS sans adoption = une bibliotheque fantome",
            ),
            2,
            "Tokens et composants ne suffisent pas : il faut une vraie adoption.",
            "Schema des couches d'adoption d'un design system",
        ),
        (
            "accessibilite-wcag-checklist",
            "a11y-tests.svg",
            "Tester l'accessibilite",
            "Auto, clavier, lecteur d'ecran, utilisateurs",
            grid3(
                [
                    ("Auto", "axe, Lighthouse"),
                    ("Clavier", "Tab, Esc, focus"),
                    ("SR", "NVDA / VoiceOver"),
                    ("Contraste", "AA minimum"),
                    ("Formulaires", "Labels, erreurs"),
                    ("Humains", "Tests reels"),
                ],
                "L'auto trouve 30-40%. Le reste = clavier + humains",
            ),
            2,
            "Checklist + tests clavier + humains : l'auto ne suffit jamais.",
            "Schema des niveaux de test accessibilite WCAG",
        ),
        (
            "ui-typographie-couleurs-grille",
            "ui-hierarchie-visuelle.svg",
            "Hierarchie visuelle",
            "Taille, poids, couleur, espace pour guider l'oeil",
            stack_layers(
                [
                    ("H1 / hero", "Une idee dominante"),
                    ("H2 / sections", "Repères de scan"),
                    ("Corps", "Lisibilite 16px+"),
                    ("Meta / captions", "Secondaire, plus petit"),
                    ("Grille / espace", "8pt : respirer"),
                ],
                "Si tout crie, rien ne guide",
            ),
            2,
            "Typo + couleur + grille = une hierarchie que l'oeil comprend en 2 secondes.",
            "Schema de hierarchie visuelle typographie couleur grille",
        ),
        (
            "micro-interactions-feedback-etats",
            "micro-timing-feedback.svg",
            "Timing du feedback",
            "Immediat, progressif, succes, erreur",
            flow_row(
                ["Clic", "<100ms", "Loading", "Succes/Erreur", "Idle"],
                "Feedback trop lent = doute. Trop flashy = fatigue",
            ),
            2,
            "Le timing du feedback cree (ou casse) la confiance.",
            "Schema du timing des micro-interactions UI",
        ),
        (
            "mesurer-ux-kpis-analytics-ab-testing",
            "ux-ab-loop.svg",
            "Boucle A/B testing",
            "Hypothese, variant, mesure, decision",
            flow_row(
                ["Hypothese", "Variant", "Trafic", "Mesure", "Ship/Kill"],
                "Pas de vanity : une metrique primaire decidee avant le test",
            ),
            3,
            "A/B utile seulement si l'hypothese et la metrique sont fixees avant.",
            "Schema de la boucle A/B testing UX",
        ),
    ]
    for slug, fname, title, desc, body, h2i, caption, alt in specs:
        EXTRA[slug] = {
            "file": fname,
            "title": title,
            "desc": desc,
            "body": body,
            "h2_index": h2i,
            "caption": caption,
            "alt": alt,
        }


def insert_figure(md: str, h2_index: int, figure_html: str) -> str:
    """Insert figure after ~2 paragraphs of the Nth ## heading (0-based)."""
    if figure_html.split("schemas/")[1].split('"')[0] in md:
        return md  # already present

    matches = list(re.finditer(r"^## .+$", md, re.M))
    if h2_index >= len(matches):
        h2_index = max(0, len(matches) - 1)
    start = matches[h2_index].end()
    end = matches[h2_index + 1].start() if h2_index + 1 < len(matches) else len(md)
    section = md[start:end]

    parts = re.split(r"(\n\n+)", section)
    para_count = 0
    idx = 0
    while idx < len(parts) and para_count < 2:
        chunk = parts[idx]
        if chunk.strip() and not chunk.startswith("<") and not chunk.startswith("##"):
            para_count += 1
            idx += 1
            if idx < len(parts) and re.match(r"\n\n+", parts[idx] or ""):
                idx += 1
            continue
        idx += 1

    insert_rel = sum(len(parts[i]) for i in range(idx))
    abs_pos = start + insert_rel
    return md[:abs_pos] + "\n\n" + figure_html.strip() + "\n\n" + md[abs_pos:]


def main() -> None:
    define_extras()
    SCHEMAS.mkdir(parents=True, exist_ok=True)
    items = json.loads(MANIFEST.read_text(encoding="utf-8"))
    svg_n = md_n = 0

    for it in items:
        slug = it["slug"]
        if slug not in EXTRA:
            print(f"[SKIP] no extra for {slug}")
            continue
        ex = EXTRA[slug]
        svg_path = SCHEMAS / ex["file"]
        svg_path.write_text(
            svg_wrap(ex["title"], ex["desc"], ex["body"]),
            encoding="utf-8",
        )
        svg_n += 1

        fig = f'''<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/{ex["file"]}" alt="{esc(ex["alt"])}" class="schema-inline" width="640" />
  <figcaption>{esc(ex["caption"])}</figcaption>
</figure>'''

        md_path = ARTICLES / f"{slug}.md"
        raw = md_path.read_text(encoding="utf-8")
        new = insert_figure(raw, ex["h2_index"], fig)
        if new != raw:
            md_path.write_text(new, encoding="utf-8")
            md_n += 1
            print(f"[OK] {slug} -> {ex['file']} @H2[{ex['h2_index']}]")
        else:
            print(f"[OK-SVG] {slug} (md unchanged)")

    print(f"svgs={svg_n} md_updated={md_n}")


if __name__ == "__main__":
    main()
