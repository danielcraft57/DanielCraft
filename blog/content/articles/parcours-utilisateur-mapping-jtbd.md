---
title: "Le chemin de l'utilisateur : étapes et freins"
date: 2025-09-16
excerpt: "User flows, journey map et JTBD — pour voir où ça coince vraiment."
type: article
tags: [UX, parcours, journey map, JTBD, produit]
series: ux-ui-serie
series_order: 5
og_image: parcours-utilisateur-mapping-jtbd-1200x630.jpg
---

# Le chemin de l'utilisateur : étapes et freins

Un produit échoue rarement parce qu'un bouton est « moche ». Il échoue parce que le parcours est confus : trop d'étapes, mauvais ordre, informations manquantes, ou anxiété - « est-ce que c'est bien pris en compte ? ». Cartographier un parcours, c'est rendre visible ce qui est habituellement implicite. Et donc pouvoir l'améliorer sans se battre à l'aveugle.

User flow, journey map, Jobs To Be Done : trois outils complémentaires. Pas trois religions. Tu les combines selon le risque et le contexte.

## User flow : le minimum vital

Un user flow, c'est un schéma d'étapes. Point d'entrée. Décisions (« si connecté / si pas connecté »). Étapes. Sortie - objectif atteint. Il sert à aligner produit, design et dev, à repérer les dépendances (auth, paiement, permissions), à définir le happy path et les erreurs majeures.

La règle d'or : un flow efficace tient sur une page. S'il déborde, tu as probablement trop de branches - ou tu n'as pas encore tranché. Un flow n'est pas une encyclopédie. C'est une carte pour décider.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/parcours-jtbd.svg" alt="Schéma JTBD : situation, motivation, résultat" class="schema-inline" width="640" />
  <figcaption>JTBD : quand [situation], je veux [motivation], afin de [résultat] - le job guide le parcours, pas l'inverse.</figcaption>
</figure>

Quand tu le dessines, force-toi à nommer les étapes avec des verbes : choisir, renseigner, valider, payer. Les noms d'écrans (« Dashboard », « Modal X ») masquent les décisions. Les verbes les exposent.

## Journey map : l'expérience au-delà de l'écran

La journey map ajoute ce que le flow ignore souvent : les émotions (stress, confiance, doute), le contexte (mobile dans les transports, bureau, client en face), les canaux (mail, SMS, app, support). Elle devient indispensable quand l'expérience dépasse l'écran - onboarding, relances, support - ou quand la confiance est un enjeu (paiement, données sensibles).

Exemple simple. Écran : « Crée ton compte ». Émotion : « je me méfie, je ne veux pas de spam ». Décision [UX](/blog/articles/ux-ui-fondamentaux-differences.html) : expliquer clairement l'usage de l'email, rassurer, montrer la valeur avant d'exiger dix champs. Sans la couche émotionnelle, tu optimises un formulaire. Avec, tu réduis une peur.

Tu n'as pas besoin d'un mur de post-its colorés. Une ligne d'étapes, une ligne d'émotions, une ligne d'opportunités - ça suffit pour une conversation utile.

## JTBD : le travail à accomplir

Jobs To Be Done aide à éviter de raisonner en features. La formule : « Quand [situation], je veux [motivation], afin de [résultat]. » Exemple : « Quand je prépare un devis pour un client pressé, je veux générer une proposition claire en trois minutes, afin de répondre vite et ne pas perdre l'opportunité. »

Le « job » guide l'ordre des étapes, les informations essentielles, les compromis - moins de champs, plus de guidance. Tu arrêtes de demander « quelles features veulent-ils ? » pour demander « quel progrès essaient-ils de faire ? ». Ça change le backlog. Ça change aussi les débats : une feature « cool » qui n'aide pas le job descend dans la pile.



<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/parcours-emotion.svg" alt="Schema parcours utilisateur avec points de friction" class="schema-inline" width="640" />
  <figcaption>Le journey map sert a voir ou ca fait mal — pas a faire joli.</figcaption>
</figure>

Le schéma situation → motivation → résultat n'est pas magique. C'est un filtre. Si tu ne peux pas écrire le job en une phrase claire, tu ne sais probablement pas encore pour qui tu conçois.

## Du flow aux écrans (sans se perdre)

Une méthode simple. Liste les étapes du flow en verbes. Pour chaque étape, pose deux questions : qu'est-ce que l'utilisateur doit décider ? Quelles infos lui manquent ? Dessine un [wireframe](/blog/articles/wireframes-prototypage-fidelite.html) par étape. Ajoute les états : loading, vide, erreur, succès.

Tu construis un parcours orienté décision, pas une suite de pages. Beaucoup de frictions naissent d'écrans qui « montrent tout » au lieu de guider une décision à la fois.

## Frictions à chercher en priorité

Les sauts de contexte - demander une info trop tôt, comme le paiement avant la valeur. Les étapes inutiles - confirmations doubles, écrans de transition vides. L'anxiété - pas de feedback, pas d'aperçu, pas de « ce qui va se passer ensuite ». Les erreurs tardives - validation uniquement à la fin, avalanche de messages.

Ces points reviennent presque partout. Cherche-les avant de polir les [micro-interactions](/blog/articles/micro-interactions-feedback-etats.html).

## Mesurer sans usine à gaz

Même sans gros outillage, quelques indicateurs orientent : taux de complétion du parcours, temps moyen pour accomplir la tâche, drop-off par étape, nombre de retours en arrière. Ce n'est pas une science exacte. C'est une boussole. Elle te montre où creuser - et si une refonte de parcours a vraiment aidé, ou si tu as juste embelli le même embouteillage.

## Aligner l'équipe autour d'une carte

Le vrai pouvoir d'un parcours, ce n'est pas le diagramme. C'est la conversation qu'il force. Produit, design, tech, parfois support ou commercial : tout le monde voit les mêmes étapes, les mêmes trous, les mêmes angoisses. Tu découvres qu'une étape « évidente » pour le métier est opaque pour l'utilisateur. Tu découvres qu'une dépendance technique (auth, paiement) a été oubliée dans le flow. Tu découvres qu'une relance mail arrive trop tôt - ou jamais.

Fais une session courte. Une heure. Flow sur un tableau, JTBD en haut de page, deux ou trois moments émotionnels clés. Sors avec des décisions : quoi couper, quoi réordonner, quoi rassurer. Si la carte ne change pas le backlog, elle n'a servi à rien. Et si vous n'êtes pas d'accord sur le job, arrêtez-vous là : designer un parcours sans accord sur le « pourquoi », c'est décorer un désaccord. Mieux vaut une heure de friction en équipe qu'un mois de friction utilisateur.

## Un bon parcours guide, il n'étale pas

Un bon parcours n'est pas celui qui montre tout. C'est celui qui mène l'utilisateur vers son objectif en réduisant le nombre de décisions, l'incertitude et la charge mentale. User flows pour la structure, journey maps pour le vécu, JTBD pour le « pourquoi ». Trois outils. Une intention : moins de friction, plus de progrès réel pour la personne en face de l'écran. Le reste - couleurs, animations, détails UI - vient après, quand le chemin tient déjà debout.
