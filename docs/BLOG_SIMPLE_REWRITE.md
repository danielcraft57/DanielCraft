# Blog : refonte « ton débutant » (articles + images)

Objectif : articles **lisibles par un débutant**, avec **schémas SVG** et **une seule image visuelle** (Open Graph = hero). **Pas de déploiement** dans ce flux sauf demande explicite.

## Principes articles

1. **Titre** : phrase claire, sans jargon inutile (ex. « Singleton : une seule copie, pas plus »).
2. **Corps court** : analogie du quotidien, **gras** sur les mots clés, 1 schéma, liens internes vers articles/séries proches.
3. **Pas de bannière** dans le markdown : retirer les `<figure>…-banner…`.
4. **Schéma** : SVG 800×420, palette DanielCraft, chemin absolu `/assets/images/blog/schemas/…`.
5. **Collection** : mettre à jour `title` / `description` de la série JSON.
6. **Build local** : `python blog/build_blog.py --output dist/blog` (pas de `scp` sauf demande).

## Scripts (par série)

| Série | Script |
|-------|--------|
| API / Cyber / UX / Docker / AWS | `simplify_article_titles.py` (+ schemas series3 / docker-aws) |
| CI/CD + Kubernetes | `scripts/simplify_cicd_k8s_articles.py` |
| SEO + GEO | `scripts/simplify_seo_geo_articles.py` |
| Marketing + Communication | `scripts/simplify_marketing_com_articles.py` |
| Design Patterns | `scripts/simplify_design_patterns_articles.py` |
| Helpers SVG | `scripts/add_series3_extra_schemas.py` (`flow_row`, `compare2`, `grid3`, `stack_layers`) |

Pattern d’un script : écrire les SVG → réécrire chaque `.md` (frontmatter `title`/`excerpt` + corps) → patcher la collection.

## Images OG (pas de bannières)

1. Régénérer les prompts après simplification des titres :
   ```bash
   python scripts/generate_simple_blog_og_prompts.py
   ```
   → `docs/prompt_og_images_articles_simple.md`  
   → `scripts/_blog_og_simple_manifest.json`

2. Générer les JPG **1200×630** (IA / Cursor) avec le **titre exact** du prompt, style débutant, bandeau bas « DanielCraft ».

3. Déposer les fichiers dans le dossier Cursor assets :
   `…/.cursor/projects/…DanielCraftFr/assets/`  
   nom typique : `{slug}-1200x630.jpg`

4. Installer dans le repo (crop/resize + WebP) :
   ```bash
   python scripts/install_ai_generated_blog_og.py --simple
   # ou un sous-ensemble :
   python scripts/install_ai_generated_blog_og.py --simple accessibilite-wcag-checklist …
   ```

5. Rebuild blog. **Ne pas** lancer `install_blog_article_banners.py`.

Le hero article utilise l’OG (`og_image` / `_get_article_hero_image` dans le build).

## Séries déjà passées en ton simple

API, Cyber, UX, Docker, AWS, CI/CD, Kubernetes, SEO, GEO, Marketing, Communication, Design Patterns.

## Suite

- Séries **IA** (`ia-*`) : titres souvent tronqués → même traitement (script + prompts OG).
- OG : beaucoup de JPG encore sur **anciens titres** ; à régénérer avec le doc `prompt_og_images_articles_simple.md`.

## Déploiement

**Désactivé par défaut** dans ce chantier. Si besoin plus tard : `scp` vers `pi@node12.lan:/var/www/danielcraft.fr` puis `chmod -R a+rX` — uniquement sur demande.
