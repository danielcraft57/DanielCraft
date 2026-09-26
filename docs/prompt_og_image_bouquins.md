# Style Open Graph bouquins & packs

## Livre seul

Cover centrée (`assets/images/livres/covers/<slug>.jpg`) sur fond papier.

## Pack

Composition `render_pack_showcase_og` :

1. **Eventail** de covers du pack (arrière-plan, légèrement pivotées)
2. **Page IA** mise en avant (`assets/images/livres/pack-pages/<slug>.jpg`)
3. **Titres** : nom du pack + titres des bouquins inclus + prix

## Génération

```bash
# Pages IA déjà dans pack-pages/ ; recomposer les OG packs :
python scripts/generate_site_og_images.py --only pack-web pack-mobile pack-ia
# ou tous les livres/packs :
python scripts/generate_site_og_images.py --only livres
```

WebP écrit à côté du JPG. Le build régénère aussi les WebP si le JPG est plus récent.
