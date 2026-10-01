---
title: "Code libre ou outil contrôlé : comment choisir ?"
date: 2026-10-07
excerpt: "Deux façons d'agir : laisser le modèle écrire du code, ou l'obliger à appeler un outil précis. Le choix dépend du risque."
type: tutorial
tags: [agents IA, formation, débutant, smolagents, sécurité]
series: hf-agents-serie
series_order: 5
og_image: agents-hf-code-agents-vs-tool-calling-1200x630.jpg
---

# Code libre ou outil contrôlé : comment choisir ?

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/agents-hf-code-vs-json.svg" alt="Schéma : code agent vs appel d'outil contrôlé" class="schema-inline" width="800" />
  <figcaption>À gauche plus souple, à droite plus sûr.</figcaption>
</figure>

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/agents-hf-code-vs-json-illustration.jpg" alt="Illustration code libre versus outil contrôlé" class="schema-inline" width="800" loading="lazy" />
  <figcaption>Deux styles d'action : souplesse ou contrôle.</figcaption>
</figure>

Ton premier agent tourne. Bien.  
Maintenant la vraie question : **comment** lui permettre d'agir ?

Il y a deux grandes familles (vues aussi dans le [cours Agents HF](https://huggingface.co/learn/agents-course)) :

1. **Code libre** : le modèle écrit un petit programme, on l'exécute.  
2. **Outil contrôlé** : le modèle choisit un outil dans une liste, avec des arguments précis.

## Analogie

**Code libre** = tu donnes un atelier complet à l'apprenti.  
**Outil contrôlé** = tu lui donnes seulement 3 boutons sur le comptoir.

Les deux peuvent servir. Pas pour les mêmes moments.

## Style 1 : code libre (CodeAgent)

Le modèle peut faire des calculs, enchaîner des étapes, bricoler.  
Pratique pour explorer.  
Risqué si la « sandbox » (zone d'exécution) est trop ouverte.

Bon pour : atelier, analyse légère, apprentissage.  
Mauvais pour : envoyer des mails, toucher la caisse, droits admin.

## Style 2 : outil contrôlé (souvent JSON)

Le modèle répond en substance :  
« appelle `get_horaires` avec jour=samedi ».

Ton serveur :

1. vérifie que l'outil est autorisé ;
2. vérifie les arguments ;
3. exécute ;
4. renvoie le résultat.

Bon pour : horaires, stock, FAQ, parcours client.  
Moins souple si tu n'as pas prévu le bon outil.

## Tableau simple

| Besoin | Piste |
|--------|--------|
| Question boutique simple | Outil contrôlé |
| Calcul / exploration | Code libre (sandbox) |
| Conformité / audit | Outil contrôlé |
| Apprendre les agents | Les deux, en lab |

## Règle pratique DanielCraft

Pour un commerce : **outils contrôlés** d'abord.  
Pour un lab perso : code libre OK, derrière une barrière.

## En résumé

Souplesse vs contrôle.  
Tu choisis selon le risque, pas selon la mode.

Ensuite : trois « boîtes à outils » (frameworks) - laquelle ouvrir selon ton cas.

---

## Questions fréquentes (FAQ)

**Lequel est « mieux » ?**  
Ni l'un ni l'autre. Ça dépend du risque.

**Code libre = danger ?**  
Oui sans limites. Non si tu enfermes bien l'exécution.

**Les chats classiques font quoi ?**  
Souvent de l'appel d'outil contrôlé.

**Je peux mixer ?**  
Oui. Beaucoup de stacks finissent mixtes. Au début, choisis une voie claire.

---

## Navigation dans la série

- Précédent : [Ton premier agent (pas à pas)](/blog/articles/agents-hf-smolagents-premier-agent.html)
- Suivant : [Trois boîtes à outils : laquelle choisir ?](/blog/articles/agents-hf-frameworks-llamaindex-langgraph.html)
