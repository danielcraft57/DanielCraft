# Positionnement : travailler avec l'IA (DanielCraft)

Document de reference pour le marketing et les agents. Le vocabulaire **client** doit rester simple (voir `AGENTS.md` - Public client).

## En une phrase

Loic developpe depuis **2011** (licence **2018**), utilise l'IA au quotidien depuis **2025** avec une vraie expertise **prompts**, et livre plus vite - souvent une vitrine standard **en moins d'une semaine** - tout en gardant la main sur la qualite, les tests et la securite.

## Messages client (francais simple)

A utiliser / adapter (apostrophes `'`, tirets `-`) :

- « Je travaille avec l'IA depuis 2025 - ca va environ trois fois plus vite, et je controle tout avant de livrer. »
- « Pour une vitrine classique, on vise souvent moins d'une semaine une fois le brief clair. »
- « L'IA m'aide a aller plus vite ; l'experience sert a choisir ce qui est solide, a tester, a proteger le site. »
- « Un seul interlocuteur : moi. Pas une usine, pas un CMS tout fait. »

A eviter cote client : noms d'outils IA, jargon (LLM, tokens, pipeline), pourcentages d'etudes.

## Arguments « pourquoi un developpeur utilise l'IA »

Synthese utile (etudes / retours marche 2025-2026) - **pour agents et docs**, pas a coller bruts sur le site :

| Argument | Idee | Traduction client |
|----------|------|-------------------|
| Vitesse (taches repetitives) | McKinsey ~46 % de temps gagne sur le routinier, bien moins sur le complexe | « Sur le gros du site, on avance nettement plus vite » |
| Courbe d'apprentissage | METR : les gains montent quand on maitrise l'outil (pas magique jour 1) | « Depuis 2025 je l'utilise tous les jours - ca change le rythme » |
| Solo / freelance | Moins de temps sur le « milieu » mecanique (pages, textes, tests) = plus de livraisons | « Un freelance peut livrer plus sans baisser la barre » |
| Moins de corvee | Boilerplate, doc, explications, premiers jets de tests | « Moins de temps perdu sur le repetitif » |
| Adoption | Outil devenu standard (Copilot / agents tres largement adopts) | « C'est devenu normal chez les bons devs » |
| Prototypage | Essayer une idee rapidement avant de figer | « On peut te montrer une piste plus tot » |
| Verification | Le vrai metier : **relire** - le code IA a souvent plus de defauts / failles si on livre en aveugle | « Je relis et je teste - je ne livre pas en aveugle » |
| Securite | Jusqu'a ~2,7x plus de failles possibles sans revue (chiffres etudes) | « La securite reste de mon cote » |
| Prompts + jugement | Power users (bons prompts + revue) gagnent ; accepter sans lire = bugs | « Expertise prompts + experience 2011 = je sais quoi garder » |
| Architecture humaine | Decisions metier / structure restent au dev ; l'IA aide le milieu | « Je pilote ; l'outil accelere » |

Sources d'inspiration : Sonar State of Code ; Black Duck State of AI-Powered Software Development ; syntheses METR / McKinsey 2025-2026 (gains selon complexite + revue).

## Placement sur le site

| Page / zone | Fichier type | Contenu |
|-------------|--------------|---------|
| Accueil - Qui suis-je | `src/pages/index.html` `#about` | Bio + IA 2025 + delais |
| Accueil - FAQ | `src/pages/index.html` `#faq` | Question « Tu bosses avec l'IA ? » |
| Audit | `src/pages/audit.html` | Diagnostic rapide, experience + IA |
| Contact | `src/pages/contact.html` / include contact | Delais, un interlocuteur |
| Processus | `src/pages/processus.html` | Etape realisation = IA + controle humain |
| Nos offres | `src/includes/nos-offres-commerce-intro.html` | Rappel delai vitrine |
| Fiches prestations | templates + `prestations.json` desc | Delai indicatif, methode moderne controlee |
| Blog | articles serie pratique IA | Pedagogie sans jargon si cible commerce |
| Espace pro / projets | pages tech | OK vocabulaire plus precis |

## Regles agents

1. Client = **zero jargon** sauf page explicitement technique.
2. Toujours coupler IA + **controle humain** (tests, secu, relecture).
3. Ne pas promettre « 3x » ou « moins d'une semaine » sans rappel que ca depend du brief / devis.
4. Aligner apostrophes `'` et tirets `-` (AGENTS.md).
5. Conserver / enrichir les **microdata schema.org** (voir AGENTS.md) quand on touche HTML marketing.
6. Avatars Loic valides : `loic-*-ingenieur` uniquement (voir AGENTS.md - Avatars Loic).
