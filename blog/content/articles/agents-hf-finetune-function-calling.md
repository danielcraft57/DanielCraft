---
title: "Mieux appeler les outils (fine-tune)"
date: 2026-10-11
excerpt: "Quand le modèle se trompe trop souvent d'outil : on lui montre des exemples corrects avant d'espérer un miracle."
type: tutorial
tags: [agents IA, fine-tuning, outils, formation, débutant]
series: hf-agents-serie
series_order: 9
og_image: agents-hf-finetune-function-calling-1200x630.jpg
---

# Mieux appeler les outils (fine-tune)

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/agents-hf-finetune-fc.svg" alt="Schéma : exemples, entraînement, tests, agent plus fiable" class="schema-inline" width="800" />
  <figcaption>D'abord de bons exemples, ensuite seulement l'entraînement.</figcaption>
</figure>

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/agents-hf-finetune-illustration.jpg" alt="Illustration fine-tune appels d'outils" class="schema-inline" width="800" loading="lazy" />
  <figcaption>Exemples → entraînement → tests → agent plus fiable.</figcaption>
</figure>

Parfois le modèle comprend la question… mais rate l'outil : mauvais nom, mauvais argument, outil inventé.  
Avant de « fine-tuner », tu as déjà corrigé les descriptions ? Si non : recommence là.

Ce bonus du [cours Agents HF](https://huggingface.co/learn/agents-course) sert **après** un bon design d'outils.

## En une phrase

Tu montres au modèle plein d'exemples d'**appels d'outils corrects**, pour qu'il se trompe moins.

## Quand ça vaut le coup

- tes outils sont très métier (devis, stock maison) ;
- malgré de bonnes descriptions, il se trompe souvent ;
- tu as des logs d'échecs réels à transformer en exemples.

## Quand ça ne vaut pas le coup

- 2 outils génériques et un prompt bancal ;
- tu n'as pas encore de traces ;
- tu espères que l'entraînement remplacera une FAQ pourrie.

## L'idée des exemples

Tu construis des conversations du type :

1. question client ;  
2. bon appel d'outil ;  
3. résultat ;  
4. bonne réponse finale.

Tu ajoutes aussi des cas « pas besoin d'outil » et des cas « outil en erreur ».

## Méthode simple

1. Liste les erreurs réelles.  
2. Écris la version correcte.  
3. Entraîne / adapte (souvent avec une méthode légère type LoRA - vu dans la série LLM).  
4. Rejoue ton jeu de tests gelé.

## En résumé

Fine-tune = rattrapage du cerveau.  
Ça ne remplace ni les garde-fous, ni les traces, ni une doc propre.

Ensuite : **LangGraph** - dessiner le parcours (si devis → humain, sinon réponse).

---

## Questions fréquentes (FAQ)

**Prompting d'abord ?**  
Oui. Toujours.

**Combien d'exemples ?**  
Des centaines propres battent des milliers de lignes sales.

**Ça remplace la boucle ?**  
Non. Ça aide le choix d'outil. La boucle reste.

---

## Navigation dans la série

- Précédent : [Voir ce que fait ton agent](/blog/articles/agents-hf-observabilite-evaluation.html)
- Suivant : [Un parcours en étapes (LangGraph)](/blog/articles/agents-hf-langgraph-premier-graphe.html)
