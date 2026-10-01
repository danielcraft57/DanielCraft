---
title: "Chercher dans ta doc, puis répondre"
date: 2026-10-09
excerpt: "L'agent va chercher dans ta FAQ avant de parler. Simple idée, gros gain de confiance."
type: tutorial
tags: [agents IA, RAG, FAQ, formation, débutant]
series: hf-agents-serie
series_order: 7
og_image: agents-hf-rag-agentique-1200x630.jpg
---

# Chercher dans ta doc, puis répondre

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/agents-hf-rag.svg" alt="Schéma : question, recherche, vérification, réponse" class="schema-inline" width="800" />
  <figcaption>Question → recherche → (autres outils) → réponse avec sources.</figcaption>
</figure>

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/agents-hf-rag-illustration.jpg" alt="Illustration chercher dans la doc puis répondre" class="schema-inline" width="800" loading="lazy" />
  <figcaption>Chercher dans ta FAQ avant de parler - en image.</figcaption>
</figure>

Tu as une FAQ. Des fiches. Des pages « délais », « livraison », « allergènes ».  
Un chat nu invente.  
Un agent utile **va d'abord chercher** dans ta doc.

On parle souvent de **RAG** : récupérer des passages, puis générer une réponse.  
**RAG agentique** : l'agent décide *quand* chercher, *quoi* chercher, parfois plusieurs fois.  
Idée au cœur du [cours Agents HF](https://huggingface.co/learn/agents-course) - ici en version terrain.

## En une phrase

L'agent traite ta documentation comme un **outil de recherche**, pas comme un décor.

## Exemple fromagerie (fictif, Grand Est)

Question : « Vous serez au marché samedi, et y'a un panier sans lactose ? »

L'agent peut :

1. chercher « marché samedi » dans la FAQ ;  
2. chercher « sans lactose / allergènes » ;  
3. répondre en citant les passages.

Sans ça, il invente un marché qui n'existe pas.

## RAG simple vs RAG « qui réfléchit »

**Simple** : toujours la même recherche, puis une réponse.  
**Agentique** : parfois 2 recherches, parfois un autre outil (horaires), parfois « je n'ai pas trouvé ».

Plus puissant. Aussi plus cher / plus lent. À utiliser quand la question a plusieurs étapes.

## La qualité de ta doc compte plus que le modèle

FAQ confuse = réponses confuses.  
Avant d'indexer 2 Go de fichiers :

- pages à jour ;
- titres clairs ;
- une info = un endroit ;
- pas les dossiers RH mélangés à la FAQ publique.

## Règle d'or

Si la recherche ne trouve rien : l'agent doit le **dire**.  
Mieux vaut « je n'ai pas trouvé dans la FAQ à jour - guette voir avec nous au magasin » qu'une livraison inventée.

## En résumé

Cherche d'abord, réponds ensuite.  
Cite ta source.  
Garde ta FAQ propre.

Ensuite : **comment voir** ce que l'agent fait vraiment (traces, tests).

---

## Questions fréquentes (FAQ)

**RAG = agent ?**  
Non. RAG est une technique de recherche + réponse. L'agent peut s'en servir comme outil.

**Toujours meilleur en mode agentique ?**  
Non. Pour une FAQ simple, un retrieve unique suffit souvent.

**Faut-il citer les sources ?**  
Oui, surtout face client. Ça crée de la confiance.

---

## Navigation dans la série

- Précédent : [Trois boîtes à outils : laquelle choisir ?](/blog/articles/agents-hf-frameworks-llamaindex-langgraph.html)
- Suivant : [Voir ce que fait ton agent](/blog/articles/agents-hf-observabilite-evaluation.html)
