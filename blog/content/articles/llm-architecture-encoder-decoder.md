---
title: "Encoder, decoder : quelle architecture choisir ?"
date: 2026-10-03
excerpt: "Comprendre encoder, decoder et encoder-decoder sans slide illisible - pour choisir selon ton besoin."
type: tutorial
tags: ["LLM", "Transformers", "architecture", "encoder", "decoder", "formation"]
series: llm-transformers-serie
series_order: 3
og_image: llm-architecture-encoder-decoder-1200x630.jpg
---

# Encoder, decoder : quelle architecture choisir ?

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/llm-architecture.svg" alt="Schéma encoder decoder encoder-decoder" class="schema-inline" width="800" />
  <figcaption>Trois familles, un choix selon le besoin.</figcaption>
</figure>

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/llm-architecture-illustration.jpg" alt="Encoder, decoder, ou les deux." class="schema-inline" width="800" loading="lazy" />
  <figcaption>Même idée en image : choisir la bonne famille.</figcaption>
</figure>

Tu n'as pas besoin de redessiner le papier Attention Is All You Need. Tu as besoin de savoir **quoi choisir** pour ton cas. Encoder, decoder, ou les deux : trois façons d'organiser un modèle Transformers. Le nom fait un peu technique. L'idée, elle, est simple.

Cette série s'inspire du [cours LLM Hugging Face](https://huggingface.co/learn/llm-course). Le texte ici est original, en français, et on vise la clarté d'abord.

## L'idée en une phrase

- **Encoder** : comprendre / classer / extraire.
- **Decoder** : générer la suite.
- **Les deux** : lire d'un côté, écrire de l'autre (traduire, résumer).

En image mentale : l'encoder lit et range. Le decoder invente la suite. L'encoder-decoder lit une entrée, puis écrit une sortie liée.

## Pourquoi on parle d'architecture

Un Transformers, c'est une famille de modèles qui traite le texte avec de l'attention. L'attention, en français simple : le modèle regarde quels mots vont ensemble pour comprendre le sens.

L'architecture, c'est le plan de construction. Même famille, trois plans utiles :

1. la partie qui lit bien (encoder) ;
2. la partie qui écrit la suite (decoder) ;
3. les deux collées (encoder-decoder).

Tu ne choisis pas « le plus gros ». Tu choisis **la forme qui match ton besoin**.

## Encoder (comprendre)

Tu donnes un texte. Tu veux une **étiquette** ou une info structurée. Pas un roman : une décision.

Exemples :

- avis positif, neutre ou négatif ;
- mail = devis, réclamation, ou spam ;
- phrase qui parle de livraison, prix, ou horaires.

Famille connue : BERT / DistilBERT. BERT lit tout le texte d'un coup. Il est fort pour classer et extraire. DistilBERT, c'est plus léger, souvent assez bon.

Point important : un encoder ne raconte pas une longue histoire. Il te donne une représentation du texte, puis tu branches une petite tête de classification (une couche qui décide l'étiquette).

### Exemple boutique (Metz)

Tu reçois des avis Google. Tu veux trier vite : positif / négatif. Un encoder + un peu de fine-tuning, c'est souvent plus propre qu'un gros chat qui invente des phrases.

## Decoder (générer)

Tu veux du **texte qui continue** : réponse, brouillon, reformulation, idée de mail.

Famille connue : modèles type GPT. Le decoder prédit le prochain morceau, puis le suivant.

C'est puissant. Ça peut aussi inventer. Il écrit fluide même quand il n'est pas sûr. Règle : **garde une relecture** avant d'envoyer chez un client.

### Exemple boutique (Lorraine)

« Propose un mail poli pour dire que le devis arrive sous 3 jours. » Un decoder marche bien. Tu vérifies délais, ton, et numéro de téléphone avant d'envoyer.

## Encoder-decoder (les deux)

Tu as une **entrée** et une **sortie** liées. Tu ne veux pas juste « continuer » : tu veux transformer A en B.

Cas typiques : traduction, résumé d'une fiche produit, reformulation cadrée (« style boutique, 80 mots max »).

Famille connue : T5, BART. L'encoder lit. Le decoder écrit en s'appuyant sur ce qui a été compris.

Aujourd'hui, un gros decoder « instructionné » (entraîné à suivre une consigne) fait souvent le même job. Connaître l'encoder-decoder t'aide quand même à lire les fiches modèles sans te perdre.

## Comment choisir (grille simple)

Pose-toi : **qu'est-ce que je veux en sortie ?**

| Besoin | Direction | Famille typique |
|--------|-----------|-----------------|
| Classe / étiquette | Encoder | BERT, DistilBERT |
| Texte libre / chat | Decoder | GPT-like |
| Entrée → sortie liée | Encoder-decoder (ou decoder instructionné) | T5, BART, ou LLM instructionné |

Version boutique :

- « Classe mes avis 1 à 5 » → encoder.
- « Propose un mail de réponse » → decoder (avec validation).
- « Résume cette fiche produit en 3 lignes » → encoder-decoder, ou un bon modèle instructionné.

## Pièges fréquents

**Tout faire avec un gros decoder.** En démo, ça impressionne. En coût et en contrôle pour classer, pas toujours optimal.

**Croire que BERT est mort.** Non. Pour classer, ça reste solide et souvent plus léger.

**Choisir au feeling du logo.** Lis la tâche sur la fiche (model card). « text-classification » ≠ modèle de chat géant.

**Oublier la langue.** Teste avec tes vrais textes du Grand Est (avis, mails, FAQ).

## Mini parcours de décision

1. Tu classifies ? → encoder.
2. Tu génères du texte libre ? → decoder.
3. Tu transformes A en B ? → encoder-decoder, ou decoder instructionné testé.
4. Tu hésites ? → 20 exemples réels, mesure, décide.

## Lien avec la suite

Ensuite : le Hub Hugging Face (trouver modèles et datasets), puis tokenizers, fine-tuning, Gradio, LoRA.

Une fois « classer vs générer » clair, le reste devient plus digeste.

## En résumé

L'architecture suit le besoin, pas la mode.

- Classe → encoder.
- Génère → decoder.
- Transforme A en B → souvent les deux (ou un decoder bien briefé).

Garde cette grille. Elle évite déjà plein de mauvaises pistes.

---

## Questions fréquentes (FAQ)

**Je peux tout faire avec un gros decoder ?**  
Souvent oui en démo. Pas toujours optimal en coût et en contrôle pour classer. Pour une étiquette, un encoder reste un bon réflexe.

**BERT est mort ?**  
Non. Pour classer et extraire, ça reste très solide. Les chatbots ont pris la lumière, pas toute la place.

**Encoder-decoder ou decoder instructionné pour un résumé ?**  
Les deux peuvent marcher. Teste sur tes textes : qualité, coût, respect de la longueur.

**Comment savoir ce que fait un modèle sur le Hub ?**  
Lis la tâche, la langue, la taille, les exemples. Fiche vide = méfiance.

**Je dois apprendre les maths du papier Transformers ?**  
Non pour démarrer. « Lire / générer / transformer » suffit pour choisir.

---

## Navigation dans la série

- Précédent : [Pipeline](/blog/articles/llm-transformers-pipeline-premiere-inference.html)
- Suivant : [Le Hub Hugging Face](/blog/articles/llm-huggingface-hub-modeles-datasets.html)
