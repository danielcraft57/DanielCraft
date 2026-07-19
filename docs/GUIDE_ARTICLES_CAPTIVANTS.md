# Articles blog captivants - guide DanielCraft

Synthese des bonnes pratiques (Backlinko, HubSpot, Google Tech Writing, Draft.dev) adaptees au ton humain du blog.

## Structure qui retient

1. **Accroche courte** (3-6 phrases) : probleme reel, scene, ou question. Pas de definition Wikipedia.
2. **Promesse claire** : ce que le lecteur va repartir avec.
3. **Corps en H2** : chaque section = une idee. Paragraphes courts (2-4 phrases).
4. **Exemples concrets** : TPE, artisan, SaaS, ticket Jira - pas de theorie pure.
5. **Conclusion ouverte** : une phrase d'action ou une question, pas un "en resume" robotique.

## Storytelling leger (meme en tech)

Arc simple : situation -> friction -> ce qui marche. Remplacer "il faut" par "tu" / scenes. Bucket brigades occasionnels ("Sauf que...", "En vrai...").

## Visuels : ou les mettre

| Type | Role | Placement |
|------|------|-----------|
| Hero OG (template) | Orienter le sujet | Deja dans le header article |
| Banniere inline | Eviter si = crop du hero | Ne pas empiler sous le H1 |
| Schema SVG | Expliquer une idee | **Juste apres** le 1er ou 2e paragraphe de la section qu'il illustre |
| 2e schema (rare) | Detail / comparaison | Avant une section dense ou apres une comparaison |

Regles Google Tech Writing / Draft.dev :
- Un schema = une idee (pas tout le systeme).
- Legende = le takeaway, pas "Schema du concept".
- Alt text descriptif.
- Pas deux figures collees en haut de page.
- Introduire le schema par le texte juste au-dessus (le lecteur a deja le contexte).
- Caption redigee *avant* le dessin si possible (force une idee claire).

Sources : [Google Tech Writing - Illustrations](https://developers.google.com/tech-writing/two/illustrations), [Draft.dev - Diagrams](https://draft.dev/learn/how-to-create-diagrams-for-technical-blog-posts).

Script : `python scripts/reposition_article_schemas.py` (retire bannieres redondantes, place le schema apres 2 paragraphes du 1er H2).

- Apostrophes droites `'`
- Tirets simples `-`
- Oral, imparfait OK, pas de jargon non explique
