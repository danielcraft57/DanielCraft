---
title: "Voir ce que fait ton agent"
date: 2026-10-10
excerpt: "Traces, erreurs, petits tests : comment savoir pourquoi l'agent a répondu n'importe quoi."
type: tutorial
tags: [agents IA, observabilité, tests, formation, débutant]
series: hf-agents-serie
series_order: 8
og_image: agents-hf-observabilite-evaluation-1200x630.jpg
---

# Voir ce que fait ton agent

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/agents-hf-observability.svg" alt="Schéma : traces, mesures, tests, améliorer" class="schema-inline" width="800" />
  <figcaption>Sans traces, tu voles à l'aveugle.</figcaption>
</figure>

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/agents-hf-observability-illustration.jpg" alt="Illustration traces mesures tests améliorer" class="schema-inline" width="800" loading="lazy" />
  <figcaption>Voir, mesurer, tester, corriger.</figcaption>
</figure>

La démo marche. Super.  
Puis un client tombe sur une réponse bizarre… et tu ne sais pas pourquoi.

Ce chapitre (esprit bonus du [cours Agents HF](https://huggingface.co/learn/agents-course)) est le plus utile en vrai : **regarder**.

## En une phrase

Tu enregistres ce que l'agent a fait (outils, résultats, réponse), tu mesures les échecs, tu corriges.

## Quoi logger (minimum vital)

Pour chaque question :

- la question du client ;
- chaque outil appelé + arguments ;
- le résultat renvoyé (même en erreur) ;
- la réponse finale ;
- le nombre d'étapes ;
- le temps écoulé.

Sans ça, « il a halluciné » reste une légende de Slack.

## Trois mesures simples

1. **Taux d'outils OK** (succès / échec)  
2. **Nombre d'étapes moyen**  
3. **« Je ne sais pas »** propre quand l'info manque  

Ajoute une revue humaine sur 10-20 messages par semaine. Cinq minutes, gros gain.

## Comment améliorer sans tout casser

Regarde les échecs d'abord :

- description d'outil floue ?  
- résultat illisible ?  
- trop d'outils ?  
- trop d'étapes autorisées ?

Corrige le contrat des outils **avant** de changer de modèle.

## Mini routine hebdo

1. Exporte 20 conversations.  
2. Classe : OK / douteux / faux.  
3. Pour les faux : ouvre la trace.  
4. Une correction (outil ou prompt), pas dix.

## En résumé

Si tu ne vois pas la trace, tu ne pilotes pas.  
Logs + petits tests + revue humaine = agent qui progresse.

Suite (bonus) : parfois le modèle se trompe trop souvent d'outil - on peut l'**entraîner** un peu pour ça.

---

## Questions fréquentes (FAQ)

**Quoi logger en priorité ?**  
Outil + arguments + résultat + réponse finale + nombre d'étapes.

**L'éval auto suffit ?**  
Non seule. Garde un œil humain sur un échantillon.

**Ça coûte cher ?**  
Moins cher qu'un client furieux. Commence léger.

---

## Navigation dans la série

- Précédent : [Chercher dans ta doc, puis répondre](/blog/articles/agents-hf-rag-agentique.html)
- Suivant : [Mieux appeler les outils (fine-tune)](/blog/articles/agents-hf-finetune-function-calling.html)
