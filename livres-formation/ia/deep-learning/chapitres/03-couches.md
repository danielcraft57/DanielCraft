# Chapitre 3 - Couches : empiler des transformations

Une **couche**, c'est un groupe de neurones qui recoivent les sorties de la couche precedente. Couche d'**entree** : tes donnees (pixels, embeddings de tokens, mesures). Couches **cachees** : transformations internes. Couche de **sortie** : prediction - classes, nombres, tokens suivants. Empiler, c'est composer : chaque etage prepare le terrain pour le suivant.

Chez DanielCraft, on compare ca a une chaine de fabrication. La premiere station nettoie et detecte des motifs simples. Les suivantes assemblent. La derniere etiquette. Si tu ajoutes des stations sans matiere premiere ni controle qualite, tu n'obtiens qu'une usine chere qui memorise le bruit.

:::retenir
Une couche transforme une representation en une autre. La profondeur est un compromis, pas un trophee.
:::

## Ce que ce n'est pas

Ce n'est pas un concours : "plus deep = plus moderne = mieux". Trop de couches sans donnees, c'est de l'overfitting et du cout. Ce n'est pas non plus obligatoire de visualiser chaque neurone. Et ce n'est pas la meme chose d'elargir une couche (plus de neurones) et d'approfondir (plus de couches) : les effets different.

Au debut du reseau, l'entree est brute. Au milieu, des motifs. A la fin, une decision. Une bonne representation rend le probleme plus simple pour la couche suivante. Sur une image, les premieres couches d'un CNN tendent a detecter des motifs locaux simples ; plus loin, des formes plus abstraites. Dans le texte, des couches successives melangent le contexte. Tu retiens l'idee : le reseau apprend aussi **comment representer** l'entree, pas seulement la derniere case a cocher.

Ines dessine trois etages pour ses pieces : entree image, cachee "motifs", sortie "classe". C'est grossier. C'est deja utile pour briefer.

```python
# Empilement dense minimal (PyTorch) : entree -> cachee -> sortie
import torch
import torch.nn as nn

class MiniMLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(4, 8),   # 4 mesures en entree
            nn.ReLU(),
            nn.Linear(8, 3),   # 3 classes en sortie (scores bruts)
        )

    def forward(self, x):
        return self.net(x)

modele = MiniMLP()
x = torch.randn(2, 4)          # 2 exemples, 4 features
logits = modele(x)
print(logits.shape)            # torch.Size([2, 3])
```

Tu n'as pas encore appris : tu as juste empile. L'apprentissage viendra avec une loss et des poids qui bougent.

## Profondeur et largeur

Plus de couches peuvent representer des fonctions plus riches - mais coutent plus cher a entrainer, et overfitent plus facilement si les donnees manquent. Elargir augmente la capacite locale ; approfondir compose des transformations. Les architectures modernes jouent sur des blocs repetes, des connexions residuelles, des normes - details que tu rencontreras plus tard. Ici, retiens le levier : **forme du reseau = hypothese sur la structure du probleme**.

:::astuce
Avant d'ajouter une couche, ecris ce que tu esperes qu'elle apporte. Si tu ne sais pas, ne l'ajoute pas encore.
:::

## Fully connected vs specialise

Une couche **dense** (fully connected) relie tout a tout. Sur une grande image aplaties, les parametres explosent. Les **CNN** partagent des filtres locaux. Les **transformers** utilisent l'attention pour relier des positions d'une sequence. L'architecture encode un a priori : localite pour l'image, dependances contextuelles pour le langage. Choisir une famille, c'est choisir un a priori - on y revient au chapitre "choix d'architecture".

## Petite histoire

Sam a demande a sa classe de dessiner un reseau spam/texte court : entree, une cachee, sortie. Un eleve a ajoute quinze couches "parce que deep". Sam a demande : "tu as combien d'exemples labels ?" L'eleve : "quarante". La classe a compris plus vite qu'avec un cours d'une heure. Lea, elle, a vu le meme piege chez un prestataire qui vendait "un reseau a 40 couches" pour classer trois types de formulaires PDF. Elle a exige une baseline simple d'abord. La baseline a presque suffi.

## Erreur classique

Ajouter des couches parce que "deep = moderne" sans mesurer. Ou ignorer la taille d'entree : aplatir une image 4K dans une couche dense naive, c'est une explosion de parametres et souvent une mauvaise idee. Autre piege : croire que la couche de sortie "comprend" ; elle ne fait que lire la representation fournie par le dessus.

:::attention
L'architecture n'est pas une garantie de qualite. Donnees, validation et usage font le resultat.
:::

## En vrai

Dessine sur papier un reseau a 3 etages pour une tache simple de ton monde. Nomme entree, cachee, sortie. Une phrase par etage : "ici j'espere que...".

## A toi

Dessine un reseau a 3 etages pour classer spam / texte court : entree, cachee, sortie. Que sort la derniere couche (2 scores ? 1 probabilite ?) ? Justifie en trois phrases.

## Representations utiles

Une representation utile separe mieux les classes, ou prepare mieux la generation du prochain token. Transfer learning = reutiliser un milieu deja riche. RAG cote LLM = injecter des faits dans le contexte plutot que de tout stocker dans les poids. Prompting = conditionner la representation de sortie sans maj de poids. Ces leviers reviendront ; ils parlent tous le langage des couches.

## Scene Ines

Ines compare deux plans : un reseau dense naif sur pixels aplatis, et un CNN preentraine. Le premier a l'air "simple a expliquer". Le second respecte la localite de l'image. Elle choisit le second, non par snobisme, mais parce que l'a priori matche le probleme. Chez DanielCraft, matcher le probleme bat impresionner la slide.

## Lire une architecture comme un brief

Quand un prestataire dit "on a 12 couches", demande ce que font les blocs, quelle entree, quelle sortie, quel preentrainement. Ines a appris a exiger un schema une page. Lea refuse les slides sans dimensions d'entree. Sam fait dessiner le schema avant tout jargon. La couche n'est pas un badge : c'est une hypothese sur la transformation.

## Connexions residuelles (apercu)

Les reseaux tres profonds ajoutent parfois des raccourcis pour laisser le signal et le gradient circuler plus facilement. Tu n'as pas a les reinventer. Sache qu'elles existent, et que "plus profond" a ete rendu praticable aussi par ce genre d'astuces d'architecture, pas seulement par plus de GPU.
