---
title: "La boucle : penser, agir, observer"
date: 2026-10-05
excerpt: "Le rythme d'un agent expliqué simplement : il réfléchit, il agit avec un outil, il lit le résultat, puis il répond."
type: tutorial
tags: [agents IA, ReAct, formation, débutant, Hugging Face]
series: hf-agents-serie
series_order: 3
og_image: agents-hf-react-pensee-action-observation-1200x630.jpg
---

# La boucle : penser, agir, observer

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/agents-hf-react.svg" alt="Schéma : penser, agir, observer, répondre" class="schema-inline" width="800" />
  <figcaption>Quatre temps : penser, agir, observer, répondre (ou recommencer).</figcaption>
</figure>

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/agents-hf-react-illustration.jpg" alt="Illustration de la boucle penser agir observer répondre" class="schema-inline" width="800" loading="lazy" />
  <figcaption>La boucle en images - le rythme de l'agent.</figcaption>
</figure>

Tu as un cerveau (le modèle) et des outils. Il manque le **rythme**.  
Comment enchaîne-t-il sans partir en vrille ?

On appelle souvent ça **ReAct**. Oublie le nom une seconde. Garde l'image : **penser → agir → regarder → (recommencer) → répondre**.

Toujours dans l'esprit du [cours Agents Hugging Face](https://huggingface.co/learn/agents-course), en français simple.

## Les 3 temps (vraiment)

### 1. Penser
« Il me faut les horaires du samedi. »

### 2. Agir
Il appelle l'outil horaires avec `jour = samedi`.

### 3. Observer
L'outil répond : `10h-17h`.

S'il a assez d'infos → il répond au client.  
Sinon → il repense et rappelle un autre outil (délai devis, stock…).

## Pourquoi c'est mieux qu'un gros blabla

Sans boucle, le modèle invente souvent.  
Avec boucle + outils, il s'appuie sur des **faits** que ton site a renvoyés.

Ce n'est pas parfait. Mais c'est déjà autre chose qu'un chat qui rêve.

## Une petite trace (à lire comme une BD)

```text
Penser : je dois vérifier le stock du produit X-42.
Agir    : check_stock(sku="X-42")
Observer: stock = 3
Penser  : ok, on peut confirmer.
Répondre: Oui, il reste 3 pièces.
```

Autre exemple :

```text
Penser : question sur samedi + délai devis vitrine.
Agir    : get_horaires(jour="samedi")
Observer: 10h-17h
Agir    : get_delai_devis(type="vitrine")
Observer: 3 à 5 jours ouvrés
Répondre: Oui, samedi 10h-17h. Devis vitrine : 3 à 5 jours ouvrés.
```

Tu n'as pas besoin d'afficher tout ça au client. Toi, en coulisse, tu le **logs**. Ça sert à comprendre les erreurs.

## Les garde-fous (indispensables)

- **Nombre max d'étapes** (ex. 5) : sinon ça tourne en boucle.
- **Liste d'outils fermée** : pas d'invention.
- **Résultat d'outil court et clair** : pas un pavé HTML de 200 pages.
- **Erreur honnête** : « service indisponible » plutôt qu'un silence.

## Analogie

C'est comme un apprenti au comptoir :

1. il écoute ;
2. il va chercher l'info sur le tableau des horaires ;
3. il revient ;
4. il te répond.

S'il doit aussi regarder le carnet des devis, il fait un deuxième aller-retour.  
Toi, tu limites le nombre d'allers-retours, sinon le client attend trop longtemps.

## Lien avec la suite

Les frameworks (smolagents, etc.) font souvent cette boucle pour toi.  
Si tu comprends ces 3 temps, tu sauras **lire une trace** et corriger : mauvais outil, mauvaise description, ou observation illisible.

## En résumé

Penser, agir, observer, répondre.  
C'est le métronome de l'agent.  
Sans ça, tu as juste un chat. Avec ça + de bons outils, tu as un vrai petit processus.

Prochaine étape : lancer un **premier agent** concret (smolagents), encore pas à pas.

---

## Questions fréquentes (FAQ)

**ReAct, je dois retenir le nom ?**  
Pas forcément. Retiens la boucle : penser / agir / observer.

**Faut-il montrer la « pensée » au client ?**  
En général non. Tu la gardes dans tes logs.

**Ça empêche toutes les inventions ?**  
Non. Mais ça en réduit beaucoup si tes outils disent vrai.

**Combien d'étapes max ?**  
Pour une question simple : 3 à 5. Au-delà, regarde ton design.

**Et s'il rappelle le même outil en boucle ?**  
Coupe (max steps) et corrige la description de l'outil.

---

## Navigation dans la série

- Précédent : [Les outils : donner des mains au modèle](/blog/articles/agents-hf-outils-et-function-calling.html)
- Suivant : [Ton premier agent (pas à pas)](/blog/articles/agents-hf-smolagents-premier-agent.html)
