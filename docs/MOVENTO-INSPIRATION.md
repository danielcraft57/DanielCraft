# Inspiration Movento → echantillons DanielCraft

Recherche navigateur (sep. 2026). Pages `https://movento.dev/prompt/<slug>`.
Prompts texte = paywall. On s'appuie sur demos live, previews image/video et tokens CSS.
**Ne pas** copier les prompts payants ni telecharger les assets Movento dans le repo.

---

## Patterns Movento (reutilisables)

### Heroes

| Pattern | Vu sur | Notes |
|--------|--------|--------|
| Split + photo bleed | Fiamma, Dental | Texte gauche, image droite pleine hauteur |
| Full-bleed cinematic photo | Healcure, Hunsy, Angelo, CargoX, Adventra, Baseline | Image viewport, overlay, H1 bas ou centre |
| Cinematic dark | Serene | Fond sombre + H1 serif geant + CTA pill |
| Giant type / editorial | Dental, Baseline, Beanro, Chipmuk, Graven | Typo enorme (souvent 100px+) |
| Glass feature bars | Dental | 3 barres translucides (benefices) |
| Dark luxury food | Basilico | Noir + or, grille plats |
| Warm product splash | Beanro | Creme + terracotta |
| Surreal agency | Portiva, Chipmuk | Photo/3D cinematic, nav pill |
| Technical luxury | Graven | Dark grid / blueprint |

### Nav et CTAs

- Pill / floating nav : Angelo (glass), Chipmuk, Serene
- Dual CTA : Angelo (Appeler + Devis), Fiamma (Reserver + Carte)
- Location badge : Angelo (Nancy + alentours)
- Social proof strip : Healcure, Hunsy, Portiva

### Sections utiles commerce local

- Preuve locale / avis
- Services cards
- Avant/apres
- Formulaire devis / reservation
- Process 3-4 etapes
- Galerie metier

### A reutiliser pour ProspectLab

1. Split hero + giant type + 1 accent fort (Dental → sante)
2. Full-bleed metier + dual CTA appel/devis + badge ville (Angelo → artisan / BTP / services)
3. Split editorial creme + serif + accent couleur metier (Fiamma → resto)
4. Sections full-viewport, peu de cards, photo reelle dominante

---

## Mapping prompt → secteur ProspectLab

| Slug Movento | Secteur / slug vitrines | Priorite |
|--------------|-------------------------|----------|
| basilico-restaurant / fiamma-pizzeria | restauration | Haute |
| beanro-coffee-shop | commerce / cafe | Moyenne |
| healcure-medical / dental-health-clinic | odontologie (sante) | Tres haute |
| serene-wellness | beaute | Moyenne |
| wandor / adventra | gites (tourisme) | Basse |
| hunsy-car-rental | automobile | Haute |
| portiva / chipmuk | communication / photo | Moyenne |
| cargox-group-hero | transport / industrie | Haute |
| baseline-tennis-club | fitness (loisirs) | Haute |
| graven-drafting-works | btp / architecture | Moyenne |
| angelo-elagage-nancy | artisan / services | Tres haute |

---

## Palettes et typos observees

| Demo | Palette | Typos |
|------|---------|-------|
| Fiamma | cream #FDFBF7, ink #1C1A17, red #C8102E, gold #C9A227 | Instrument Serif + Inter |
| Serene | near-black, blanc, glow | Instrument Serif + Inter |
| Hunsy | blanc UI + cuivre photo | Sans geometrique |
| Dental | blanc / noir + accent photo | Open Sauce One, H1 ~176px |
| Angelo | forest #1f3d2b, leaf #8fcf9a, paper #fbfcf9 | Avenir Next / SF Pro |

---

## Demos live (URL)

| Slug | URL live |
|------|----------|
| fiamma-pizzeria | https://pizza-jade-ten.vercel.app/ |
| serene-wellness | https://radiant-serene.lovable.app/ |
| hunsy-car-rental | https://grand-ride-intro.lovable.app/ |
| baseline-tennis-club | https://court-craft-html.lovable.app/ |
| dental-health-clinic | https://luminous-clinic-render.lovable.app/ |
| angelo-elagage-nancy | https://angelo-self.vercel.app/ |

---

## Media preview (analyse seulement - ne pas telecharger)

Voir historiques de session agent : R2 `pub-86dc5b…`, Cloudinary, SceneAI, GetLayers, posters `/posters/*.jpg` sur movento.dev.

---

## Flagships DanielCraft (19 secteurs)

| Secteur | Slug | Pattern Movento cible |
|---------|------|----------------------|
| Artisanat | artisan | Bleed Angelo |
| Automobile | automobile | Bleed Hunsy |
| Beaute | beaute | Dark Serene / soft |
| BTP | btp | Bleed Angelo + tech Graven |
| Commerce | commerce | Warm Beanro |
| Communication | communication | Agency Portiva |
| Education | education | Split editorial |
| Finance | banque | Split sobre |
| Hotellerie | etablissement | Cinematic luxury |
| Immobilier | immobilier | Split editorial |
| Industrie | industrie | Tech Graven / CargoX |
| Juridique | juridique | Split sobriety |
| Loisirs | fitness | Giant Baseline |
| Restauration | restauration | Split Fiamma / dark Basilico |
| Sante | odontologie | Split Dental |
| Services | services | Bleed Angelo |
| Technologie | technologie | Agency dark |
| Tourisme | gites | Cinematic Adventra |
| Transport | transport | Bleed CargoX |

Kit technique : `assets/vitrines/demos/shared/vitrine-movento.css` + blocs dans `scripts/vitrine_layouts.py`.

## Statut execution

| Vague | Contenu | Statut |
|-------|---------|--------|
| Nouveaux | `btp`, `communication`, `transport` | Fait (`vitrine_secteurs_movento.py`) |
| Vague A | artisan, automobile, beaute, commerce, immobilier, juridique, odontologie, restauration | Fait (`vitrine_movento_vague_a.py`) |
| Vague B | industrie, education, services, etablissement, technologie, fitness, banque, gites | Fait (`vitrine_movento_vague_b.py`) |
| Vague C | boulangerie, chocolaterie, traiteur, fleuriste, caviste, coiffure, yoga, kine, osteo | Fait (`vitrine_movento_vague_c.py`) |
| Vague D | electricien, architecture, promoteur, comptable, assurance, notaire, logistique, photographie, association | Fait (`vitrine_movento_vague_d.py`) |
| Hors scope | `saas-*` | Demos produit (pas commerce local) |
