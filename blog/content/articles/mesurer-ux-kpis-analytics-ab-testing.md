---
title: "Mesurer l'expérience : chiffres utiles (pas de vanité)"
date: 2025-10-02
excerpt: "KPIs, analytics et A/B testing : une boucle pour apprendre, pas pour se mentir."
type: article
tags: [UX, analytics, KPI, A/B testing, produit]
series: ux-ui-serie
series_order: 10
og_image: mesurer-ux-kpis-analytics-ab-testing-1200x630.jpg
---

# Mesurer l'expérience : chiffres utiles (pas de vanité)

Améliorer l'[UX](/blog/articles/ux-ui-fondamentaux-differences.html) sans mesure, c'est possible - jusqu'à un certain point. Sans données, tu ne sais pas si la friction est réelle ou juste ressentie en interne, si une amélioration marche pour 10 % ou pour 90 %, si tu as déplacé le problème ailleurs. Mais mesurer n'est pas empiler des dashboards. L'objectif, c'est de meilleures décisions.

La boucle utile est courte : mesurer, apprendre, itérer. Pas « tout tracker ». Choisir des indicateurs qui reflètent la réussite utilisateur, comprendre pourquoi ça casse, corriger, re-mesurer.

## Les pièges : vanity metrics et fausses certitudes

Pages vues sans contexte. Temps passé - parfois signe d'intérêt, parfois signe de friction. « Engagement » flou. Ces chiffres rassurent. Ils orientent mal.

La question clé : quelle action représente une réussite utilisateur ? Activation, devis envoyé, paiement confirmé, tâche accomplie sans support. Tout le reste est second. Si tu ne peux pas nommer le succès, tu mesures du bruit.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/ux-kpis-boucle.svg" alt="Schéma de la boucle UX : mesurer, apprendre, itérer" class="schema-inline" width="640" />
  <figcaption>Mesurer → apprendre → itérer : une boucle courte bat un dashboard que personne ne lit.</figcaption>
</figure>

Autre piège : conclure trop vite sur un échantillon minuscule, ou confondre corrélation et cause. Un pic de conversion après une release n'est pas forcément dû au bouton bleu. Regarde la saisonnalité, le trafic, les bugs simultanés. L'humilité analytique fait gagner du temps.

## Les métriques UX qui servent

Sur un parcours : taux de complétion, temps pour réussir, drop-off par étape, erreurs (fréquence et type), retours arrière. Si tu peux : tickets support liés au parcours, CSAT ou question ciblée juste après l'action - pas un NPS global qui mélange tout.

Ces indicateurs te disent où ça casse. Ils ne te disent pas toujours pourquoi. C'est normal. Le quanti localise. Le quali explique. Tu as besoin des deux pour itérer sans te tromper de problème.

## Instrumentation minimale : cinq événements bien choisis

Tu n'as pas besoin de 200 events. Pour un funnel simple : `funnel_start`, étapes complétées, `success`, `error` avec un type. Ajoute source (mobile/web), variant si A/B, parfois un bucket de latence si la perf compte.

L'idée : diagnostiquer sans espionner. Moins d'événements, mieux nommés, documentés. Un dictionnaire d'events à jour vaut mieux qu'un lac de données que personne ne comprend. Et respecte le consentement et le minimum utile - mesurer l'UX n'excuse pas de tout collecter.

## Funnels et cohortes

Le funnel montre où les gens sortent. La cohorte montre comment le comportement évolue dans le temps - nouveaux vs anciens, avant/après une release. Souvent l'amélioration n'est pas « +10 % global » mais « +25 % mobile, +5 % desktop ». Sans segmentation, tu rates l'essentiel et tu moyennes des réalités différentes.

Regarde aussi les erreurs par étape. Un drop-off peut être un abandon volontaire - ou un mur technique. Les codes d'erreur et les messages affichés t'aident à trancher avant de « redesign » au hasard.



<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/ux-ab-loop.svg" alt="Schema de la boucle A/B testing UX" class="schema-inline" width="640" />
  <figcaption>A/B utile seulement si l'hypothese et la metrique sont fixees avant.</figcaption>
</figure>

## Quali + quanti : le duo

Chiffres : où. [Tests utilisateurs](/blog/articles/ux-recherche-utilisateur-interviews-tests.html) : pourquoi. Méthode efficace : repérer un drop-off, faire cinq tests ciblés sur cette étape, corriger, re-mesurer. Boucle courte. Moins de débats de salle. Plus de preuves.

Les interviews et le support enrichissent aussi. Un verbatim récurrent + un pic d'erreur sur le même champ, c'est une priorité - pas une opinion. Documente le lien « signal quanti → insight quali → correctif » pour que l'équipe voie la boucle, pas seulement le ticket.

## A/B testing : utile, pas magique

Utile quand tu as du trafic suffisant, un impact mesurable, peu de variables. Dangereux ou inutile quand le bug UX est évident, ou quand le trafic est trop faible pour conclure autre chose que du hasard.

Avant un A/B, un test utilisateur explique souvent plus vite. L'A/B valide à l'échelle. Il ne remplace pas la compréhension. Et un A/B mal cadré (trop de changements à la fois, métrique de succès floue, arrêt trop tôt) te donne une « victoire » que tu ne sauras pas reproduire.

Garde une métrique primaire, quelques gardes-fous (erreurs, support, perf), une durée minimale. Sinon tu optimises le vanity du test lui-même.

## KPIs propres par type de feature

Onboarding : activation (action clé atteinte), temps pour y arriver, support lié à l'inscription. Formulaire : complétion, erreurs par champ, abandon par étape. Checkout : conversion, erreur de paiement, latence. Choisis deux ou trois métriques max par surface. Au-delà, personne ne priorise.

Relie chaque KPI à une décision possible. « Si le drop-off à l'étape 2 dépasse X, on simplifie les champs. » Sinon le KPI reste un ornement de dashboard.

## Revue régulière, pas reporting de prestige

Une revue bihebdo de vingt minutes sur un parcours critique bat un reporting mensuel de quarante slides. Regarde le funnel, les top erreurs, deux verbatims support, une décision. Qui corrige quoi avant la prochaine revue. Si personne ne sort avec une action, la mesure n'a servi à rien - tu as juste regardé des graphiques.

Évite aussi de changer la définition des KPIs toutes les semaines. Stabilise un mois, observe, puis ajuste. Sinon tu compares des pommes à des oranges et tu appelles ça de l'agilité.

## Privacy et confiance

Mesurer l'UX n'excuse pas de tout collecter. Minimum utile, consentement respecté, rétention courte, pas de champs personnels dans les events si ce n'est pas nécessaire. Un bon setup analytics inspire autant confiance côté conformité que côté produit. Les équipes qui « trackent tout au cas où » finissent avec un lac illisible - et parfois un risque [RGPD](/blog/articles/conformite-rgpd-nis2-iso27001.html).

Documente ce que tu mesures et pourquoi. Ça aide l'onboarding des nouveaux, les audits, et ça force à couper les events morts.

## Mesurer pour décider, pas pour décorer

Mesurer l'UX, ce n'est pas tout tracker. C'est choisir des indicateurs de réussite utilisateur et boucler : observation (quanti), compréhension (quali), amélioration (design/dev), validation (mesure). Si tu fais ça régulièrement, tu progresses - et tu évites les débats sans fin où chacun sort son avis comme une preuve.

Commence petit : un parcours critique, cinq events, un funnel, une revue bihebdo des drop-offs. Mesurer, apprendre, itérer. Le dashboard peut attendre. La boucle, non.
