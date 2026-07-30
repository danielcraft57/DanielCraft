# Chapitre 11 - Transfer learning : reutiliser un cerveau deja forme

Le **transfer learning**, c'est repartir d'un modele deja entraine sur une tache large - reconnaitre des objets sur des millions d'images, ou un modele de langage sur d'enormes corpus - et l'adapter a ton cas avec moins de donnees. Au lieu d'apprendre tout **from scratch**, tu reutilises des representations utiles.

Chez DanielCraft, c'est souvent le geste 2026 par defaut. Les donnees labellisees coutent cher. Les modeles fondation existent. Reutiliser avant de reentrainer le monde n'est pas de la paresse : c'est de l'ingenierie.

:::retenir
Transfer learning = reutiliser un modele preentraine et l'adapter. Moins de donnees, moins de calcul, souvent meilleur depart.
:::

## Ce que ce n'est pas

Ce n'est pas une dispense de validation. Ce n'est pas magique si ton domaine est trop eloigne ou si tes labels sont sales - tu transfers aussi vers le sale. Ce n'est pas non plus "interdire le from scratch pour toujours" : parfois le domaine l'exige, avec budget et donnees. Et ce n'est pas synonyme exact de prompting : le prompting conditionne sans maj de poids ; le transfer, au sens strict, adapte des poids (meme legerement).

Tu embauches quelqu'un qui a deja vu des millions d'objets, et tu lui apprends tes pieces detachees. Tu ne reprends pas l'alphabet visuel a zero. Ines telecharge un CNN preentraine, remplace la tete de classification, entraine surtout les dernieres couches. Sur le texte, on fine-tune legerement, ou on fait du prompting / RAG sans tout retoucher. L'esprit est le meme : partir d'un milieu deja riche.

```python
# Esquisse PyTorch : backbone gele + tete adaptee (N classes)
import torch.nn as nn
from torchvision import models

backbone = models.resnet18(weights="DEFAULT")
for p in backbone.parameters():
    p.requires_grad = False          # gele : on reutilise
backbone.fc = nn.Linear(backbone.fc.in_features, 5)  # 5 classes metier
# Ensuite : entrainer surtout backbone.fc, learning rate petit, early stopping
```

:::astuce
Ecris "ce que je reutilise" et "ce que j'adapte". Si les deux cases sont vides, tu n'as pas encore de plan transfer.
:::

## Strategies

Geler beaucoup de couches, entrainer la tete. Puis parfois deverrouiller plus profond a petit learning rate. Adapter avec peu de parametres (**LoRA** et cousins dans le monde LLM). Surveiller l'overfitting : meme un modele preentraine peut coller a 100 images. Lea met dans ses contrats : "strategie de gel / degel documentee, learning rates, critere d'arret".

## Domaine shift

Si tes images de pieces sont grasses, floues, mal eclairees, et que le modele preentraine a vu des photos web propres, tu as un ecart de domaine. Le transfert aide encore souvent, mais prevois plus d'exemples cibles, une augmentation realiste, et une evaluation sur le vrai terrain. Max le rappelle : "mes photos ne sont pas Instagram".

## Petite histoire

Ines compare from scratch (echec) et transfer (debut utile). Elle gele le backbone, entraine la tete, regarde val. Puis elle degele quelques couches a petit pas. Elle documente. Quand un investisseur demande "vous avez invente l'architecture ?", elle repond "non, on a adapte proprement". Chez DanielCraft, cette honnetete vend mieux que le mythe du genie solitaire.

## Limites

Domaine trop eloigne : transfert plus difficile. Labels sales : transfert du sale. Licences et couts des modeles : a lire. Catastrophic forgetting : reentrainer tout a gros learning rate peut detruire les representations utiles. Sam fait un schema au tableau : "petit pas sur un geant > grand pas qui ecrase le geant".

## Erreur classique

Reentrainer tout a gros learning rate et detruire les representations utiles. Ou croire que transfer learning dispense de validation. Ou ignorer la licence du modele fondation.

:::attention
Adapter n'abolit pas mesurer. Le preentraine arrive avec des biais et des angles morts : teste sur ton terrain.
:::

## En vrai

Choisis un modele fondation (vision ou texte) que tu reuserais. Ecris ce que tu adapterais : classes, style, documents, tete de sortie.

## A toi

Decris le modele fondation, la strategie (gele / tete / LoRA...), le volume de donnees estime, et le critere go/no-go. Une demi-page max.

## Prompting, RAG, fine-tune

Trois leviers voisins, forces differentes. Prompting : rapide, pas de maj de poids. RAG : injecte des faits dans le contexte. Fine-tune / transfer : change le comportement du modele sur ton domaine. Ines les range dans cet ordre de cout. Elle monte d'un cran seulement si le cran d'en dessous ne suffit pas. C'est la discipline du chapitre.

## LoRA et adaptation legere (idee)

Dans le monde LLM, on adapte parfois avec peu de parametres ajoutes (LoRA et cousins) plutot que de tout retoucher. Esprit voisin du transfer : changer peu, garder beaucoup. Tu n'as pas a implementer LoRA ici. Tu dois savoir que "fine-tune" n'egal pas toujours "reecrire le geant". Lea exige qu'on precise la methode et le cout avant de signer.

## Licence et provenance

Un modele fondation a une licence, une provenance de donnees, parfois des restrictions commerciales. Lire avant d'integrer. Sam le met dans sa grille ethique scolaire version legere : "d'ou vient le cerveau que tu reuses ?". Chez DanielCraft, le transfer sans lecture de licence est une dette, pas une astuce.

## Ordre des leviers (rappel)

1) Modele preentraine + tete. 2) Data meilleure / plus realiste. 3) Degeler un peu. 4) Methodes legeres type LoRA si LLM. 5) From scratch seulement avec preuves. Cet ordre evite 80 % des derivations couteuses. Lea l'imprime ; Max le simplifie en "reutiliser, mesurer, puis seulement compliquer".
