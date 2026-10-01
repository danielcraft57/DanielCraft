---
title: "Les outils : donner des mains au modèle"
date: 2026-10-04
excerpt: "Le modèle demande, ton site exécute. Comment brancher horaires, stock ou FAQ sans jargon."
type: tutorial
tags: [agents IA, outils, formation, débutant, Hugging Face]
series: hf-agents-serie
series_order: 2
og_image: agents-hf-outils-et-function-calling-1200x630.jpg
---

# Les outils : donner des mains au modèle

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/agents-hf-tools.svg" alt="Schéma : question, choix d'outil, exécution, résultat" class="schema-inline" width="800" />
  <figcaption>Le modèle choisit un outil ; ton code fait le vrai travail.</figcaption>
</figure>

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/agents-hf-tools-illustration.jpg" alt="Illustration : les 4 étapes des outils" class="schema-inline" width="800" loading="lazy" />
  <figcaption>Question, choix, exécution, réponse - le film en images.</figcaption>
</figure>

Dans l'article précédent, on a dit : un agent a un cerveau, des outils, et une boucle. Ici on zoom sur **les outils**. C'est la partie la plus concrète. Et souvent celle qu'on explique trop mal.

Inspiration libre du [cours Agents Hugging Face](https://huggingface.co/learn/agents-course). Texte simple, exemples boutique.

## En une phrase

Un **outil**, c'est une capacité réelle de ton système (horaires, stock, FAQ) que le modèle a le droit de demander.

Le modèle dit : « appelle horaires pour samedi ».  
Ton serveur le fait.  
Tu renvoies le résultat au modèle.  
Lui, il te parle ensuite.

## Analogie du tiroir

Imagine un tiroir d'outils au magasin :

- clé des horaires ;
- carnet des délais de devis ;
- feuille de stock.

Le stagiaire (le modèle) ne peut utiliser **que** ce qu'il y a dans le tiroir. Pas la caisse enregistreuse, pas le coffre. Toi tu remplis le tiroir.

## Petit exemple Python (lisible)

```python
def get_horaires_boutique(jour: str) -> str:
    """Donne les horaires pour un jour (ex. samedi)."""
    data = {
        "samedi": "10h-17h",
        "dimanche": "ferme",
        "lundi": "ferme",
    }
    return data.get(jour.strip().lower(), "jour inconnu")
```

Tu vois : c'est du code normal. Pas de magie.  
Le modèle reçoit surtout la **description** : « Donne les horaires pour un jour… »

## Le film en 4 scènes

1. Le client demande quelque chose.  
2. Le modèle choisit un outil (ou répond direct s'il n'en a pas besoin).  
3. Ton site exécute l'outil pour de vrai.  
4. Tu renvoies le résultat ; le modèle formule la réponse.

On appelle parfois ça « function calling » ou « tool calling ». En français : **appel d'outil**.

## Bien décrire un outil (très important)

Mauvaise description : « récupère des infos ».  
Bonne description : « Retourne les horaires d'ouverture pour un jour de la semaine (lundi à dimanche). »

Le modèle lit ça comme un mode d'emploi. Vague = il se trompe.

## Combien d'outils au début ?

**2 ou 3**, pas 20.  
Exemples :

- horaires ;
- délai devis ;
- chercher dans la FAQ.

Quand ça marche, tu en ajoutes. Pas avant.

## Ce qu'il ne faut pas mettre dans le tiroir

- envoyer un e-mail sans validation ;
- payer ;
- SQL libre sur toute la base ;
- « faire n'importe quoi sur le serveur ».

Pour le sensible : brouillon + **toi** qui valides.

## Mini cas : délai de devis

```python
def get_delai_devis(type_prestation: str) -> str:
    """Délai indicatif de devis : vitrine, boutique ou audit."""
    delais = {
        "vitrine": "3 à 5 jours ouvrés",
        "boutique": "5 à 10 jours ouvrés",
        "audit": "sous 48 h pour l'audit gratuit par e-mail",
    }
    return delais.get(type_prestation.strip().lower(), "type inconnu")
```

Question : « Pour une vitrine, le devis arrive quand ? »  
L'agent doit appeler cet outil, lire `3 à 5 jours ouvrés`, et répondre avec ça. Pas inventer « demain matin ».

## Checklist ultra courte

- [ ] outil utile pour une vraie question client  
- [ ] description claire en français  
- [ ] liste fermée d'outils (allowlist)  
- [ ] message d'erreur lisible si ça casse  
- [ ] tu as testé l'outil **sans** le modèle d'abord  

## En résumé

Les outils, ce sont les mains.  
Le modèle demande ; ton site exécute ; le modèle répond avec le résultat.  
Peu d'outils, bien décrits, droits limités.

Ensuite : la **boucle** penser / agir / observer - pour enchaîner sans se perdre.

---

## Questions fréquentes (FAQ)

**Appel d'outil = agent ?**  
C'est une brique. L'agent, c'est quand on enchaîne et qu'on regarde le résultat plusieurs fois.

**Combien d'outils ?**  
2 ou 3 pour démarrer. Sinon le modèle se perd.

**Le modèle voit mon code secret ?**  
Non. Il voit le mode d'emploi que tu lui donnes. Toi tu exécutes derrière.

**Et s'il invente un outil ?**  
Tu refuses. Tu lui renvoies « outil inconnu ». Tu améliores la liste.

**Tout doit passer par un outil ?**  
Non. Reformuler une phrase : pas besoin. Lire le stock : oui.

---

## Navigation dans la série

- Précédent : [Agents IA : c'est quoi, au juste ?](/blog/articles/agents-hf-quest-ce-qu-un-agent.html)
- Suivant : [La boucle : penser, agir, observer](/blog/articles/agents-hf-react-pensee-action-observation.html)
