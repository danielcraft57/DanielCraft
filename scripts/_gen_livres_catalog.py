#!/usr/bin/env python3
"""Genere src/data/livres.json (catalogue vente)."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "src" / "data" / "livres.json"

CATS = [
    {
        "id": "informatique",
        "title": "Informatique",
        "nav_label": "Informatique",
        "icon": "fa-laptop-code",
        "description": "Langages, web, SQL, Git et securite — du premier script au niveau expert.",
    },
    {
        "id": "ia",
        "title": "Intelligence artificielle",
        "nav_label": "IA",
        "icon": "fa-robot",
        "description": "Les bases de l'IA, le machine learning et le deep learning expliques simplement.",
    },
    {
        "id": "finance",
        "title": "Finance",
        "nav_label": "Finance",
        "icon": "fa-chart-line",
        "description": "Marches, produits et crypto : comprendre avant d'investir (pedagogie, pas un conseil perso).",
    },
    {
        "id": "commerce",
        "title": "Commerce & vente",
        "nav_label": "Commerce",
        "icon": "fa-store",
        "description": "Vendre mieux : offre, clients, e-commerce et dropshipping.",
    },
    {
        "id": "marketing",
        "title": "Marketing",
        "nav_label": "Marketing",
        "icon": "fa-bullhorn",
        "description": "Cible, message, canaux et mesure — sans jargon inutile.",
    },
    {
        "id": "communication",
        "title": "Communication",
        "nav_label": "Communication",
        "icon": "fa-comments",
        "description": "Parler clair : ecrire, presenter, convaincre.",
    },
    {
        "id": "agile",
        "title": "Agile et Scrum",
        "nav_label": "Agile",
        "icon": "fa-people-arrows",
        "description": "Gestion de projet agile, Scrum, roles Scrum Master et Product Owner - en langage simple.",
    },
]

# slug, category, level, title, tagline, short, keywords, source, pdf, icon, featured
RAW = [
    ("html-css-les-bases", "informatique", "base", "HTML & CSS — Les bases", "Ta premiere page web, propre et responsive", "Apprends a structurer une page et a la styliser. Ideal pour demarrer le web.", "html,css,web,front,debutant", "informatique/html-css", "html-css-les-bases.pdf", "fa-code", True),
    ("html-css-la-suite", "informatique", "intermediaire", "HTML & CSS — La suite", "Layouts, composants et polish", "Passe au niveau suivant : grilles, flex avance, composants reutilisables.", "html,css,flexbox,grid,web", "informatique/html-css-suite", "html-css-la-suite.pdf", "fa-code", False),
    ("javascript-les-bases", "informatique", "base", "JavaScript — Les bases", "Rendre la page vivante", "Variables, conditions, DOM et evenements — le JS utile au quotidien.", "javascript,js,dom,front,debutant", "informatique/javascript", "javascript-les-bases.pdf", "fa-js", True),
    ("javascript-la-suite", "informatique", "intermediaire", "JavaScript — La suite", "Modules, async et pratique", "Continue apres les bases : organisation du code, asynchrone, bons reflexes.", "javascript,js,async,modules", "informatique/javascript-suite", "javascript-la-suite.pdf", "fa-js", False),
    ("typescript-les-bases", "informatique", "base", "TypeScript — Les bases", "Typer pour moins se tromper", "Ajoute des types a ton JS et ecris du code plus solide.", "typescript,ts,types,javascript", "informatique/typescript", "typescript-les-bases.pdf", "fa-file-code", False),
    ("python-les-bases", "informatique", "base", "Python — Les bases", "Le langage polyvalent, version claire", "Syntaxe, structures et premiers scripts — parfait pour debuter.", "python,script,debutant,backend", "informatique/python", "python-les-bases.pdf", "fa-python", True),
    ("python-pratique", "informatique", "intermediaire", "Python — Pratique", "Projets concrets apres les bases", "Ateliers et mini-projets pour ancrer Python dans le vrai monde.", "python,projets,pratique,fichiers", "informatique/python-pratique", "python-pratique.pdf", "fa-python", False),
    ("java-les-bases", "informatique", "base", "Java — Les bases", "OOP et premiers programmes", "Classes, objets et bases du langage Java, expliquees simplement.", "java,oop,debutant", "informatique/java", "java-les-bases.pdf", "fa-mug-hot", False),
    ("java-intermediaire", "informatique", "intermediaire", "Java — Intermediaire", "Collections, exceptions, pratique", "Monte d'un cran : structures, erreurs et bons reflexes Java.", "java,collections,exceptions", "informatique/java-intermediaire", "java-intermediaire.pdf", "fa-mug-hot", False),
    ("kotlin-les-bases", "informatique", "base", "Kotlin — Les bases", "Modernite sur la JVM", "Decouvre Kotlin : null-safety, syntaxe nette, premiers programmes.", "kotlin,jvm,android,debutant", "informatique/kotlin", "kotlin-les-bases.pdf", "fa-mobile-alt", False),
    ("kotlin-intermediaire", "informatique", "intermediaire", "Kotlin — Intermediaire", "Fonctions, classes et pratique", "Approfondis Kotlin apres les bases, avec des cas concrets.", "kotlin,fonctions,classes", "informatique/kotlin-intermediaire", "kotlin-intermediaire.pdf", "fa-mobile-alt", False),
    ("csharp-les-bases", "informatique", "base", "C# — Les bases", "Le langage .NET, version accessible", "Variables, classes et premiers programmes en C#.", "csharp,c#,dotnet,debutant", "informatique/csharp", "csharp-les-bases.pdf", "fa-hashtag", False),
    ("go-les-bases", "informatique", "base", "Go — Les bases", "Simple, rapide, concurrent", "Prends en main Go : packages, types et premiers programmes.", "go,golang,backend,debutant", "informatique/go", "go-les-bases.pdf", "fa-bolt", False),
    ("php-les-bases", "informatique", "base", "PHP — Les bases", "Le web cote serveur", "Pages dynamiques, formulaires et bases de PHP pour le web.", "php,serveur,web,debutant", "informatique/php", "php-les-bases.pdf", "fa-php", False),
    ("rust-les-bases", "informatique", "base", "Rust — Les bases", "Memoire sure, sans panique", "Ownership et types : Rust explique sans jargon inutile.", "rust,memoire,systeme,debutant", "informatique/rust", "rust-les-bases.pdf", "fa-cog", False),
    ("ruby-les-bases", "informatique", "base", "Ruby — Les bases", "Elegant et lisible", "Syntaxe douce et premiers scripts Ruby.", "ruby,script,debutant", "informatique/ruby", "ruby-les-bases.pdf", "fa-gem", False),
    ("swift-les-bases", "informatique", "base", "Swift — Les bases", "Pour l'ecosysteme Apple", "Optionals, types et premiers programmes Swift.", "swift,ios,apple,debutant", "informatique/swift", "swift-les-bases.pdf", "fa-apple", False),
    ("c-cpp-les-bases", "informatique", "base", "C / C++ — Les bases", "Proche de la machine", "Pointeurs, memoire et bases C/C++ en langage simple.", "c,c++,pointeurs,systeme", "informatique/c-cpp", "c-cpp-les-bases.pdf", "fa-microchip", False),
    ("sql-les-bases", "informatique", "base", "SQL — Les bases", "Interroger des tables", "SELECT, JOIN, INSERT : parler a une base de donnees.", "sql,base de donnees,data,requetes", "informatique/sql", "sql-les-bases.pdf", "fa-database", True),
    ("sql-intermediaire", "informatique", "intermediaire", "SQL — Intermediaire", "Sous-requetes, dates, vues", "Passe a des questions plus riches : HAVING, unions, index (idee).", "sql,sous-requetes,having,data", "informatique/sql-intermediaire", "sql-intermediaire.pdf", "fa-database", False),
    ("sql-expert", "informatique", "expert", "SQL — Expert", "Perf, fenetres, cas durs", "Fenetres, perf et cas metier exigeants — pour aller loin.", "sql,window,performance,expert", "informatique/sql-expert", "sql-expert.pdf", "fa-database", False),
    ("git-les-bases", "informatique", "base", "Git — Les bases", "Versionner sans stress", "Commit, branche, historique : le kit minimum pour ne plus perdre ton code.", "git,versionning,commit,github", "informatique/git", "git-les-bases.pdf", "fa-code-branch", False),
    ("git-en-equipe", "informatique", "intermediaire", "Git — En equipe", "PR, rebase, CI", "Travailler a plusieurs sans panique : revue, branches, bons reflexes.", "git,pull request,equipe,ci", "informatique/git-equipe", "git-en-equipe.pdf", "fa-users", False),
    ("securite-web-les-bases", "informatique", "base", "Securite web — Les bases", "Proteger le quotidien", "Mots de passe, HTTPS, phishing, sauvegardes : les gestes essentiels.", "securite,https,phishing,rgpd", "informatique/securite-web", "securite-web-les-bases.pdf", "fa-shield-alt", True),
    ("securite-web-intermediaire", "informatique", "intermediaire", "Securite web — Intermediaire", "Attaques et defenses concretes", "XSS, CSRF, sessions : comprendre pour mieux proteger.", "securite,xss,csrf,owasp", "informatique/securite-web-intermediaire", "securite-web-intermediaire.pdf", "fa-shield-alt", False),
    ("securite-web-expert", "informatique", "expert", "Securite web — Expert", "Hardening et cas avances", "Aller plus loin : hardening, modeles de menaces, bonnes pratiques pro.", "securite,hardening,expert,audit", "informatique/securite-web-expert", "securite-web-expert.pdf", "fa-user-shield", False),
    ("ia-les-bases", "ia", "base", "IA — Les bases", "Comprendre avant d'automatiser", "Prompts, outils et ethique : l'IA utile au quotidien, sans magie.", "ia,prompt,chatgpt,debutant", "ia/essentiel", "ia-les-bases.pdf", "fa-robot", True),
    ("ia-machine-learning", "ia", "intermediaire", "IA — Machine learning", "Donnees, modeles, metriques", "Regression, classification et pipelines — le ML explique clairement.", "machine learning,ml,scikit-learn,data", "ia/machine-learning", "ia-machine-learning.pdf", "fa-brain", False),
    ("ia-deep-learning", "ia", "expert", "IA — Deep learning", "Reseaux, CNN, transformers", "Neurones, couches et architectures modernes, en langage accessible.", "deep learning,cnn,transformers,neural", "ia/deep-learning", "ia-deep-learning.pdf", "fa-network-wired", False),
    ("finance-les-bases", "finance", "base", "Finance — Les bases", "Lire les marches sans jargon", "Budget, risque, produits : une boussole pour commencer.", "finance,investissement,debutant,epargne", "finance/essentiel", "finance-les-bases.pdf", "fa-wallet", False),
    ("finance-actions-obligations", "finance", "intermediaire", "Finance — Actions & obligations", "Actions, obligations, portefeuille", "Comprendre actions et obligations avant de construire un portefeuille.", "actions,obligations,bourse,portefeuille", "finance/actions-obligations", "finance-actions-obligations.pdf", "fa-chart-pie", False),
    ("finance-produits-derives", "finance", "expert", "Finance — Produits derives", "Options, futures (idee)", "Les derives expliques sans promesse miracle.", "derives,options,futures,hedging", "finance/produits-derives", "finance-produits-derives.pdf", "fa-exchange-alt", False),
    ("finance-forex-matieres", "finance", "intermediaire", "Finance — Forex & matieres", "Devises et matieres premieres", "Forex et matieres : mecanismes, risques, vocabulaire.", "forex,devises,or,petrole", "finance/forex-matieres", "finance-forex-matieres.pdf", "fa-globe", False),
    ("finance-crypto", "finance", "intermediaire", "Finance — Crypto", "Wallets, risques, bonnes pratiques", "Crypto sans hype : wallet, arnaques, securite, staking (idee).", "crypto,bitcoin,wallet,blockchain", "finance/crypto", "finance-crypto.pdf", "fa-coins", False),
    ("commerce-les-bases", "commerce", "base", "Commerce — Les bases", "Offre, marge, relation client", "Vendre mieux : besoin, offre, prix et relation.", "commerce,vente,marge,client", "commerce/essentiel", "commerce-les-bases.pdf", "fa-handshake", False),
    ("vente-avancee", "commerce", "intermediaire", "Vente avancee", "Negociation et closing", "Objections, closing et vente en equipe — niveau suivant.", "vente,negociation,closing,b2b", "commerce/vente-avancee", "vente-avancee.pdf", "fa-comments-dollar", False),
    ("ecommerce-trouver-clients", "commerce", "intermediaire", "E-commerce — Trouver des clients", "Trafic et acquisition", "Attirer des clients : canaux, mesure, funnels simples.", "ecommerce,acquisition,traffic,ads", "commerce/trouver-clients", "ecommerce-trouver-clients.pdf", "fa-users", False),
    ("ecommerce-clients", "commerce", "intermediaire", "E-commerce — Clients", "Retention et LTV", "Apres le clic : email, contenu, mesure et ethique.", "ecommerce,retention,ltv,email", "commerce/ecommerce-clients", "ecommerce-clients.pdf", "fa-heart", False),
    ("dropshipping", "commerce", "intermediaire", "Dropshipping", "Niche, fournisseurs, realite", "Le dropshipping sans mythes : marges, logistique, pieges.", "dropshipping,fournisseurs,niche,boutique", "commerce/dropshipping", "dropshipping.pdf", "fa-box-open", False),
    ("ecommerce-dropshipping", "commerce", "intermediaire", "E-commerce & dropshipping", "Lancer sans stock (avec prudence)", "Combinaison e-commerce + dropshipping : cadre legal et lancement.", "ecommerce,dropshipping,lancement,juridique", "commerce/ecommerce-dropshipping", "ecommerce-dropshipping.pdf", "fa-store", False),
    ("marketing-les-bases", "marketing", "base", "Marketing — Les bases", "Cible, message, canaux", "Persona, funnel, contenu et mesure — le marketing utile.", "marketing,persona,funnel,seo", "marketing/essentiel", "marketing-les-bases.pdf", "fa-bullhorn", False),
    ("communication-les-bases", "communication", "base", "Communication — Les bases", "Ecrire et parler clair", "Messages nets, presentations et relation — sans blabla.", "communication,ecriture,presentation,clair", "communication/essentiel", "communication-les-bases.pdf", "fa-comments", False),
    ("gestion-projet-agile", "agile", "base", "Gestion de projet agile", "Petits pas, priorites claires, feedback tot", "Comprendre l'agile sans jargon de certif : cascade vs iteratif, backlog, ceremonies.", "agile,gestion de projet,backlog,iteration,scrum", "agile/gestion-projet", "gestion-projet-agile.pdf", "fa-people-arrows", False),
    ("methodologie-scrum", "agile", "base", "Methodologie Scrum", "Sprints, roles, ceremonies, Definition of Done", "Le cadre Scrum explique simplement : equipe, artefacts, evenements.", "scrum,sprint,backlog,daily,retro", "agile/methodologie-scrum", "methodologie-scrum.pdf", "fa-sync-alt", False),
    ("devenir-scrum-master", "agile", "intermediaire", "Devenir Scrum Master", "Faciliter, debloquer, coacher sans prendre le volant", "Le role Scrum Master au quotidien : facilitation, obstacles, focus, coaching.", "scrum master,facilitation,coaching,agile,equipe", "agile/scrum-master", "devenir-scrum-master.pdf", "fa-hands-helping", False),
    ("devenir-product-owner", "agile", "intermediaire", "Devenir Product Owner", "Vision, backlog, priorisation, valeur client", "Le role Product Owner : vision, stakeholders, user stories, priorisation.", "product owner,backlog,priorisation,vision,agile", "agile/product-owner", "devenir-product-owner.pdf", "fa-bullseye", False),
]


def main() -> None:
    items = []
    for slug, cat, level, title, tagline, short, kw, source, pdf, icon, feat in RAW:
        items.append(
            {
                "slug": slug,
                "category": cat,
                "level": level,
                "title": title,
                "tagline": tagline,
                "short_description": short,
                "description": (
                    f"{short} Format PDF telechargeable, langage simple, exercices et schemas. "
                    "Chez DanielCraft."
                ),
                "keywords": [k.strip() for k in kw.split(",") if k.strip()],
                "source_dir": source,
                "pdf": pdf,
                "icon": icon,
                "price_eur": 4.9,
                "price_label": "Prix d'appel",
                "price_note": "TTC — PDF envoye par e-mail apres paiement",
                "currency": "EUR",
                "featured": feat,
                "has_page": True,
                "stripe_payment_link_url": "",
                "benefits": [
                    "PDF clair, plusieurs dizaines de pages",
                    "Schemas et exemples concrets (Lea, Max, Sam)",
                    "Ateliers et quiz pour ancrer",
                    "Langage simple, sans jargon inutile",
                ],
                "includes": [
                    "Livre PDF complet",
                    "Acces a vie au fichier envoye",
                    "Mises a jour mineures si corrigees",
                ],
            }
        )

    data = {
        "currency": "EUR",
        "default_price_eur": 4.9,
        "price_display": "TTC",
        "stripe_note": "Checkout dynamique via api/stripe-create-livre-checkout.php.",
        "intro_note": "Prix d'appel de lancement — livres de formation PDF.",
        "categories": CATS,
        "levels": [
            {"id": "base", "label": "Base", "icon": "fa-seedling"},
            {"id": "intermediaire", "label": "Intermediaire", "icon": "fa-layer-group"},
            {"id": "expert", "label": "Expert", "icon": "fa-mountain"},
        ],
        "featured_order": [
            "javascript-les-bases",
            "python-les-bases",
            "html-css-les-bases",
            "ia-les-bases",
            "sql-les-bases",
            "securite-web-les-bases",
        ],
        "items": items,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"[OK] {len(items)} livres -> {OUT}")


if __name__ == "__main__":
    main()
