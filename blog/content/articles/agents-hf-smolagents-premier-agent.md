---
title: "Ton premier agent (pas à pas)"
date: 2026-10-06
excerpt: "Installer, brancher un petit outil, lancer : un premier agent sans usine à gaz."
type: tutorial
tags: [agents IA, smolagents, formation, débutant, Hugging Face]
series: hf-agents-serie
series_order: 4
og_image: agents-hf-smolagents-premier-agent-1200x630.jpg
---

# Ton premier agent (pas à pas)

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/agents-hf-smolagents.svg" alt="Schéma : préparer, un outil, l'agent, on lance" class="schema-inline" width="800" />
  <figcaption>Quatre étapes : préparer, un outil, l'agent, on lance.</figcaption>
</figure>

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/agents-hf-smolagents-illustration.jpg" alt="Illustration pas à pas premier agent" class="schema-inline" width="800" loading="lazy" />
  <figcaption>Installer, outil, brancher, lancer - le mode d'emploi visuel.</figcaption>
</figure>

Assez de théorie. On va faire tourner quelque chose de simple.  
On utilise **smolagents** (bibliothèque Hugging Face), parce que c'est pensé pour débuter. Tu peux suivre l'esprit du [cours Agents HF](https://huggingface.co/learn/agents-course) sans recopier leurs leçons.

## Objectif de cet article

À la fin, tu as :

1. un petit outil (une fonction Python) ;
2. un agent qui peut l'utiliser ;
3. une trace lisible (ce qu'il a fait).

Pas un robot qui gère ta boîte. Juste la tuyauterie.

## Ce qu'il te faut

- Python (idéalement 3.10+)
- un environnement virtuel
- 30 à 45 minutes
- un accès à un modèle (souvent via API - suis la doc smolagents du moment)

```bash
pip install smolagents
```

## Étape 1 : un outil bête (volontairement)

```python
def average(nums: list[float]) -> float:
    """Calcule la moyenne d'une liste de nombres."""
    if not nums:
        return 0.0
    return sum(nums) / len(nums)
```

Pourquoi un calcul idiot ? Pour valider le branchement **sans** te noyer dans un CRM.

## Étape 2 : créer l'agent

```python
from smolagents import CodeAgent, HfApiModel

# Adapte selon ta config réelle (token, modèle…)
model = HfApiModel()
agent = CodeAgent(tools=[average], model=model)

result = agent.run("Quelle est la moyenne de 10, 12 et 17 ?")
print(result)
```

Sous le capot : il peut écrire un peu de code, appeler `average`, lire le résultat, répondre.  
C'est la boucle « agir / observer » en vrai.

## Étape 3 : version boutique

```python
def get_horaires_boutique(jour: str) -> str:
    """Retourne les horaires pour un jour (ex. samedi)."""
    data = {"samedi": "10h-17h", "dimanche": "ferme", "lundi": "ferme"}
    return data.get(jour.strip().lower(), "jour inconnu")

agent = CodeAgent(tools=[get_horaires_boutique], model=model)
print(agent.run("Est-ce que vous ouvrez samedi ?"))
```

Si la réponse cite `10h-17h` : bien.  
Si elle invente `9h-19h` : regarde la trace - outil non appelé, ou résultat ignoré.

## Ce que tu vérifies (checklist)

- [ ] le bon outil est choisi  
- [ ] le résultat de l'outil apparaît dans la logique de réponse  
- [ ] ça ne tourne pas en boucle 15 fois  
- [ ] un « jour inconnu » renvoie une erreur claire  

## Attention sécurité (version courte)

Un agent qui exécute du code, c'est pratique… et risqué.  
En local pour apprendre : OK.  
Dès que des inconnus y ont accès : limite les droits, timeouts, et préfère souvent des outils « liste fermée » (on compare juste après).

## En résumé

1. Un outil.  
2. Un agent.  
3. Une question.  
4. Tu lis ce qu'il a vraiment fait.

Ensuite : deux styles d'action - **code libre** vs **appel d'outil contrôlé**.

---

## Questions fréquentes (FAQ)

**smolagents, c'est obligatoire ?**  
Non. C'est un bon chemin pour apprendre. D'autres frameworks existent.

**Faut-il un PC avec carte graphique ?**  
Pas forcément. Beaucoup de tests passent par une API.

**Ça marche du premier coup en prod ?**  
Non. C'est pour apprendre et prototyper. Ensuite tu durcis (droits, logs, tests).

**Je peux mettre plusieurs outils ?**  
Oui. Commence avec un seul pour lire la trace facilement.

---

## Navigation dans la série

- Précédent : [La boucle : penser, agir, observer](/blog/articles/agents-hf-react-pensee-action-observation.html)
- Suivant : [Code libre ou outil contrôlé : comment choisir ?](/blog/articles/agents-hf-code-agents-vs-tool-calling.html)
